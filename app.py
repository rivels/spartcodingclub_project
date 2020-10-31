from pymongo import MongoClient

from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

client = MongoClient('localhost', 27017)
db = client.project


# HTML 화면 보여주기
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/list', methods=['GET'])
def show_playlist():
    M_playlist = list(db.melon_spring.find({}, {'_id': False}))
    G_playlist = list(db.genie_spring.find({}, {'_id': False}))
    B_playlist = list(db.bugs_spring.find({}, {'_id': False}))
    # 2. 성공하면 success 메시지와 함께 stars_list 목록을 클라이언트에 전달합니다.
    return jsonify({'result': 'success','M_playlist':M_playlist, 'G_playlist':G_playlist, 'B_playlist':B_playlist})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)