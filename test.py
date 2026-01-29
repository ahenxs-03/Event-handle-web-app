# from db import *
from app import create
from flask import session
import os
app=create()
#app.config['SECERET_KEY'] = "abc"
# with app.app_context():
#   for i in range(3, 9):
#      stu = User.query.get(i)
#   database.session.delete(stu)
#     database.session.commit()
# stu = Student.query.get(1)
# database.session.delete(stu)
# database.session.commit()
#print(app.'SECRET_KEY')
#print(id(app))
print (session)
