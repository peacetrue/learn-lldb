# 本文件记录执行 LLDB 命令相关的内容

LFLAGS:=# LLDB 选项
# 直接执行 LLDB
lldb:
	lldb $(LFLAGS) $(ARGS)
# 执行 LLDB 时，跟随应用和参数
lldb/%: $(BUILD)/%.bin
	lldb $(LFLAGS) $< $(ARGS)

# 使用 LLDB 执行 empty 应用
lldb.empty.case: lldb/empty;
lldb.basic_flow.case: clean/basic_flow.bin lldb/basic_flow;

# 演示多个 target 相互切换，然后执行完成并退出
$(BUILD)/target.source: $(BUILD)/empty.bin $(BUILD)/basic_flow.bin
	echo "$(addprefix target create ,$(addsuffix \n,$^))" > $@
	echo "target list" >> $@
	echo "target select 0\n b main\n run" >> $@
	echo "target select 1\n b main\n run" >> $@
	echo "target select 0\n c" >> $@
	echo "target select 1\n c" >> $@
target.case: $(BUILD)/target.source
	lldb -b -S $(word 1,$^)



