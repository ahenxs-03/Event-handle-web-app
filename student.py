from app import app
from flask import render_template, url_for
from db import *
@app.route('/student')
def admin():
    
    return render_template('student.html')