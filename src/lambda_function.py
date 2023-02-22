import os
import json
# import boto3
import MeCab

def lambda_handler(event, context):
  text = "静かなる鏡のごとき湖が眠れるアリチアの森"
  tagger = MeCab.Tagger()
  print(tagger.parse(text))