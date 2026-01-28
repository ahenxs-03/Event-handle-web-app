#from app import app

from flask import render_template, url_for
from db import *
from flask import Blueprint
stu=Blueprint('student','__name__')
@stu.route('/student')
def admin():
    
    return render_template('student.html')