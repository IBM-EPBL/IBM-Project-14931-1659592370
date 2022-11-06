# -- coding: utf-8 --
"""
Created on Sun Sep 25 16:53:16 2022
@author: VINO
"""

from flask import *

app = Flask(_name_)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/signin')
def sigin():
    return render_template('signin.html')

@app.route('/about')
def about():
    return render_template('about.html')