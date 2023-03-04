import json
from resource_model import Resource

from pynamodb.models import Model
from pynamodb.attributes import UnicodeAttribute, NumberAttribute, MapAttribute

resources = dynamodb.Table('Resource')

def generate_search_key(text):

def insert_resource_record(prompt, completion, username):
  dt = datetime.datetime.now()
  ts = datetime.datetime.timestamp(dt)
  res = trainings.put_item(
    Item = {
      "sentence_id": ts,
      "search_key": prompt,
      "completion": completion,
      "user": username
    }
  )
  return (res)
  sentence_id = UnicodeAttribute(hash_key=True)
  search_key = UnicodeAttribute(range_key=True)
  sentence_text = UnicodeAttribute()
  created_with = UnicodeAttribute()
  created_by = UnicodeAttribute()