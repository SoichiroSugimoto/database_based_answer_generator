import MeCab

NOUN = "名詞-普通名詞-一般"

def lexer(text):
  tagger = MeCab.Tagger()
  lexer_result = tagger.parse(text)
  word_array = lexer_result.splitlines()
  lexer_array = []
  for a in word_array:
    lexer_array.append(a.split('\t'))
  return (lexer_array)

def get_noun(text):
  lexer_array = lexer(text)
  noun_array = []
  for la in lexer_array:
    if (la[0] != "EOS" and la[4] == NOUN):
      noun_array.append(la[0])
  return (noun_array)

def generate_search_key(text):
  search_key = ''
  noun_array = get_noun(text)
  for word in noun_array:
    if (search_key != ''):
      search_key += '_'
    search_key += word
  return (search_key)

