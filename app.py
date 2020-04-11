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
COLLECTION_NAME = "skills_manager"

mongo = PyMongo(app)

@app.route('/')
@app.route('/get_skill')
def get_skill():
    return render_template("skill.html", skill=mongo.db.skill.find())


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)