from app import create
app=create()
from db import *
from config import *
from flask import session

from home import manager
from home import log
from student import stu
from admin import adm
from host import hst
app.config.from_object(Config)
manager.init_app(app)


app.register_blueprint(log)
app.register_blueprint(stu)
app.register_blueprint(hst)
app.register_blueprint(adm)
#with app.app_context:
database.init_app(app)
if __name__=='__main__':
    #print(session)
    app.run(debug=True)
    
#print(app.config)

#with app.app_context():
   # student_role = Role(role_name="student")
    #host_role = Role(role_name="host")
    #admin_role = Role(role_name="admin")

    #admin = User(User_email_id="admin123xyz@asso.co.in", User_name="User_Admin",
     #            user_password=generate_password_hash("1234"), role_id=3)

    #database.session.add_all([student_role, host_role, admin_role, admin])
    #database.session.commit()

 #   database.drop_all()
  #  database.create_all()
    #     add admin
     
     
    # database.session.commit()
    # database.create_all()
    # database.session.commit()

    