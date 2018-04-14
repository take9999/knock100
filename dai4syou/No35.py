import MeCab
from dai4syou import No30
from collections import Counter

m = No30.mapping_MeCab("neko.txt.mecab")

nouns = []
noun = []
c = Counter()

for morphemes in m:
    for morpheme in morphemes:
        c.update(morpheme["surface"])

print(c)