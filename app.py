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
COLLECTION_NAME = os.environ.get("COLLECTION_NAME")

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html', title='About')

@app.route('/projects')
def projects():
    return render_template('projects.html', title='Projects')

@app.route('/contact')
def contact():
    return render_template('contact.html', title='Contact')

@app.route('/admin')
def admin():
    return render_template('admin.html', title='Admin')


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=(os.environ.get('DEBUG'))