import os
import json
import csv
import boto3
import MeCab

dynamodb = boto3.resource('dynamodb', region_name = 'ap-northeast-1')
resources = dynamodb.Table('Resource')

def lambda_handler(event, context):
  text = "静かなる鏡のごとき湖が眠れるアリチアの森"
  tagger = MeCab.Tagger()
  lexer_result = tagger.parse(text)
  word_array = lexer_result.splitlines()
  lexer_array = []
  for a in word_array:
    lexer_array.append(a.split('\t'))
  print(lexer_array[2][4])
