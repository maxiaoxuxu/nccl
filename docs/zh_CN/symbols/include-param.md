# include-param 的定义位置

每项列出定义名和起始行；同一个名字可有多个重载与特化。

## src/include/param/common.h

[整个文件](../../../src/include/param/common.h)

- 结构体 [ncclParamInterface · L68](../../../src/include/param/common.h#L68)

## src/include/param/param.h

[整个文件](../../../src/include/param/param.h)

- 结构体 [ncclParam · L53](../../../src/include/param/param.h#L53)
- 函数 [ncclParam · L71](../../../src/include/param/param.h#L71)
- 函数 [operator() · L87](../../../src/include/param/param.h#L87)
- 函数 [getRawData · L93](../../../src/include/param/param.h#L93)
- 函数 [toString · L105](../../../src/include/param/param.h#L105)
- 函数 [dump · L110](../../../src/include/param/param.h#L110)
- 函数 [ensureLoaded · L134](../../../src/include/param/param.h#L134)
- 函数 [loadValue · L156](../../../src/include/param/param.h#L156)
- 函数 [ncclParam&lt;const char*&gt;::operator() · L181](../../../src/include/param/param.h#L181)
- 函数 [ncclParam&lt;const char*&gt;::loadValue · L190](../../../src/include/param/param.h#L190)
- 函数 [ncclParam&lt;const char*&gt;::getRawData · L211](../../../src/include/param/param.h#L211)

## src/include/param/param_registry.h

[整个文件](../../../src/include/param/param_registry.h)

- 类 [ncclParamRegistry · L45](../../../src/include/param/param_registry.h#L45)
- 结构体 [mapEntry · L47](../../../src/include/param/param_registry.h#L47)
- 结构体 [registryState · L53](../../../src/include/param/param_registry.h#L53)

## src/include/param/parser_bitset.h

[整个文件](../../../src/include/param/parser_bitset.h)

- 结构体 [bitsetCtx · L21](../../../src/include/param/parser_bitset.h#L21)
- 函数 [bitsetResolve · L28](../../../src/include/param/parser_bitset.h#L28)
- 函数 [bitsetValidate · L62](../../../src/include/param/parser_bitset.h#L62)
- 函数 [bitsetToString · L67](../../../src/include/param/parser_bitset.h#L67)
- 函数 [ncclParamBitsetOf · L104](../../../src/include/param/parser_bitset.h#L104)

## src/include/param/parser_combo.h

[整个文件](../../../src/include/param/parser_combo.h)

- 结构体 [comboCtx · L22](../../../src/include/param/parser_combo.h#L22)
- 函数 [comboResolve · L28](../../../src/include/param/parser_combo.h#L28)
- 函数 [comboValidate · L35](../../../src/include/param/parser_combo.h#L35)
- 函数 [comboToString · L42](../../../src/include/param/parser_combo.h#L42)
- 函数 [ncclParamCombo · L56](../../../src/include/param/parser_combo.h#L56)

## src/include/param/parser_common.h

[整个文件](../../../src/include/param/parser_common.h)

- 结构体 [ncclParamParser · L21](../../../src/include/param/parser_common.h#L21)
- 函数 [resolve · L33](../../../src/include/param/parser_common.h#L33)
- 函数 [validate · L36](../../../src/include/param/parser_common.h#L36)
- 函数 [toString · L39](../../../src/include/param/parser_common.h#L39)
- 结构体 [ncclOption · L65](../../../src/include/param/parser_common.h#L65)
- 结构体 [ncclOptionSet · L73](../../../src/include/param/parser_common.h#L73)
- 函数 [begin · L76](../../../src/include/param/parser_common.h#L76)
- 函数 [end · L79](../../../src/include/param/parser_common.h#L79)
- 函数 [size · L82](../../../src/include/param/parser_common.h#L82)
- 函数 [ncclOptionSetAssertUnique · L89](../../../src/include/param/parser_common.h#L89)
- 函数 [makeOption · L101](../../../src/include/param/parser_common.h#L101)
- 函数 [makeOption · L107](../../../src/include/param/parser_common.h#L107)
- 函数 [makeOptions · L113](../../../src/include/param/parser_common.h#L113)

## src/include/param/parser_default.h

[整个文件](../../../src/include/param/parser_default.h)

- 结构体 [ncclParamParserDefault · L23](../../../src/include/param/parser_default.h#L23)
- 函数 [resolve · L24](../../../src/include/param/parser_default.h#L24)
- 函数 [validate · L28](../../../src/include/param/parser_default.h#L28)
- 函数 [toString · L32](../../../src/include/param/parser_default.h#L32)
- 结构体 [ncclParamParserDefault&lt;bool&gt; · L41](../../../src/include/param/parser_default.h#L41)
- 函数 [resolve · L42](../../../src/include/param/parser_default.h#L42)
- 函数 [validate · L57](../../../src/include/param/parser_default.h#L57)
- 函数 [toString · L61](../../../src/include/param/parser_default.h#L61)
- 结构体 [ncclParamParserDefault&lt;const char*&gt; · L72](../../../src/include/param/parser_default.h#L72)
- 函数 [resolve · L73](../../../src/include/param/parser_default.h#L73)
- 函数 [validate · L78](../../../src/include/param/parser_default.h#L78)
- 函数 [toString · L82](../../../src/include/param/parser_default.h#L82)
- 函数 [validate · L91](../../../src/include/param/parser_default.h#L91)
- 结构体 [ncclIntegerParser · L91](../../../src/include/param/parser_default.h#L91)
- 函数 [resolve · L92](../../../src/include/param/parser_default.h#L92)
- 函数 [toString · L120](../../../src/include/param/parser_default.h#L120)
- 结构体 [ncclParamParserDefault&lt;int8_t&gt; · L129](../../../src/include/param/parser_default.h#L129)
- 结构体 [ncclParamParserDefault&lt;int16_t&gt; · L131](../../../src/include/param/parser_default.h#L131)
- 结构体 [ncclParamParserDefault&lt;int32_t&gt; · L133](../../../src/include/param/parser_default.h#L133)
- 结构体 [ncclParamParserDefault&lt;int64_t&gt; · L135](../../../src/include/param/parser_default.h#L135)
- 结构体 [ncclParamParserDefault&lt;uint8_t&gt; · L137](../../../src/include/param/parser_default.h#L137)
- 结构体 [ncclParamParserDefault&lt;uint16_t&gt; · L139](../../../src/include/param/parser_default.h#L139)
- 结构体 [ncclParamParserDefault&lt;uint32_t&gt; · L141](../../../src/include/param/parser_default.h#L141)
- 结构体 [ncclParamParserDefault&lt;uint64_t&gt; · L143](../../../src/include/param/parser_default.h#L143)
- 函数 [defaultResolve · L153](../../../src/include/param/parser_default.h#L153)
- 函数 [defaultValidate · L158](../../../src/include/param/parser_default.h#L158)
- 函数 [defaultToString · L163](../../../src/include/param/parser_default.h#L163)
- 结构体 [boundedCtx · L168](../../../src/include/param/parser_default.h#L168)
- 函数 [boundedValidate · L174](../../../src/include/param/parser_default.h#L174)
- 函数 [ncclParamBounded · L201](../../../src/include/param/parser_default.h#L201)
- 函数 [ncclParamBounded · L209](../../../src/include/param/parser_default.h#L209)

## src/include/param/parser_enum.h

[整个文件](../../../src/include/param/parser_enum.h)

- 函数 [oneOfLookup · L20](../../../src/include/param/parser_enum.h#L20)
- 函数 [oneOfResolve · L28](../../../src/include/param/parser_enum.h#L28)
- 函数 [oneOfValidate · L43](../../../src/include/param/parser_enum.h#L43)
- 函数 [oneOfToString · L48](../../../src/include/param/parser_enum.h#L48)
- 函数 [ncclParamOneOf · L60](../../../src/include/param/parser_enum.h#L60)

## src/include/param/parser_list.h

[整个文件](../../../src/include/param/parser_list.h)

- 结构体 [listOfCtx · L18](../../../src/include/param/parser_list.h#L18)
- 函数 [listOfResolve · L23](../../../src/include/param/parser_list.h#L23)
- 函数 [listOfValidate · L37](../../../src/include/param/parser_list.h#L37)
- 函数 [listOfToString · L42](../../../src/include/param/parser_list.h#L42)
- 函数 [ncclParamListOf · L59](../../../src/include/param/parser_list.h#L59)

## src/include/param/parsers.h

[整个文件](../../../src/include/param/parsers.h)

该文件可按路径打开；当前索引未识别带函数体或类型体的命名定义。

## src/include/param/utils.h

[整个文件](../../../src/include/param/utils.h)

- 函数 [ncclParamTypeIdOf · L43](../../../src/include/param/utils.h#L43)
- 函数 [flagsStr · L64](../../../src/include/param/utils.h#L64)
- 函数 [srcDefault · L83](../../../src/include/param/utils.h#L83)
- 函数 [srcEnvPlugin · L86](../../../src/include/param/utils.h#L86)
- 函数 [stringFormat · L93](../../../src/include/param/utils.h#L93)
- 函数 [iequals · L103](../../../src/include/param/utils.h#L103)
- 函数 [trim · L113](../../../src/include/param/utils.h#L113)
- 函数 [split · L121](../../../src/include/param/utils.h#L121)
