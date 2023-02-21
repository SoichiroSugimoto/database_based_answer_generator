import os
import json
import boto3
import MeCab
text = "静かなる鏡のごとき湖が眠れるアリチアの森"

def lambda_handler(event, context):
	tagger = MeCab.Tagger()
	print(tagger.parse(text))