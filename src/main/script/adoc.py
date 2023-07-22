#  https://docs.python.org/3.13/library/index.html
import lldb
import re
import logging
import os

# 基于 Makefile 的目录
base_dir: str = "../../docs/antora/modules/ROOT/pages"
man_dir: str = f"{base_dir}/man"
key_dir: str = f"{base_dir}/key"
suffix: str = ".adoc"

# 自动创建目录
if not os.path.exists(man_dir):
    os.makedirs(man_dir)
if not os.path.exists(key_dir):
    os.makedirs(key_dir)

# 配置日志输出格式
logging.basicConfig(
    level=logging.INFO,  # 设置日志级别为INFO，即只记录INFO级别及以上的日志
    format="[%(levelname)s] %(message)s",  # 日志格式
    handlers=[
        logging.FileHandler("adoc.log"),  # 将日志写入文件
        logging.StreamHandler()  # 在控制台输出日志
    ]
)


def __lldb_init_module(debugger, internal_dict):
    # lldb 初始执行
    # save_command_help(debugger.GetCommandInterpreter())
    # generate_nav_man()
    save_command_key(debugger.GetCommandInterpreter(), ["settings list", "log list"])
    generate_nav_key()


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


def save(command, content, cmd_dir=man_dir):
    # 保存命令帮助信息
    command = command.strip()
    parts = command.split()
    # 如果不是 help 命令，则移除前缀 help
    if command != "help" and parts[0] == "help":
        parts = parts[1:]
    name = '-'.join(parts)
    content = f"= {name}\n\n----\n{content}\n----"
    with open(f"{cmd_dir}/{name}{suffix}", "w") as file:
        file.write(content)


def handle_return_command(interpreter, command) -> str:
    # 执行命令并返回
    result = lldb.SBCommandReturnObject()
    interpreter.HandleCommand(command, result)
    return result.GetOutput().rstrip("\n")


def generate_nav_man():
    # 生成导航中的 man 部分
    navs: list[str] = ["* https://lldb.llvm.org/man/lldb.html[帮助手册^]"]
    file_list = os.listdir(man_dir)
    file_list = sorted(file_list, key=lambda x: x.split('.')[0])
    for file_name in file_list:
        commands = file_name.split(".")[0].split("-")
        navs.append(f"*{'*' * len(commands)} xref:man/{file_name}[{commands[-1]}]")
    with open(f"{man_dir}/../../partials/nav-man.adoc", "w") as file:
        file.write("\n".join(navs))


def save_command_key(interpreter, commands: list[str]):
    # 保存命令关键信息
    logging.info(f"save_command_key: {len(commands)}")
    for command in commands:
        key = handle_return_command(interpreter, command)
        logging.debug(f"command key: \n{key}")
        save(command, key, key_dir)


def generate_nav_key(this_dir=key_dir):
    # 生成导航中的 key 部分
    navs: list[str] = ["* 帮助选项"]
    file_list = os.listdir(this_dir)
    file_list = sorted(file_list, key=lambda x: x.split('.')[0])
    for file_name in file_list:
        commands = file_name.split(".")[0]
        navs.append(f"** xref:key/{file_name}[{commands}]")
    with open(f"{this_dir}/../../partials/nav-key.adoc", "w") as file:
        file.write("\n".join(navs))
