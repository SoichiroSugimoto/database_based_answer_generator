import json
from .. import utils
from resource_model import Resource

with open('preset_resource.csv', 'r') as f:
  reader = csv.reader(f)
  for line in reader:
    utils.insert_resource_record(line[2], line[1], line[0])
