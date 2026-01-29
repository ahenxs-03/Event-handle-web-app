from app import create
app=create()
from db import *
from home import sessions
#with app.app_context:
database.init_app(app)
app.run(debug=True)

    