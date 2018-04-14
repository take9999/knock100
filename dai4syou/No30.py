import MeCab

#MeCab.Tagger()で解析方法を指定
#1行ずつ読み込んでparseで解析した結果を1行ずつ書き込む
def make_analyzed_file(input_txt,output_txt):
    _m = MeCab.Tagger()
    with open(input_txt, "r") as i_txt, open(output_txt, "w") as o_txt:
        o_txt.write(_m.parse(i_txt.read()))

make_analyzed_file("neko.txt","neko.txt.mecab")

def mapping_MeCab(mecab_file):
    with open(mecab_file,encoding="utf-8") as m_file:
        sentense = []
        sentenses = []

        for morpheme in m_file.read().split("\n"):
            #MeCabの形態素解析の結果

            surfase = morpheme.split("\t")

            #解析結果が出力されている行（タブがある）のみ処理対象
            if len(surfase) >= 2:
                #残りをカンマで区切る
                result = surfase[1].split(",")

                #結果をマッピングで格納
                word = {
                    "surface":surfase[0],
                    "base":result[6],
                    "pos":result[0],
                    "pos1":result[1]
                }
                #1文単位のリストに追加
                sentense.append(word)

                #句点か空白があったら終了
                if word["pos1"] == "句点":# or word["pos1"] == "空白":
                    sentenses.append(sentense)
                    #yield sentense
                    sentense = []
    return sentenses

m = mapping_MeCab("neko.txt.mecab")
