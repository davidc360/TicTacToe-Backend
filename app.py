from flask import Flask, Response, request, jsonify
from flask_cors import CORS

from flask_pymongo import PyMongo

import json
import uuid
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

#dev
import json

app = Flask(__name__)
CORS(app)
# mongo URI for pymongo
MONGO_URI = os.environ.get("MONGO_URI")
app.config["MONGO_URI"] = MONGO_URI
mongo = PyMongo(app)
gamesdb = mongo.db.games

# home route
@app.route('/')
def home():
    return "678345012"

@app.route('/game', methods=['POST'])
def post_game():
    game_id = str(uuid.uuid4())[:8]
    while gamesdb.find_one({'id': game_id}) is not None:
        game_id = str(uuid.uuid4())[:8]
    params = request.get_json()
    doc = {
        "id": game_id,
        "m": params.get('moves')
    }
    name = params.get('name')
    if name is not None and length(name) > 0:
        doc["n"] = params.get('name')
    gamesdb.insert_one(doc)
    return jsonify(game_id)

GAME_KEY_NAMES = {
    "m": "moves",
    "n": "name"
}    
@app.route('/game/<game_id>', methods=['GET', 'DELETE'])
def return_game(game_id=None):
    if request.method == 'GET':
        game = gamesdb.find_one({"id": game_id})
        if game is None:
            return Response(status=404)
        # formate dictionary names
        for key, value in GAME_KEY_NAMES.items():
            game[value] =  game.pop(key, None)
        return json.dumps(game, default=str)

if __name__ == '__main__':
    app.run()