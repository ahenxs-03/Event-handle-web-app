# import secret
import os
from flask import Flask
app = Flask('__name__')
app.config['SECERET_KEY'] = os.environ.get(
    'SECERET_KEY', 'a_temporary_dev_key')
# from admin import *
# from home import *
