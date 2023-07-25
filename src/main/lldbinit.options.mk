# 初始化选项

# 创建一个 source 文件
$(BUILD)/%.source: $(BUILD)
	echo "$(call lldb_echo,$*)" > $@

# o 在 s 前
lflags= -b
lflags+= -O "$(call lldb_echo,--one-line-before-file)"
lflags+= -o "$(call lldb_echo,--one-line-after-file)"
lflags+= -S $(BUILD)/source-before-file.source
lflags+= -s $(BUILD)/source-after-file.source
lldbinit.options.case: LFLAGS=$(lflags)
lldbinit.options.case: $(BUILD)/source-before-file.source $(BUILD)/source-after-file.source clean/init init-local lldb/empty


# s 在 o 前
lflags= -b
lflags+= -S $(BUILD)/source-before-file.source
lflags+= -s $(BUILD)/source-after-file.source
lflags+= -O "$(call lldb_echo,--one-line-before-file)"
lflags+= -o "$(call lldb_echo,--one-line-after-file)"
lldbinit.options.order.case: LFLAGS=$(lflags)
lldbinit.options.order.case: $(BUILD)/source-before-file.source $(BUILD)/source-after-file.source clean/init init-local lldb/empty


