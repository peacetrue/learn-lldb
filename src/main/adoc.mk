# 将 命令的 help 信息生成 adoc 文档
adoc.case: script/adoc.py
	lldb -b -O "command script import $<"
	command -v antora && cd ../../docs/antora && antora generate playbook.yml || true
