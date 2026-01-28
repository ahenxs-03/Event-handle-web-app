#from app import app
from flask import render_template, url_for
from db import *
from flask import Blueprint
hst=Blueprint('host','__name__')

@hst.route('/host')
def admin():
    
    return render_template('host.html')