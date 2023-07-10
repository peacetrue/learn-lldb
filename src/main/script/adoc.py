#  https://docs.python.org/3.13/library/index.html
import lldb
import re
import logging
import os

# 基于 Makefile 的目录
man_dir: str = "../../docs/antora/modules/ROOT/pages/man"
suffix: str = ".adoc"

if not os.path.exists(man_dir):
    # 自动创建 man_dir 目录
    os.makedirs(man_dir)

# 配置日志输出格式
logging.basicConfig(
    level=logging.INFO,  # 设置日志级别为INFO，即只记录INFO级别及以上的日志
    format="[%(levelname)s] %(message)s",  # 日志格式
    handlers=[
        logging.FileHandler("man.log"),  # 将日志写入文件
        logging.StreamHandler()  # 在控制台输出日志
    ]
)


def __lldb_init_module(debugger, internal_dict):
    # lldb 初始执行
    save_command_help(debugger.GetCommandInterpreter())
    generate_nav_man()


def save_command_help(interpreter, command="help"):
    # 保存命令帮助信息
    logging.info(f"save_command_help: {command}")
    content = handle_return_command(interpreter, command)
    logging.debug(f"man content: \n{content}")
    # 忽略简写的命令
    # if f"'{command.lstrip('help').strip()}' is an abbreviation for" in content:
    #     return
    save(command, content)
    sub_commands = resolve_command_content(command, content)
    # 删除 help help 否则 help help 的内容覆盖 help
    sub_commands = [item for item in sub_commands if command == "help"]
    logging.info(f"sub_commands: {sub_commands}")
    for sub_command in sub_commands:
        save_command_help(interpreter, f"{command} {sub_command}")


def resolve_command_content(command, content) -> list[str]:
    # 解析子命令
    matches = re.findall(r"^\s+(\w+)\s+--", content, re.MULTILINE)
    return [match.strip() for match in matches]


def save(command, content):
    # 保存命令帮助信息
    command = command.strip().split()
    # 如果不是 help 命令，则移除前缀 help
    if len(command) > 1:
        command = command[1:]
    name = '-'.join(command)
    content = f"= {name}\n\n----\n{content}\n----"
    with open(f"{man_dir}/{name}{suffix}", "w") as file:
        file.write(content)


def handle_return_command(interpreter, command) -> str:
    # 执行命令并返回
    result = lldb.SBCommandReturnObject()
    interpreter.HandleCommand(command, result)
    return result.GetOutput().rstrip("\n")


def generate_nav_man():
    # 生成导航中的 man 部分
    navs: list[str] = ["* https://lldb.llvm.org/man/lldb.html[man 手册^]"]
    file_list = os.listdir(man_dir)
    file_list = sorted(file_list, key=lambda x: x.split('.')[0])
    for file_name in file_list:
        commands = file_name.split(".")[0].split("-")
        navs.append(f"*{'*' * len(commands)} xref:man/{file_name}[{commands[-1]}]")
    with open(f"{man_dir}/../../partials/nav-man.adoc", "w") as file:
        file.write("\n".join(navs))
