#100本ノックNo00-02

print("No2")
#zip(a,b)を使用することで、a,bそれぞれの文字列を前から一つずつ取り出して処理することができる。
#繰り返し回数は、a,bいずれか小さい方の文字数となる
str1="タクシー"
str2="パトカーあ"
joined_word=[x+y for x,y in zip(str1,str2)]
print(joined_word)

z=""
for x,y in zip(str1,str2):#zipを使用すると、str1,str2のそれぞれを1文字ずつ繰り返しながらfor処理できる
    print(str(x+y))
    z += (x+y)
print(z)


print("No1")
#スライスを使用して前から順番に2文字置きに文字を表示する
str = "パタトクカシーー"
print(str[::2])


print("No0")
#スライスを使用して逆順に文字を表示する
string = "stressed"
print(string[3::-1])
print(string[::-2])


#import numpy as np
#import matplotlib.pyplot as plt
#x = np.arange(-3, 3, 0.1)
#y = np.sin(x)
#plt.plot(x, y)


