from dai3syou import No20
import re

lines = No20.extract_from_json("イギリス").split("\n")

for i, line in enumerate(lines):
    # ()でくくったところはgroupになる
    # (=+)は=が1個以上
    # \sは任意の空白文字
    # (.*?)は任意の文字列
    file_line = re.search("^(File|ファイル):(.*?)\|", line)
    if file_line is not None:
        print(str(i) + str(file_line.group(2)))
