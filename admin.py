#from app import app
from flask import render_template, url_for, request, redirect
from db import *
from flask import Blueprint
adm=Blueprint('admin','__name__')



@adm.route('/admin')
def admin():
    event = Event.query.all()
    area = Area.query.all()
    about = User.query.filter_by(role_id=3).first()
    details = {
        "name": about.User_name,
        "password": about.user_password
    }
    Category = []
    for obj in area:
        di = {
            "area_id": obj.area_id,
            "area_name": obj.area_name

        }
        Category.append(di)

    return render_template('admin.html', event=event, details=details, category=Category)
# actions
# status control


@adm.route('/reject event/name')
def reject(name):
    ...
    return redirect(url_for('admin'))


@adm.route('/add/category', methods=['GET', 'POST'])
def add_category():
    if request.method == 'GET':
        return render_template('category.html')


@adm.route('/create', methods=['GET', 'POST'])
def create():
    name = request.form['Areaname']
    area = Area(area_name=name)
    database.session.add(area)
    database.session.commit()
    return redirect(url_for('admin'))


@adm.route('/delete/<int:id>', methods=['GET', 'POST'])
def delete_category(id):
    event = Area.query.get(id)
    database.session.delete(event)
    database.session.commit()
    return redirect(url_for('admin'))


#app.run(debug=True)
