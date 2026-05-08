# json for apis
# convert json into dict
import json 

data = {
    "name": "web1",
    "env": "prod"
}

json_data = json.dumps(data)
print(json_data)