# 同时调试源码和汇编代码

# error: invalid enumeration value '1', valid values are: never, always, no-debuginfo, no-source
# 没有调试信息时，按汇编调试
disassembly.nodebug.case: CFLAGS:=
disassembly.nodebug.case: clean/disassembly.bin lldb/disassembly

# 有调试信息时，按源码调试
disassembly.debug.case: clean/disassembly.bin lldb/disassembly

# 有调试信息时，同时按源码和汇编调试
disassembly.case: clean/disassembly.bin $(BUILD)/disassembly.bin
	lldb -b -s source/disassembly.source $(word 2,$^)
