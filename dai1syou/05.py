#100本ノックNo.05

def n_gram(char, n, mode):
    """
    Args:
        char:対象の文字列
        n:Nの値
        mode:単語で区切るなら「word」, 文字で区切るなら「char」.デフォルトはword
    Return:
        n_gram:N-gramで分解した結果
    """
    n_gram = []
    # 単語　or 文字で区切る
    if (mode == "word"):
        chars = char.split()  # 単語で区切る
    if (mode == "char"):
        chars = char.replace(" ","") # 文字で区切る

    first_n = n
    while n - 1 < len(chars):
        n_gram.append(chars[n - first_n: n])
        n += 1

    return n_gram

# 問の回答
char = "I am an NLPer"
print("単語bi-gram")
words = n_gram(char, 2, "word")
print(words)

print("文字bi-gram")
chars = n_gram(char, 3, "char")
print(chars)


################
def n_gram(target, n):
    result = []
    for i in range(0, len(target) -n + 1):
        result.append(target[i:i+n])
    return result

l = "I am an NLPer"
words = l.split(" ")

# bi-gram
result = n_gram(words, 2)
print(result)

# tri-gram
result = n_gram(words, 3)
print(result)


