from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash
from flask import session
from flask import Blueprint
from flask_login import LoginManager, logout_user, login_user, login_required

#from app import create
from flask import render_template, url_for, request, redirect, flash
from db import Role, User, Host, Student

#app=create()
# login maneger create
manager = LoginManager()
log=Blueprint('log','__name__')
manager.view='login'
@manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@log.route('/', methods=['GET', 'POST'])
def login():
    
    if request.method == "GET":
        print('get response')
        print(session)
        return render_template('home.html')
    if request.method == 'POST':
        print("post")
        print(session)
        
        #flash('Wrong')
        name = request.form["name"]
        password = request.form["passw"]
        info = User.query.filter_by(User_name=name).all()
        print("check play load")
        print(session)
        if info == []:
            flash('Wrong')
            return render_template('home.html')
        else:
            l = []
            check = {
                "name": name,
                "pass_hash": password
            }
            for i in info:
                if name == i.User_name and check_password_hash(i.user_password, password):
                    login_user(i)
                    print("created login user")
                    print(session)
                
                    
                    
                    if Role.query.get(i.role_id).role_name=='admin':
                        print("before redirect")
                        print(session)
                        session.permanent=True
                        return  redirect(url_for('admin.admin'))
                    elif Role.query.get(i.role_id).role_name=='host':
                        return  redirect(url_for('host.dashboard',idi=i.user_id))
                    elif Role.query.get(i.role_id).role_name=='student':
                        return  redirect(url_for('student.student_dash',idi=i.user_id))



            flash("invalid cardinals")
            return render_template('home.html')
    
@login_required
@log.route('/log/out')
def logout():
    logout_user()
    session.clear()
    print(session)
    return redirect(url_for('log.login'))
@log.route('/acc/create', methods=['GET', 'POST'])
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
    return 'exist'

#app.run(debug=True)
