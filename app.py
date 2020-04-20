import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from os import path
if path.exists("env.py"):
    import env 

app = Flask(__name__)    
# Configuration values for flask_pymongo  
# Documentation at http://flask-pymongo.readthedocs.io/en/latest/#configuration app.config['MONGO_DBNAME'] = 'skills_manager'  
app.config['MONGO_URI'] = os.environ.get('MONGO_URI')
mongo = PyMongo(app)


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html', title='About', skills=mongo.db.skills.find())

@app.route('/projects')
def projects():
    return render_template('projects.html', title='Projects')

@app.route('/contact')
def contact():
    return render_template('contact.html', title='Contact')

@app.route('/admin')
def admin():
    return render_template('admin.html', title='Admin', skills=mongo.db.skills.find())

@app.route('/insert_skill', methods=['POST'])
def insert_skill():
    skills = mongo.db.skills
    skills.insert_one(request.form.to_dict())
    return redirect(url_for('admin'))


if __name__ == '__main__':
    app.run(host=os.getenv('IP', '0.0.0.0'), 
    port=int(os.getenv('PORT', 8080)), 
    debug=True)
