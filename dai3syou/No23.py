from dai3syou import No20
import re

lines = No20.extract_from_json("イギリス").split("\n")

for line in lines:
    # ()でくくったところはgroupになる
    # (=+)は=が1個以上
    # \sは任意の空白文字
    # (.*?)は任意の文字列
    section_line = re.search("^(=+)\s*(.*?)\s*(=+)$", line)
    if section_line is not None:
        print(section_line.group(2), len(section_line.group(1)) - 1)
