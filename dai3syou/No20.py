#jawiki-country.jsonは、textとtitleで構成されたjson
#titleには国名が入っている

import json

# with open("jawiki-country.json","r") as f:
#     article_json = f.readline()
#     while article_json:
#         article_dict = json.loads(article_json)
#         if article_dict["title"] == u"イギリス":
#             print(article_dict["title"])
#         article_json = f.readline()

def extract_from_json(title):
    with open("jawiki-country.json","r") as f:
        json_data = f.readline()
        while json_data:
            article_dict = json.loads(json_data)
            if article_dict["title"] == title:
                return article_dict["text"]
            else:
                json_data = f.readline()
    return ""#見つからなければ空白を返す

