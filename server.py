import json
import requests

from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/soccer/json', methods=['GET'])
def soccer():
    return json.dumps({"name": "Soccer", "top_players":['Messi','Ronaldo','Drogba']})

@app.route('/', methods=['POST'])
def post():
    body = request.get_json()
    print(body['hello'])
    return "POST ROUTE"
