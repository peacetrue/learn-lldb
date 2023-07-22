import lldb


def __lldb_init_module(debugger: lldb.SBDebugger, internal_dict: dict):
    debugger.HandleCommand(f"command script add -o -f {__name__}.command_r _r")
    debugger.HandleCommand(f"command script add -o -f {__name__}.command_c _c")
    debugger.HandleCommand(f"command script add -o -f {__name__}.command_r_c _r_c")
    r_c(debugger)


def view_lldb(debugger):
    # eCommandRequiresProcess = _lldb.eCommandRequiresProcess
    target: lldb.SBTarget = debugger.GetSelectedTarget()
    process: lldb.SBProcess = target.GetProcess()
    thread: lldb.SBThread = process.GetSelectedThread()
    frame: lldb.SBThread = thread.GetSelectedFrame()
    print(f"debugger: {lldb.debugger} - {debugger}")
    print(f"target: {lldb.target} - {target}")
    print(f"process: {lldb.process} - {process}")
    print(f"thread: {lldb.thread} - {thread}")
    print(f"frame: {lldb.frame} - {frame}")
    lldb.debugger = debugger
    lldb.process = process
    lldb.target = target
    lldb.thread = thread
    lldb.frame = frame


def command_r(debugger: lldb.SBDebugger, command: str, result: lldb.SBCommandReturnObject, internal_dict: dict):
    handle_command("r", debugger)


def command_c(debugger: lldb.SBDebugger, command: str, result: lldb.SBCommandReturnObject, internal_dict: dict):
    handle_command("c", debugger)


def command_r_c(debugger: lldb.SBDebugger, command: str, result: lldb.SBCommandReturnObject, internal_dict: dict):
    r_c(debugger)


def r_c(debugger):
    handle_command("b main", debugger)
    handle_command("r", debugger)
    handle_command("c", debugger)


def handle_command(command, debugger):
    print(f"(lldb) {command}")
    view_lldb(debugger)
    debugger.HandleCommand(command)
