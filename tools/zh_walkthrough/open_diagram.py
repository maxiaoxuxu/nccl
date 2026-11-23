"""Open the offline walkthrough at an editor's current source line."""
import argparse
from pathlib import Path
from urllib.parse import urlencode
import webbrowser

root = Path(__file__).resolve().parents[2]
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("--file", required=True, type=Path)
parser.add_argument("--line", type=int, required=True)
parser.add_argument("--print-url", action="store_true")
args = parser.parse_args()
source = args.file.resolve() if args.file.is_absolute() else (root / args.file).resolve()
if not source.is_relative_to(root / "src") or not source.is_file():
    parser.error("请选择本仓库 src 目录中的源文件")
if not 1 <= args.line <= len(source.read_bytes().splitlines()):
    parser.error("行号超出文件范围")
reader = root / "docs/zh_CN/reader.html"
url = reader.as_uri() + "#" + urlencode({"file": source.relative_to(root).as_posix(), "line": args.line})
if args.print_url:
    print(url)
else:
    webbrowser.open(url)
