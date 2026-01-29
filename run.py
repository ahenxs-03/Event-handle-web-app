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

    