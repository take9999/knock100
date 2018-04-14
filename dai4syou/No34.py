import MeCab
from dai4syou import No30
import ngram

m = No30.mapping_MeCab("neko.txt.mecab")
index = ngram.NGram(N=3)

w_list = []
for morpheme in m:
    for three_words in index.ngrams(morpheme):
        if three_words[0]["pos"] == "名詞" and three_words[1]["surface"] == "の" and three_words[2]["pos"] == "名詞":
            w_list.append([three_words[0]["surface"],three_words[1]["surface"],three_words[2]["surface"]])

print(w_list)