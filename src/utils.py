import json
import lexer
import boto3

from resource_model import Resource
from pynamodb.models import Model
from pynamodb.attributes import UnicodeAttribute, NumberAttribute, MapAttribute

dynamodb = boto3.resource('dynamodb', region_name = 'ap-northeast-1')
resources = dynamodb.Table('Resource')

def insert_resource_record(source_text, means, username):
  dt = datetime.datetime.now()
  ts = datetime.datetime.timestamp(dt)
  search_key = lexer.generate_search_key(source_text)
  res = resources.put_item(
    Item = {
      "sentence_id": ts,
      "search_key": search_key,
      "sentence_text": source_text,
      "created_with": means,
      "created_byr": username
    }
  )
  return (res)
