#100本ノックNo.06

str1="paraparaparadise"
str2="paragraph"

X=set([])
Y=set([])

for i in range(len(str1)-1):
    X.add(str1[i:i+2])

for j in range(len(str2)-1):
    Y.add(str2[j:j+2])

print(X)
print(Y)

print("和集合"+str(X|Y))
print("差集合"+str(X-Y))
print("積集合"+str(X&Y))

if "se" in X:
    print("seはXに含まれる")


if "se" in Y:
    print("seはYに含まれる")