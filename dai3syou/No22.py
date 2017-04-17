from dai3syou import No20
import re

lines = No20.extract_from_json(u"イギリス").split("\n")

for line in lines:
    #()でくくったところはgroupになる
    #.*?は、任意の文字列と最短一致
    category_line = re.search("^\[\[Category:(.*?)(|\|.*)\]\]$",line)
    if category_line is not None:
        print(category_line.group(1))
        print(category_line.group(2))
