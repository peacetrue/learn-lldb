# ASLR 的全称是 "Address Space Layout Randomization"，即地址空间布局随机化
#Linux 上设置开启/禁用地址随机化
aslr/%:
	@sysctl -a | grep kernel.randomize_va_space
	@sysctl -w kernel.randomize_va_space=$*
#	cp /etc/sysctl.conf /etc/sysctl.conf.bak
#	echo 'kernel.randomize_va_space = 0' >> /etc/sysctl.conf
#	sysctl -p
aslr.enable: aslr/2
aslr.disable: aslr/0

aslr.times:=2
# 不使用 lldb 直接运行
aslr.run.case: $(BUILD)/aslr.bin; $(shell yes "$<;" | head -n $(aslr.times))
# 使用 lldb 运行 # settings set target.disable-aslr false
aslr.lldb.name:=default enable disable
aslr.lldb.targets:=$(addsuffix .case,$(addprefix aslr.,$(aslr.lldb.name)))
# linux 上 yes "-o" 导致 yes: invalid option -- 'o' 改为 yes " -o"
aslr.default.case: LFLAGS:=-b $(shell yes " -o 'process launch'" | head -n $(aslr.times))
aslr.enable.case: LFLAGS:=-b $(shell yes " -o 'process launch -A false'" | head -n $(aslr.times))
aslr.disable.case: LFLAGS:=-b $(shell yes " -o 'process launch -A true'" | head -n $(aslr.times))
$(aslr.lldb.targets): ARGS:=| grep elf
$(aslr.lldb.targets): lldb/aslr

aslr.cases:
	make aslr.run.case
	@for target in $(aslr.lldb.targets) ; do\
	    make $$target;\
	done
