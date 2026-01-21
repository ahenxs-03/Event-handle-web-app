from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash

from app import app
from flask import render_template, url_for, request, redirect, flash
from db import *


@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method=="GET":
        return render_template('home.html')
    else:
        name=request.form["name"]
        password=request.form["passw"]
        info=User.query.filter_by(User_name=name).all()
        if info==[]:
            return render_template('home.html',drawback="not found try again")
        else:
            l=[]
            check={
                "name":name,
                "pass_hash":password
            }
            for i in info:
                if name==i.User_name and check_password_hash(i.user_password,password):
                    return('Welcome')
            
            else:
                return render_template('home.html',drawback="no match found")
                


@app.route('/acc/create', methods=['GET', 'POST'])
def create_acc():
    if request.method=="GET":
        return render_template('user.html')
    elif request.method=="POST":
        name=request.form["name"]
        pass_hash=generate_password_hash(request.form["pass"])
        use=request.form["Type"]
        #get userid
        idi=Role.query.filter_by(role_name=use).first()
        id_new=idi.role_id

        #construct new User
        user=User(User_name=name,user_password=pass_hash,role_id=id_new)
        database.session.add(user)
        database.session.commit()
        #prevent if already exist



app.run(debug=True)
