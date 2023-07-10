import unittest
from re import Match

import commands
import re

man_dir: str = "/Users/xiayx/Documents/Projects/learn-lldb/docs/antora/modules/ROOT/pages/man"


# 继承 unittest.TestCase 创建测试类
def read_adoc() -> str:
    with open(f"{man_dir}/help.adoc", "r") as file:
        return file.read()


class TestCases(unittest.TestCase):

    # 每个测试方法以 "test_" 开头
    def test_re(self):
        content = read_adoc()
        print("is an abbreviation for" in content)
        matches = re.findall(r"^\s{2}(.*?)\s+--", content, re.MULTILINE)
        for match in matches:
            print(match.strip())


# 运行测试
if __name__ == '__main__':
    unittest.main()
