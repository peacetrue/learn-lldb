#此文件用于演示如何处理可执行文件的日志

# 运行并结束
bin.log.normal.case: LFLAGS:=-b -o run
bin.log.normal.case: lldb/bin_log

# 运行并结束 + grep 过滤日志
bin.log.grep.case: LFLAGS:=-b -o run
bin.log.grep.case: ARGS:=| grep log-0
bin.log.grep.case: lldb/bin_log

# 正常运行并结束 + grep 过滤日志
bin.log.grep.step.case: LFLAGS:=-b -o "run | grep log-0"
bin.log.grep.step.case: lldb/bin_log

#日志保存到文件中
# shell cat build/bin.log | grep log-0 : Linux 可用
# shell sh -c 'cat $(BUILD)/bin.log | grep log-0'" : macOS 上可用
bin.log.file.case: LFLAGS:=-b -o "process launch -o $(BUILD)/bin.log" -o "shell sh -c 'cat $(BUILD)/bin.log | grep log-0'"
bin.log.file.case: clean/bin.log lldb/bin_log

