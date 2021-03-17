from flask import Flask, Response, request
from flask_cors import CORS

from flask_pymongo import PyMongo

import json
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

#dev
import json

app = Flask(__name__)
CORS(app)
# mongo URI for pymongo
# MONGO_URI = os.environ.get("MONGO_URI")
# app.config["MONGO_URI"] = MONGO_URI
# mongo = PyMongo(app)

# home route
@app.route('/')
def home():
    return "678345012"

if __name__ == '__main__':
    app.run()