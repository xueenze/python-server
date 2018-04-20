import json

# JSON文件转对象
def transformJSON(path):
    with open(path, 'r') as f:
        return json.loads(f.read())
