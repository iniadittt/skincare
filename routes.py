from main import app
from flask import render_template, jsonify, request
from http import HTTPStatus
from recommendation import recommend
from load_model import load_data
import re

df = load_data('./static/models/list_products.pkl')
similarity = load_data('./static/models/similarity_products.pkl')

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])
def recommend_skincare():
    try:
        skin_type = request.form['skin_type']
        print(skin_type)
        results = recommend(skin_type.lower(), df, similarity, top=10)
        print(results)
        result = [{"name": res["name"].rstrip(), "type": res["type"]} if res["name"][-1] == " " else {"name": res["name"], "type": res["type"]} for res in results]
        result = [{"name": re.sub(r'/', '', x["name"]), "type": x["type"]} for x in result]
        return jsonify({
            'code': HTTPStatus.OK,
            'message': 'Success predicting',
            'data': result
        }), HTTPStatus.OK
    except Exception as error:
        return jsonify({
            'code': HTTPStatus.BAD_REQUEST,
            'message': str(error)
        }), HTTPStatus.BAD_REQUEST
        