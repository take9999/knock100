# 100本ノックNo.09
import random

str = "こんちには みさなん おんげき ですか？ わしたは げんき です。 " \
      "この ぶんょしう は いりぎす の ケブンッリジ だがいく の " \
      "けゅきんう の けっか にんんげ は もじ を にしんき する とき " \
      "その さしいょ と さいご の もさじえ あいてっれば じばんゅん は " \
      "めくちちゃゃ でも ちんゃと よめる という けゅきんう に もづいとて " \
      "わざと もじの じんばゅん を いかれえて あまりす。 どでうす？　" \
      "ちんゃと よゃちめう でしょ？ ちんゃと よためら はのんう よしろく"

str_list = str.split(" ")
print(str_list)
output = ""

for s in str_list:
    if len(s) > 4:
        list_s = list(s)
        first_s = list_s.pop(0)
        last_s = list_s.pop(len(list_s) - 1)
        output += first_s
        for i in range(len(list_s)):
            output += list_s.pop(random.randint(0, len(list_s) - 1))
        output += last_s
    else:
        output += s
    output += " "
print(output)
