import MeCab
from dai4syou import No30
import collections
from matplotlib import pyplot as plt
from matplotlib.font_manager import FontProperties
fp = FontProperties(fname='/System/Library/Fonts/ヒラギノ角ゴシック W2.ttc')

m = No30.mapping_MeCab("neko.txt.mecab")

nouns = []
noun = []
c = collections.Counter()

for morphemes in m:
    for morpheme in morphemes:
        c.update(morpheme["surface"])

#most_common(n)で上位n個表示する
print(c)

from matplotlib import pyplot as plt
from matplotlib.font_manager import FontProperties

nums = []
for x in c.values():
    nums.append(x)
#print(nums)

#No38
# plt.xlabel("x")
# plt.ylabel("y")
# plt.grid(axis="y")
# # #出現頻度0対策
# # plt.xlim(xmin=1,xmax=100)
# # plt.hist(nums,bins=20,range=(1,100))
# # #plt.show()


#No39
vals = []
for y in c.keys():
    vals.append(y)

plt.scatter(range(len(nums)), nums)
# 対数化
plt.xscale('log')
plt.yscale('log')
# 軸の範囲調整
plt.xlim(1, len(vals))
plt.ylim(1, nums[0])
# ラベルづけ
plt.xlabel('出現度順位', fontproperties=fp)
plt.ylabel('出現頻度', fontproperties=fp)
plt.show()