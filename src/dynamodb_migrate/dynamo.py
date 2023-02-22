import json
from resource_model import Resource

if not Resource.exists():
  Resource.create_table(read_capacity_units=1,
                    write_capacity_units=1, wait=True)

print('Done!')
