import sys
import os
import csv
import datetime

sys.path.append(os.path.abspath(".."))
import lexer

from resource_model import Resource

with open('preset_resource.csv', 'r') as f:
  reader = csv.reader(f)
  for line in reader:
    dt = datetime.datetime.now()
    ts = datetime.datetime.timestamp(dt)
    search_key = lexer.generate_search_key(line[2])
    print ("===== ", search_key)
    if (search_key != ''):
      Resource(
        sentence_id=ts,
        search_key=search_key,
        sentence_text=line[2],
        created_with=line[1],
        created_by=line[0]
        ).save()
