import json
from resource_model import Resource

n = 0
attr = None

with open('preset_resource.json', 'r',encoding="utf-8") as f:
  preset_resource = json.load(f)

for pr in preset_resource:
  attr = None
  n += 1
  Resource(sentence_id=n, sentence=json.dumps(preset_resource[n]), sentence_type=attr).save()

