#from app import app
from flask import render_template, url_for
from db import *
from flask import Blueprint
hst=Blueprint('host','__name__')

@hst.route('/host/<int:idi>')
def dashboard(idi):
    
    return render_template('host.html',idi=idi)