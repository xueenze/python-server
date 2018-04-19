import json
from flask import Flask

# 创建APP
app = Flask(__name__)

@app.route('/')
def index():
    data = {
        'code': 0,
        'data': [{
            'id': 1,
            'imageUrl': '/images/card/1.jpg',
            'title': '【微信跳一跳】浅析（上）',
            'subTitle': '微信小游戏',
            'addDate': '2017-12-30',
            'redirctUrl': '/pages/detail/analysis/smallgame1/smallgame1'
            }]
    }
    return json.dumps(data, ensure_ascii=False)

if __name__ == '__main__':
    app.run(debug=True)
