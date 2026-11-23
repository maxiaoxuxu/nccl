"""Verify annotated blobs, local references and source-derived CPU examples. Run from any directory."""
import argparse
import hashlib
from pathlib import Path
import re
import subprocess
import sys
import tempfile
from urllib.parse import unquote
from xml.etree import ElementTree

ROOT = Path(__file__).resolve().parents[2]
DOC = ROOT / "docs/zh_CN"
BASE = "ad2d192c1f279aefcaf340f67e07880b65a1116b"
NOTES = re.compile(rb" /\* " + "中文索引·".encode() + rb"[^\n]*? \*/|/\* " + "中文图解·".encode() + rb"[^\n]*? \*/ ")


def verify_sources():
    listing = subprocess.check_output(["git", "ls-tree", "-r", "-z", BASE, "--", "src"], cwd=ROOT)
    annotated = notes = 0
    for entry in listing.rstrip(b"\0").split(b"\0"):
        meta, path = entry.split(b"\t", 1)
        data = (ROOT / path.decode()).read_bytes()
        clean, count = NOTES.subn(b"", data)
        digest = hashlib.sha1(b"blob %d\0" % len(clean) + clean).hexdigest()
        assert digest == meta.split()[2].decode(), path.decode()
        annotated += count != 0
        notes += count
    print(f"源码还原通过：{annotated} 个带注释文件，{notes} 处注释。")


def verify_links():
    files = [ROOT / "START_HERE_ZH.md", *DOC.rglob("*.md")]
    n = 0
    for file in files:
        for target in re.findall(r"\]\(([^)\s]+)\)", file.read_text()):
            if target.startswith(("https:", "http:", "#")):
                continue
            path, _, anchor = target.partition("#")
            link = (file.parent / unquote(path)).resolve()
            assert link.exists(), (file, target)
            if re.fullmatch(r"L\d+", anchor):
                assert 1 <= int(anchor[1:]) <= len(link.read_bytes().splitlines()), (file, target)
            n += 1
    for svg in (DOC / "figures").glob("*.svg"):
        ElementTree.parse(svg)
    print(f"文档链接及行号通过：{n} 个本地引用。")


def compile_examples():
    # Keep function bodies from the branch verbatim, including the CUDA ring loop.
    def extract(file, first, last="\n}"):
        text = NOTES.sub(b"", (ROOT / file).read_bytes()).decode()
        start = text.index(first)
        end = text.index(last, start) + len(last)
        return text[start:end] + "\n"

    defs = [
        ("src/include/device.h", "#define WARP_SIZE ", "\n"),
        ("src/include/device.h", "#define NCCL_LL_MAX_NTHREADS ", "\n"),
        ("src/include/nccl_device/impl/ll__types.h", "#define NCCL_LL_LINES_PER_THREAD ", "\n"),
        ("src/include/nccl_device/impl/ll__types.h", "union ncclLLFifoLine {", "\n};"),
        ("src/include/device.h", "#define NCCL_STEPS ", "\n"),
        ("src/include/device.h", "#define NCCL_MAX_TREE_ARITY_TOP ", "\n"),
        ("src/include/device.h", "#define NCCL_MAX_TREE_ARITY ", "\n"),
        ("src/include/device.h", "constexpr int ncclFlowTreeIndexChild0", ";"),
        ("src/include/device.h", "constexpr int ncclFlowTreeIndexChild1", ";"),
        ("src/include/device.h", "struct ncclTree {", "\n};"),
        ("src/include/coll_sizes.h", "inline int ncclGetChunkSteps("),
        ("src/include/coll_sizes.h", "inline int ncclGetSliceSteps("),
        ("src/include/coll_sizes.h", "inline size_t ncclGetChunkSize("),
        ("src/include/coll_sizes.h", "#define ALLREDUCE_SLICESTEPS ", "\n"),
        ("src/include/coll_sizes.h", "#define ALLREDUCE_CHUNKSTEPS ", "\n"),
        ("src/include/channel.h", "static constexpr size_t ncclMinTrafficPerChannel", ";"),
        ("src/include/channel.h", "struct ncclCollChannelLayout {", "\n};"),
        ("src/channel.cc", "size_t ncclCollTrafficPerChannel("),
        ("src/channel.cc", "struct ncclCollChannelLayout ncclComputeCollChannelLayout("),
        ("src/include/device.h", "struct alignas(16) ncclDevWorkColl {", "\n};"),
        ("src/include/device.h", "__host__ __device__ constexpr int ncclProtoGrainSize("),
        ("src/include/device.h", "template <typename Int>\n__host__ __device__ inline void ncclCollCbdPart("),
        ("src/include/device.h", "inline __host__ __device__ void ncclP2pPartBounds("),
        ("src/include/coll_sizes.h", "template <typename Int>\n__host__ __device__ inline Int ncclSimpleSliceSize("),
        ("src/include/coll_sizes.h", "template <typename Int>\n__host__ __device__ inline Int ncclElementAlignedDivUp("),
    ]
    header = (Path(__file__).with_name("cpu_ring.cc.in")).read_text()
    for macro in ("NCCL_PROTO_SIMPLE", "NCCL_PROTO_LL", "NCCL_PROTO_LL128", "NCCL_ALGO_RING", "NCCL_ALGO_TREE"):
        defs.insert(0, ("src/include/plugin/nccl_tuner.h", "#define " + macro + " ", "\n"))
    ll128_types = "src/include/nccl_device/impl/ll128__types.h"
    for macro in ("NCCL_LL128_LINESIZE", "NCCL_LL128_LINEELEMS", "NCCL_LL128_DATAELEMS",
                  "NCCL_LL128_SHMEM_ELEMS_PER_THREAD", "NCCL_LL128_ELEMS_PER_THREAD", "NCCL_LL128_MAX_NTHREADS"):
        defs.insert(0, (ll128_types, "#define " + macro + " ", "\n"))
    defs.extend([
        ("src/init.cc", "#define DEFAULT_LL_BUFFSIZE ", "))\n"),
        ("src/init.cc", "#define DEFAULT_LL128_BUFFSIZE ", "\n"),
        ("src/init.cc", "#define DEFAULT_BUFFSIZE ", "\n"),
    ])
    funcs = "\n".join(extract(*args) for args in defs)
    ring = extract("src/device/all_reduce.h", "template <typename T, typename RedOp, typename Proto>\n__device__ __forceinline__ void runRing(")
    code = header.replace("/* SOURCE_HELPERS */", funcs).replace("/* SOURCE_RING */", ring)
    # Run the actual argument to waitSend with a CPU recorder. Memory accesses
    # and the CUDA synchronization surrounding the expression stay on the device.
    for marker, file, constants in (
        ("LL_LENGTH", "src/device/prims_ll.h", ["EltPerLine"]),
        ("LL128_LENGTH", "src/device/prims_ll128.h", ["WireWordPerSlice", "DataEltPerSlice"]),
    ):
        declarations = "".join(extract(file, "static constexpr int " + name + " =", ";") for name in constants)
        length = extract(file, "if (SEND) waitSend(divUp(nelem,", ";")
        code = code.replace("/* " + marker + " */", declarations + length)
    tree_defs = [
        ("src/graph/trees.cc", "ncclResult_t ncclGetBtree("),
        ("src/graph/trees.cc", "ncclResult_t ncclGetDtree("),
        ("src/graph/connect.cc", "static ncclResult_t setTreeUp("),
        ("src/graph/connect.cc", "static ncclResult_t setTreeDown("),
        ("src/graph/connect.cc", "static ncclResult_t connectTrees("),
    ]
    for name in ("runTreeSplit", "runTreeUpDown"):
        tree_defs.append(("src/device/all_reduce.h",
                          "template <typename T, typename RedOp, typename Proto>\n"
                          "__device__ __forceinline__ void " + name + "("))
    tree_test = Path(__file__).with_name("cpu_tree.cc.in").read_text()
    code = code.replace("/* TREE_TEST */", tree_test.replace("/* SOURCE_TREE */",
                        "\n".join(extract(*args) for args in tree_defs)))
    with tempfile.TemporaryDirectory() as tmp:
        path = Path(tmp)
        (path / "test.cc").write_text(code)
        subprocess.run(["c++", "-std=c++17", "-O2", str(path / "test.cc"), "-o", str(path / "test")], check=True)
        subprocess.run([str(path / "test")], check=True)


def verify_reader():
    from base64 import b64decode
    import gzip
    from html.parser import HTMLParser
    import json
    from urllib.parse import parse_qs

    reader = (DOC / "reader.html").read_text()

    def payload(element):
        return re.search(r'<script[^>]* id="' + element + r'"[^>]*>(.*?)</script>', reader, re.S)[1]

    chapters = json.loads(payload("chapters"))
    figures = json.loads(payload("figs"))
    db = json.loads(gzip.decompress(b64decode(payload("packed"))))
    for path, source in db["source"].items():
        assert (ROOT / path).read_bytes() == source.encode(), path
    for path, notes in db["manual"].items():
        lines = db["source"][path].splitlines()
        for line, (figure, note) in notes.items():
            assert figure in figures and note in lines[int(line) - 1], (path, line)
    for figure, uri in figures.items():
        data = b64decode(uri.split(",", 1)[1])
        assert (DOC / "figures" / (figure + ".svg")).read_bytes() == data, figure

    class ChapterLinks(HTMLParser):
        def handle_starttag(self, tag, attrs):
            attrs = dict(attrs)
            if tag == "img":
                assert attrs["src"] in figures.values(), attrs["src"][:80]
            if tag == "a":
                href = attrs["href"]
                assert href.startswith("#"), href
                params = parse_qs(href[1:])
                if "file" in params:
                    lines = db["source"][params["file"][0]].splitlines()
                    assert 1 <= int(params["line"][0]) <= len(lines), href
                else:
                    assert params["chapter"][0] in chapters, href

    for _, body in chapters.values():
        ChapterLinks().feed(body)
    print(f"离线文件通过：{len(chapters)} 个专题，{len(figures)} 张内嵌原图，{len(db['source'])} 个源码文件。")


if __name__ == "__main__":
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--docs-only", action="store_true")
    args = p.parse_args()
    verify_links()
    verify_reader()
    if not args.docs_only:
        verify_sources()
        compile_examples()
