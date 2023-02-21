import MeCab
text = "静かなる鏡のごとき湖が眠れるアリチアの森"

tagger = MeCab.Tagger()
print(tagger.parse(text))
