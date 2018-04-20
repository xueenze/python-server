import utils
import json
from flask import Flask

# 创建APP
app = Flask(__name__)

@app.route('/')
def index():
    data = utils.transformJSON('mock/index.json')
    return json.dumps(data, ensure_ascii=False)
if __name__ == '__main__':
    app.run(debug=True)
