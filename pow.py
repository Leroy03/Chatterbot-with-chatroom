import jieba
import jieba.posseg as pg
import jieba.analyse


def ana(text):
    jieba.set_dictionary("./dict.txt.big")  # 匯入違規字詞

    words = pg.cut(text)
    f = open("./dict.txt.big", "r")
    word = []

    content = f.readlines()
    for i in content:  # 讀入違規字詞
        t = i.split(' ')
        word.append(t[0])
    f.close()

    for x, w in words:  # x 為字典中的字詞， w 為相似度
        if x not in word:  # 如果該字詞不在裡面則自動新增
            f = open("./dict.txt.big", "a")
            fre = jieba.suggest_freq(x, True)
            f.writelines(x+" "+str(fre)+" "+w+"\n")
            f.close()
        print(x, w)

    jieba.enable_parallel(10)  # 平行運算加快速度
    jieba.analyse.set_stop_words("./stop_words.txt")
    jieba.analyse.TFIDF(idf_path=None)
    jieba.analyse.set_idf_path("./userdict.txt.big")

    # x 為字典中的字詞， w 為相似度
    for x, w in jieba.analyse.extract_tags(text, withWeight=True, topK=20):
        print(x, w)
        if w > 12:  # 如果相似度大於 12
            return True  # 回傳 True 踢出使用者

    return False
