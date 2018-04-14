import MeCab
from dai4syou import No30

m = No30.mapping_MeCab("neko.txt.mecab")

result = []

for words in m:
    for word in words:
        #if word["pos"] == "動詞":
            #print(word["surface"])
            #print(word["base"])
        if word["pos"] == "名詞" and word["pos1"] == "サ変接続":
            result.append(word["surface"])

print(result)