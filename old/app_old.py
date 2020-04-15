import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from os import path
if path.exists("env.py"):
  import env 

app = Flask(__name__)

MONGODB_URI = os.environ.get("MONGO_URI")
DBS_NAME = "skills_manager"
COLLECTION_NAME = "skills" 


mongo = PyMongo(app)

@app.route('/')
@app.route('/home')
def home():
    return render_template("home.html")


if __name__ == '__main__':
    app.run(debug=True)