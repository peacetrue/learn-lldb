# 构建相关：编译、链接
#.SILENT:#静默模式，不会输出执行的命令
CFLAGS:=-g #生成调试信息

# gcc 编译
$(BUILD)/%.bin: $(BUILD)
$(BUILD)/%.bin: $(BUILD)/%.s $(BUILD)
	gcc $(CFLAGS) -o $@ $<
$(BUILD)/%.bin: c/%.c $(BUILD)
	gcc $(CFLAGS) -o $@ $<
$(BUILD)/%.bin: cpp/%.cpp $(BUILD)
	gcc $(CFLAGS) -o $@ $<

