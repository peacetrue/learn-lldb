# https://stackoverflow.com/questions/33333165/how-to-switch-between-source-code-debug-mode-and-disassembly-debug-mode-in-lldb
# 执行 lldb
lldb:
	lldb $(LFLAGS) $(ARGS)
lldb/%: $(BUILD)/%.bin
	lldb $(LFLAGS) -- $< $(ARGS)
