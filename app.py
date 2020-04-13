import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from os import path
if path.exists("env.py"):
  import env 

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def home():
    return render_template('pages/home.html')

@app.route('/about')
def about():
    return render_template('pages/about.html', title='About')

@app.route('/projects')
def projects():
    return render_template('pages/projects.html', title='Projects')

@app.route('/contact')
def contact():
    return render_template('pages/contact.html', title='Contact')


if __name__ == '__main__':
    app.run(debug=True)