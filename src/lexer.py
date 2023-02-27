import MeCab

NOUN = "名詞-普通名詞-一般"

def lexer(prompt):
  tagger = MeCab.Tagger()
  lexer_result = tagger.parse(text)
  word_array = lexer_result.splitlines()
  lexer_array = []
  for a in word_array:
    lexer_array.append(a.split('\t'))
  return (lexer_array)

def get_noun(prompt):
	lexer_array = lexer(prompt)
	noun_array = []
	for la in lexer_array:
		if (la[0] != "EOS" and la[4] == NOUN):
			noun_array.append(la[0])
	print(noun_array)
