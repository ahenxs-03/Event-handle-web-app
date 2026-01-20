

from app import app
from flask import render_template, url_for, request, redirect
from db import *


@app.route('/', methods=['GET', 'POST'])
def login():
    return render_template('home.html')


@app.route('/acc/create', methods=['GET', 'POST'])
def create_acc():
    return render_template('user.html')


app.run(debug=True)
