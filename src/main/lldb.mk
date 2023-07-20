# 执行 lldb
lldb:
	lldb $(LFLAGS) $(ARGS)
lldb/%: $(BUILD)/%.bin
	lldb $(LFLAGS) -- $< $(ARGS)
