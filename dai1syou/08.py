#100本ノックNo.08
#ordで文字をunicodeに変換、chrでunicodeを文字に変換

def cipher(str):
    enc=""
    if(str.isalpha() & str.islower()):
        for c in str:
            enc+=chr(219-ord(c))
        return(enc)
    else:
        return(str)

print(cipher("test"))
print(cipher(cipher("test")))
