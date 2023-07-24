# 本文件记录执行 LLDB 命令相关的内容

LFLAGS:=# LLDB 选项
# 直接执行 LLDB
lldb:
	lldb $(LFLAGS) $(ARGS)
# 执行 LLDB 时，跟随应用和参数
lldb/%: $(BUILD)/%.bin
	lldb $(LFLAGS) -- $< $(ARGS)

# 使用 LLDB 执行 empty 应用
lldb.empty.case: lldb/empty;
lldb.basic_flow.case: lldb/basic_flow;
