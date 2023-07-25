# 用于指示 LLDB 启动一个 REPL（Read-qEval-Print Loop）环境。与普通模式相比，允许您直接在调试器中执行代码片段
repl.case:
	make init.global.case LFLAGS=-r
