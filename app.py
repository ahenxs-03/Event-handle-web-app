# import secret
import os
from flask import Flask
from config import *
def create():
    app=Flask('__name__')
    app.config.from_object(Config)
# from admin import *
# from home import *
