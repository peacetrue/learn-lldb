# 在源码调试模式和汇编调试模式之间转换
# debug mode between source code and disassembly = dmbsd
# https://stackoverflow.com/questions/33333165/how-to-switch-between-source-code-debug-mode-and-disassembly-debug-mode-in-lldb

# error: invalid enumeration value '1', valid values are: never, always, no-debuginfo, no-source
dmbsd.case: $(BUILD)/dmbsd.bin
	lldb -b -s source/dmbsd.source $<
