

#1行ずつ読み込んでparseで解析した結果を1行ずつ書き込む
def make_analyzed_file(input_txt,output_txt):
    _m = MeCab.Tagger()
    with open(input_txt, "r") as i_txt, open(output_txt, "w") as o_txt:
        o_txt.write(_m.parse(i_txt.read()))

make_analyzed_file("neko.txt","neko.txt.mecab")