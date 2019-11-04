# zip(a,b)を使用し、a,bそれぞれの文字列を前から一つずつ取り出して処理
# 繰り返し回数は、a,bいずれか小さい方の文字数となる
str1 = "タクシー"
str2 = "パトカーあいう"

print("exp1")
joined_word = [x + y for x, y in zip(str1, str2)]
print(joined_word)

print("exp2")
z = ""
for x, y in zip(str1, str2):  # zipを使用すると、str1,str2のそれぞれを1文字ずつ繰り返しながらfor処理できる
    print(str(x + y))
    z += (x + y)
print(z)
