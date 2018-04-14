from dai4syou import No30
import collections
from matplotlib import pyplot as plt
#from matplotlib.font_manager import FontProperties
#fp = FontProperties(fname='/System/Library/Fonts/ヒラギノ角ゴシック W2.ttc')

m = No30.mapping_MeCab("neko.txt.mecab")

c = collections.Counter()

for morphemes in m:
    for morpheme in morphemes:
        c.update(morpheme["surface"])
#most_common(n)で上位n個表示する
print(c.most_common())


#No37
from matplotlib import pyplot as plt
from matplotlib.font_manager import FontProperties

fp = FontProperties(fname='/System/Library/Fonts/ヒラギノ角ゴシック W2.ttc')
#zip(*c)で、[("a",10),("i",5),("u",7)...]が[("a","i","u"...),(10,5,7...)]となる
dataset = list(zip(*c.most_common(10)))#top10のみ
print(dataset[0])
print(dataset[1])
plt.xticks(range(len(dataset[0])), dataset[0], fontproperties=fp)
plt.bar(range(len(dataset[0])), dataset[1], align='center')
plt.show()


# #No38
# plt.xlabel("出現頻度")
# plt.ylabel("単語の種類数")
# plt.grid(axis="y")
# #出現頻度0対策
# #plt.xlim(xmin=1,xmax=20)
# plt.hist(dataset[1],bins=30)
# plt.show()