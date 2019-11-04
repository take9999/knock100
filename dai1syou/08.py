def cipher(s):
    enc = ""
    if str.isalpha and str.islower:
        for c in s:
            enc += chr(219 - ord(c))
        return enc
    else:
        return s


print(cipher("test"))
print(cipher(cipher("test")))
