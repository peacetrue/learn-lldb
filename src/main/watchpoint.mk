
# 观察点案例，进程运行起来后，才能设置观察点
watchpoint.case: $(BUILD)/watchpoint.source
	echo "b main" > $<
	echo "run" >> $<
	echo "watchpoint set variable a" >> $<
#	echo "watchpoint set expression -w write -s 1 -- a + 32" >> $<
	echo "n" >> $<
	make lldb/watchpoint LFLAGS="-b -s $<"
