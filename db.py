from flask_sqlalchemy import SQLAlchemy
from app import app
app.config['SQLALCHEMY_DATABASE_URI']="sqlite:///mydatabase.db"

database=SQLAlchemy(app)

class Role(database.Model):
    __tablename__='Role'
    role_id = database.Column( database.Integer, primary_key=True )
    role_name = database.Column( database.String, unique=True )
    users = database.Relationship( 'User', lazy='dynamic', backref='role', cascade='all,delete-orphan')
class User(database.Model):
    __tablename__='User'
    user_id = database.Column(database.Integer, primary_key=True)
    User_name = database.Column(database.String, unique=False)
    user_password = database.Column(database.String, unique=False)
    role_id = database.Column(database.Integer, database.ForeignKey(Role.role_id))
    status = database.Column(database.String, default="registerd")
    participants = database.Relationship('Participate', lazy='dynamic', backref='User', cascade='all,delete-orphan')
class Area(database.Model):
    __tablename__='Area'
    area_id = database.Column(database.Integer, primary_key=True)
    area_name = database.Column(database.String, unique=True)
    events = database.Relationship('Event', lazy='dynamic', backref='Area', cascade='all,delete-orphan')
class Event(database.Model):
    __tablename__='Event'
    event_id = database.Column(database.Integer, primary_key=True)
    event_name = database.Column(database.String, unique=True)
    area_id = database.Column(database.Integer, database.ForeignKey(Area.area_id))
    status = database.Column(database.String, default="pending")
    events = database.Relationship('Participate', lazy='dynamic', backref='Event', cascade='all,delete-orphan')

class Participate(database.Model):
    application_id = database.Column(database.Integer, primary_key=True)
    event_id = database.Column(database.Integer, database.ForeignKey(Event.event_id), unique=False)
    user_id = database.Column(database.Integer, database.ForeignKey(User.user_id), unique=False)
