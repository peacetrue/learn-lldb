# 解析文档的 python 脚本测试
import re
import unittest

man_dir: str = "../../../docs/antora/modules/ROOT/pages/man"


# 继承 unittest.TestCase 创建测试类
def read_adoc() -> str:
    with open(f"{man_dir}/breakpoint.adoc", "r") as file:
        return file.read()


class TestCases(unittest.TestCase):

    # 每个测试方法以 "test_" 开头
    def test_subcommand(self):
        # 从命令的帮助信息中提取子命令信息
        content = read_adoc()
        matches = re.findall(r"^\s+(\w+)\s+--", content, re.MULTILINE)
        for match in matches:
            print(match.strip())

    def test_resolve_filename(self):
        # 解析文件名：
        # 期待：type-synthetic-add.adoc -> type-synthetic-add -> ['type', 'synthetic', 'add']
        # 实际：type-synthetic-add.adoc -> type-synthetic- -> ['type', 'synthetic', '']
        file_name = "type-synthetic-add.adoc"
        simple_file_name = file_name.rstrip(".adoc")  # rstrip 此函数似乎对 . 有什么特殊逻辑
        commands = simple_file_name.split("-")
        print(f'{file_name} -> {simple_file_name} -> {commands}')


# 运行测试
if __name__ == '__main__':
    unittest.main()
