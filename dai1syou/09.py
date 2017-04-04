#100本ノックNo.09
import random

str="こんちには みさなん おんげき ですか？ わしたは げんき です。 この ぶんょしう は いりぎす の ケブンッリジ だがいく の けゅきんう の けっか にんんげ は もじ を にしんき する とき その さしいょ と さいご の もさじえ あいてっれば じばんゅん は めくちちゃゃ でも ちんゃと よめる という けゅきんう に もづいとて わざと もじの じんばゅん を いかれえて あまりす。 どでうす？　ちんゃと よゃちめう でしょ？ ちんゃと よためら はのんう よしろく"

l=str.split(" ")
print(l)
output=""

for s in l:
    if len(s) > 4:
        list_s=list(s)
        #print(s)

        first_s=list_s.pop(0)
        #print(last_s)

        last_s=list_s.pop(len(list_s)-1)
        #print(last_s)

        output+=first_s

        for i in range(len(list_s)):
            output+=list_s.pop(random.randint(0,len(list_s)-1))

        output+=last_s

    else:
        output+=s

    output+=" "

print(output)


##############################
# import random
#
# def typoglycemia(sentence):
#     '''
#     param : 対象の文字列
#     return : 変換した文字列
#     '''
#     result = []
#     for word in sentence.split(' '):
#         if len(word) <= 3:
#             result.append(word)
#         else:
#             w_list = list(word[1:-1])
#             random.shuffle(w_list)
#             result.append(word[0] + ''.join(w_list) + word[-1])
#
#     return ' '.join(result)
#
# target = input('文字列を入力してください。\n')
#
# result = typoglycemia(target)
# print('変換結果\n' + result)