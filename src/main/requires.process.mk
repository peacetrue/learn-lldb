# error: Command requires a current process.
requires.process.error.case: script/requires_process.py $(BUILD)/empty.bin
	lldb -b -o 'command script import $<' -- $(word 2,$^)

requires.process.correct.case: source/requires.process.source $(BUILD)/empty.bin
	lldb -b -s $< -- $(word 2,$^)

requires.process.case: requires.process.error.case requires.process.correct.case;

# source 提供执行的命令列表，已有命令无法支持的，通过 py 脚本实现
# py 脚本提供自定义命令，不在初始化过程中提供命令列表
