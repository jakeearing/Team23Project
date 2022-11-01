import os
from flask import Flask
from flask import render_template
from flask import request
from flask import redirect, url_for

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')