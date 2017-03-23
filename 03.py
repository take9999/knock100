#100本ノックNo.03

str1="Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
str1=str1.replace(",","")
str1=str1.replace(".","")
list1=[]
for i in str1.split():#splitのデフォルトは空白区切のようです。
    list1.append(len(i))
print(list1)


#str = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
#str = str.replace('.', "")
#str = str.replace(',', "")
#str = str.split()
#
# list = []
#
# for word in str:
#     list.append(len(word))
#
# print(list)