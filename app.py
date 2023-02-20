from flask import Flask, request
from db import add_image,add_like,add_dislike,get_data
app = Flask(__name__)

@app.route('/api/add-img/',methods=['POST'])
def home():
    if request.method == 'POST':
        data = request.get_json(force=True)
        photo_id = data['photo_id']
        chat_id = data('chat_id')

        if add_image(photo_id,chat_id):
            return {'status_id': 200}
        return {"status_id":400}   

@app.route('/api/likes',methods=['POST'])
def add_like():
    if request.method == 'POST':
        data = request.get_json(force=True)
        photo_id = data['photo_id']
        chat_id = data('chat_id')
        

        


        if add_like(photo_id,chat_id):
            return {'status_id': 200}
        return {"status_id":400}         

@app.route('/api/dislikes',methods=['POST'])
def dislike():
    if request.method == 'POST':
        data = request.get_json(force=True)
        photo_id = data['photo_id']
        chat_id = data('chat_id')

        if dislike(photo_id,chat_id):
            return {'status_id': 200}
        return {"status_id":400}         

