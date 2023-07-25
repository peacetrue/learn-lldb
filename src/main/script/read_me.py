# lldb 脚本格式
# /Applications/Xcode.app/Contents/SharedFrameworks/LLDB.framework/Resources/Python/lldb/__init__.py
import lldb


# debugger = None
# target = None
# process = None
# thread = None
# frame = None


def __lldb_init_module(debugger: lldb.SBDebugger = lldb.debugger,
                       internal_dict: dict = None):
    """
    加载脚本后由 lldb 执行。
    :param debugger: LLDB 调试器对象，用于执行调试操作并访问调试器的各种功能和属性。
    :param internal_dict: LLDB 内部字典参数，用于存储调试器内部的状态或其他相关信息。
    """
    # print("debugger:", type(debugger), debugger)
    # print("internal_dict:", type(internal_dict))
    debugger.HandleCommand(f"command script add -o -f {__name__}.command_formatter _help")
    debugger.HandleCommand("_help help")


def command_formatter(debugger: lldb.SBDebugger = lldb.debugger,
                      command: str = None,
                      result: lldb.SBCommandReturnObject = lldb.SBCommandReturnObject(),
                      internal_dict: dict = None):
    """
    自定义命令格式。
    :param debugger: LLDB 调试器对象，用于执行调试操作并访问调试器的各种功能和属性。
    :param command: LLDB 命令参数，传递给调试器的特定命令以执行相应的操作或获取信息。
    :param result: LLDB 结果参数，调试器执行命令后返回的结果。结果可以是一个值、对象或状态信息。
    :param internal_dict: LLDB 内部字典参数，用于存储调试器内部的状态或其他相关信息。
    """
    print("debugger:", type(debugger), debugger)
    print("command:", type(command), command)
    print("result:", type(result), result)
    # print("internal_dict:", type(internal_dict), internal_dict)  # internal_dict 内容太多
    print("internal_dict:", type(internal_dict))

# 拷贝以下代码，创建命令
# def command_usage(debugger: lldb.SBDebugger, command: str, result: lldb.SBCommandReturnObject, internal_dict: dict):
