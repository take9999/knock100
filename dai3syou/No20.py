# jawiki-country.jsonは、textとtitleで構成されたjson
# titleには国名が入っている

import json


def extract_from_json(title):
    with open("jawiki-country.json", "r") as f:
        json_data = f.readline()
        while json_data:
            article_dict = json.loads(json_data)
            if article_dict["title"] == title:
                return article_dict["text"]
            else:
                json_data = f.readline()
    return ""  # 見つからなければ空白を返す


print(extract_from_json("イギリス"))