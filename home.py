from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash
from flask import session
from flask_login import LoginManager, logout_user, login_user

from app import app
from flask import render_template, url_for, request, redirect, flash
from db import *

app.config['secret_key'] = "i DONT KNOW!"
# login maneger create
manager = LoginManager(app)


@manager.user_loader
def load_user(user_id):
    User.query.get(int(user_id))


@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == "GET":
        return render_template('home.html')
    else:
        name = request.form["name"]
        password = request.form["passw"]
        info = User.query.filter_by(User_name=name).all()
        if info == []:
            flash('Wrong')
        else:
            l = []
            check = {
                "name": name,
                "pass_hash": password
            }
            for i in info:
                if name == i.User_name and check_password_hash(i.user_password, password):
                    login_user(i)
                    return ('Welcome')

            flash("invalid cardinals")
            return render_template('home.html')


@app.route('/acc/create', methods=['GET', 'POST'])
def create_acc():
    if request.method == "GET":
        return render_template('user.html')
    elif request.method == "POST":
        email = request.form["email"]
        name = request.form["name"]
        pass_hash = generate_password_hash(request.form["pass"])
        use = request.form["Type"]
        # get userid
        idi = Role.query.filter_by(role_name=use).first()
        id_new = idi.role_id

        # construct new User
        user = User(User_email_id=email, User_name=name,
                    user_password=pass_hash, role_id=id_new)
        try:
            database.session.add(user)
            database.session.commit()
            stu = user.user_id
            if id_new == 1:
                candidate = Student(User_id=stu)
                database.session.add(candidate)
                database.session.commit()
            elif id_new == 2:
                candidate = Host(User_id=stu)
                database.session.add(candidate)
                database.session.commit()
        except:
            flash("already exist")

            # prevent if already exist


app.run(debug=True)
