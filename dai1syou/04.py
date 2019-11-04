# 100本ノックNo.04

target_str = "Hi He Lied Because Boron Could Not Oxidize Fluorine. " \
             "New Nations Might Also Sign Peace Security Clause. Arthur King Can."
target_str = target_str.replace(",", "")
target_str = target_str.replace(".", "")
str_list = target_str.split()  # splitのデフォルトは空白区切
num_list = [1, 5, 6, 7, 8, 9, 15, 16, 19]  # この番号の文字は頭文字をkeyにして辞書を作成、それ以外は頭2文字をkeyにして追加
str_dict = {}  # 辞書初期化

# enumerateを使用すると便利
for (i, s) in enumerate(str_list, start=1):
    if i in num_list:
        str_dict[s[:1:]] = i
    else:
        str_dict[s[:2:]] = i
print(str_dict)
print(sorted(str_dict.items(), key=lambda x: x[1]))
