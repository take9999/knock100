#100本ノックNo.04

str="Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
str=str.replace(",","")
str=str.replace(".","")
list=str.split()#splitのデフォルトは空白区切
num_list=[1, 5, 6, 7, 8, 9, 15, 16, 19]#この番号の文字は頭文字をkeyにして辞書を作成、それ以外は頭2文字をkeyにして追加
dict={}#辞書初期化

#enumerateを使用すると便利
for (i,x) in enumerate(list,start=1):
    if i in num_list:
        dict[x[:1:]] = i
    else:
        dict[x[:2:]] = i
print(dict)
print(sorted(dict.items(),key=lambda x:x[1]))

#############
#オリジナル回答（enumerate使ってないのでちょっとダサい）
# for s in list:
#    i=list.index(s)#iは0から始まるので(i+1)が番号となる。
#    if (i+1) in num_list:
#        dict[s[:1]]=(i+1)
#    else:
#        dict[s[:2]]=(i+1)
# print(dict)
#############

first_w_list = [1, 5, 6, 7, 8, 9, 15, 16, 19]
target = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
results = {}

words = target.split(" ")

for (num, word) in enumerate(words, 1):
    if num in first_w_list:
        results[word[0:1]] = num
    else:
        results[word[0:2]] = num

print(results)