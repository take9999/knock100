str1 = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
str1 = str1.replace(",", "")
str1 = str1.replace(".", "")
list1 = []
for i in str1.split():  # splitのデフォルトは空白区切のようです。
    list1.append(len(i))
print(list1)

str2 = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
# str2=str2.translate(None,".,")
str2 = str2.replace(",", "")
str2 = str2.replace(".", "")
str2 = str2.split()
num_char = [len(x) for x in str2]
print(str2)
print(num_char)
