def __lldb_init_module(debugger, internal_dict):
    debugger.HandleCommand(f'shell echo "__lldb_init_module"')
    debugger.HandleCommand("expr int $a=1")
