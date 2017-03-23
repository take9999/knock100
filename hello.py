#100本ノックNo00-02

#zip(a,b)を使用することで、a,bそれぞれの文字列を前から一つずつ取り出して処理することができる。
#繰り返し回数は、a,bいずれか小さい方の文字数となる
str1="タクシー"
str2="パトカーあ"
joined_word=[x+y for x,y in zip(str1,str2)]
print(joined_word)


#スライスを使用して前から順番に2文字置きに文字を表示する
str = "パタトクカシーー"
print(str[::2])


#スライスを使用して逆順に文字を表示する
string = "stressed"
print(string[3::-1])
print(string[::-2])


#import numpy as np
#import matplotlib.pyplot as plt
#x = np.arange(-3, 3, 0.1)
#y = np.sin(x)
#plt.plot(x, y)


