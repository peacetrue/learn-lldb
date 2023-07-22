# error: Command requires a current process.
requires.process.error.case: script/requires_process.py $(BUILD)/empty.bin
	lldb -o 'command script import $<' -- $(word 2,$^)

requires.process.correct.case: source/requires.process.source $(BUILD)/empty.bin
	lldb -b -s $< -- $(word 2,$^)

requires.process.case: requires.process.error.case requires.process.correct.case;

