#此文件用于演示如何处理可执行文件的日志

# 运行并结束
bin.log.normal.case: LFLAGS:=-b -o run
bin.log.normal.case: lldb/bin_log

# 运行并结束 + grep 过滤日志
bin.log.grep.case: LFLAGS:=-b -o run
bin.log.grep.case: ARGS:=| grep 0
bin.log.grep.case: lldb/bin_log
# lldb -b -o run -- build/bin_log.bin | grep 0

# 正常运行并结束 + grep 过滤日志
bin.log.grep.step.case: LFLAGS:=-b -o 'run | grep 0'
bin.log.grep.step.case: lldb/bin_log

#日志保存到文件中
bin.log.file.case: LFLAGS:=-b -o 'process launch -o bin.log'
bin.log.file.case: lldb/bin_log

# 只能执行第一个先决条件，why？
bin.log.cases: bin.log.normal.case bin.log.grep.case bin.log.grep.step.case bin.log.file.case
