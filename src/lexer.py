import MeCab

def lexer(prompt):
  tagger = MeCab.Tagger()
  lexer_result = tagger.parse(text)
  word_array = lexer_result.splitlines()
  lexer_array = []
  for a in word_array:
    lexer_array.append(a.split('\t'))
  return (lexer_array)