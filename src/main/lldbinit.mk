# lldb 初始化配置

# 在 lldb 命令行打印信息
lldb_echo=shell echo 'lldb: $(1)'
# 默认全局配置
init-global:
	echo "$(call lldb_echo,~/.lldbinit)" > ~/.lldbinit
# 应用全局配置：命令行、Xcode
init-global/%:
	echo "$(call lldb_echo,~/.lldbinit-$*)" > ~/.lldbinit-$*
# 命令行全局配置
init-cmd: init-global/lldb init-global;
init-clion: init-global/CLion init-global;
init-local: init-global
	echo "settings set target.load-cwd-lldbinit true" >> ~/.lldbinit
	echo "$(call lldb_echo,./.lldbinit)" > ./.lldbinit
clean/init:
	rm -rf ~/.lldbinit ~/.lldbinit-* ./.lldbinit

# 初始化相关案例
## 清除配置文件
#init.none.case init.none.option.case init.global.case init.cmd.case init.local.case: LFLAGS+=-b -o "sh echo ''"
init.none.case: clean/init lldb;
init.global.case: init-global lldb;
# 命令行优先级高于全局默认，会顶替掉全局默认
init.cmd.case: clean/init init-cmd lldb;
init.local.case: clean/init init-local lldb;

## 初始化时创建变量，后续打印变量。make 传递参数十分诡异
#init-expr: clean/init init-global
#	echo "expr int \$$a=1;" >> ~/.lldbinit
#init.expr.case:
#	make init-expr lldb LFLAGS="-b -O \"p \\$$\$$a\""
