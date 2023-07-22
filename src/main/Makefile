include build.common.mk
include build.elf.mk
include lldb.mk
include aslr.mk
include bin_log.mk
include dmbsd.mk
include requires.process.mk

%: $(BUILD)/%;

# lldb 调试 C 语言
empty.case: lldb/empty;
# lldb 调试汇编语言
empty.asm.case: lldb/empty.asm;
$(BUILD)/%.asm.s: c/%.c
	cc -S -o $@ $<

# 在 lldb 命令行打印信息
lldb_echo=shell echo 'lldb: $(1)'
#全局默认
init-global:
	echo "$(call lldb_echo,~/.lldbinit)" > ~/.lldbinit
#应用特定
init/%:
	echo "$(call lldb_echo,~/.lldbinit-$*)" > ~/.lldbinit-$*
#命令行特定
init-cmd: init/lldb init-global;
init-local: init-global
	echo "settings set target.load-cwd-lldbinit true" >> ~/.lldbinit
	echo "$(call lldb_echo,./.lldbinit)" > ./.lldbinit
clean/init:
	rm -rf ~/.lldbinit
	rm -rf ~/.lldbinit-lldb
	rm -rf ./.lldbinit
# 创建一个 source 文件
$(BUILD)/%.source: $(BUILD)
	echo "$(call lldb_echo,$*)" > $@


# 初始化相关案例
## 清除配置文件
init.none.case: clean/init lldb;
## 禁止使用配置文件
init.none.option.case:
	make lldb LFLAGS=--no-lldbinit
init.global.case: init-global lldb;
# 命令行优先级高于全局默认，会顶替掉全局默认，注意不是内容覆盖
init.cmd.case: clean/init init-cmd lldb;
init.local.case: init-local lldb;

# 初始化时创建变量，后续打印变量。make 传递参数十分诡异
init-expr: clean/init init-global
	echo "expr int \$$a=1;" >> ~/.lldbinit
init.expr.case:
	make init-expr lldb LFLAGS="-b -O \"p \\$$\$$a\""

# 观察点案例，进程运行起来后，才能设置观察点
watchpoint.case: $(BUILD)/watchpoint.source
	echo "b main" > $<
	echo "run" >> $<
	echo "watchpoint set variable a" >> $<
#	echo "watchpoint set expression -w write -s 1 -- a + 32" >> $<
	echo "n" >> $<
	make lldb/watchpoint LFLAGS="-b -s $<"

# 初始化时导入脚本，然后在脚本中创建变量，后续打印变量
init-script: clean/init init-local
	echo "command script import script/commands.py" >> ./.lldbinit
init.script.case:
	make init-script lldb LFLAGS=" -O \"p \\$$\$$a\""

lflags+= -b
#lflags+= -Q
lflags+= -O \"$(call lldb_echo,--one-line-before-file)\"
lflags+= -o \"$(call lldb_echo,--one-line-after-file)\"
lifecycle.case: $(BUILD)/source-before-file.source $(BUILD)/source-after-file.source
	make init-local lldb/empty LFLAGS="$(lflags) -S $(word 1,$^) -s $(word 2,$^)"

# 用于指示 LLDB 启动一个 REPL（Read-qEval-Print Loop）环境。与普通模式相比，允许您直接在调试器中执行代码片段
repl.case:
	make init.global.case LFLAGS=-r

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

# 将 man 手册生成 adoc 文档
adoc.case: script/adoc.py
	lldb -b -O "command script import $<"
	command -v antora && cd ../../docs/antora && antora generate playbook.yml || true

