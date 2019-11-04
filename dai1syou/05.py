def make_ngram(c, n, mode):
    n_gram = []
    chars = None
    if mode == "word":
        chars = c.split()  # 単語で区切る
    elif mode == "char":
        chars = c.replace(" ", "")  # 文字で区切る

    first_n = n
    while n - 1 < len(chars):
        n_gram.append(chars[n - first_n: n])
        n += 1

    return n_gram


char = "I am an NLPer"
print("単語bi-gram")
words = make_ngram(char, 2, "word")
print(words)

print("文字bi-gram")
bi_chars = make_ngram(char, 3, "char")
print(bi_chars)
