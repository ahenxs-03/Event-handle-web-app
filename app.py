# import secret
import os
from flask import Flask
from config import *
from home import log
from student import stu
from admin import adm
from host import hst
def create():
    app=Flask('__name__')
    app.config.from_object(Config)
    app.register_blueprint(log)
    app.register_blueprint(stu)
    app.register_blueprint(hst)
    app.register_blueprint(adm)
    return app
#app=create()

#print(app.config)



# from admin import *
# from home import *
