from dai3syou import No20
import re
import requests


def remove_markup(str):
    # 強調
    str = re.sub(r"'{2,5}", r"", str)
    # 内部リンク
    str = re.sub(r"\[{2}([^|\]]+?\|)*(.+?)\]{2}", r"\2", str)
    # 言語を指定した表記
    str = re.sub(r"\{{2}.+?\|.+?\|(.+?)\}{2}", r"\1 ", str)
    # コメント
    str = re.sub(r"<.*?>", r"", str)
    # 外部リンク
    str = re.sub(r"\[.*?\]", r"", str)
    return str


temp_dict = {}
lines = No20.extract_from_json(u"イギリス").split("\n")


def json_search(json_data):
    ret_dict = {}
    for k, v in json_data.items():
        if isinstance(v, list):
            for e in v:
                ret_dict.update(json_search(e))
        elif isinstance(v, dict):
            ret_dict.update(json_search(v))
        else:
            ret_dict[k] = v
    return ret_dict


for line in lines:
    category_line = re.search("^\|(.*?)\s=\s(.*)", line)
    if category_line is not None:
        temp_dict[category_line.group(1)] = remove_markup(category_line.group(2))

for k, v in sorted(temp_dict.items(), key=lambda x: x[0]):
    print(k, v)

url = "https://en.wikipedia.org/w/api.php"
payload = {"action": "query",
           "titles": "File:{}".format(temp_dict[u"国旗画像"]),
           "prop": "imageinfo",
           "format": "json",
           "iiprop": "url"}

print("requests:" + str(requests.get(url, params=payload).url))
json_data = requests.get(url, params=payload).json()
print(json_data)

print(json_search(json_data)["url"])
print(json_search(json_data))
