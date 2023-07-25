# 此文件演示 lldb 的脚本功能
script.case: script/read_me.py
	lldb -O "command script import $<"
