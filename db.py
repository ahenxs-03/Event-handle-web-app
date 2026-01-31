from flask_sqlalchemy import SQLAlchemy
#from app import create
from flask_login import UserMixin
from werkzeug.security import generate_password_hash
#app=create()
database = SQLAlchemy()
class Role(database.Model):
    __tablename__ = 'Role'
    role_id = database.Column(database.Integer, primary_key=True)
    role_name = database.Column(database.String, unique=True)
    users = database.Relationship(
        'User', lazy='dynamic', backref='role', cascade='all,delete-orphan')


class User(database.Model, UserMixin):
    __tablename__ = 'User'
    user_id = database.Column(database.Integer, primary_key=True)
    User_email_id = database.Column(
        database.String, unique=True, nullable=False)
    User_name = database.Column(database.String, unique=False)
    user_password = database.Column(database.String, unique=False)
    role_id = database.Column(
        database.Integer, database.ForeignKey(Role.role_id))
    host = database.Relationship(
        'Host', lazy='dynamic', backref='User', cascade='all,delete-orphan')
    student = database.Relationship(
        'Student', lazy='dynamic', backref='User', cascade='all,delete-orphan')

    def get_id(self):
        return str(self.user_id)


class Student(database.Model):
    __tablename__ = 'Student'
    student_id = database.Column(database.Integer, primary_key=True)
    User_id = database.Column(
        database.Integer, database.ForeignKey(User.user_id), unique=False)
    roll = database.Column(database.String, unique=True)
    level = database.Column(database.String, unique=False)


class Host(database.Model):
    __tablename__ = 'Host'
    host_id = database.Column(database.Integer, primary_key=True)
    User_id = database.Column(
        database.Integer, database.ForeignKey(User.user_id), unique=False)
    about = database.Column(database.String, unique=True)
    website = database.Column(database.String, unique=True)
    events = database.Relationship(
        'Event', lazy='dynamic', backref='Event', cascade='all,delete-orphan')
    status = database.Column(database.String, default="pending")


class Area(database.Model):
    __tablename__ = 'Area'
    area_id = database.Column(database.Integer, primary_key=True)
    area_name = database.Column(database.String, unique=True)
    events = database.Relationship(
        'Event', lazy='dynamic', backref='Area', cascade='all,delete-orphan')


class Event(database.Model):
    __tablename__ = 'Event'
    event_id = database.Column(database.Integer, primary_key=True)
    event_name = database.Column(database.String, unique=True)
    area_id = database.Column(
        database.Integer, database.ForeignKey(Area.area_id))
    status = database.Column(database.String, default="pending")
    events = database.Relationship(
        'Participate', lazy='dynamic', backref='Event', cascade='all,delete-orphan')
    host = database.Column(
        database.Integer, database.ForeignKey(Host.host_id), unique=False)


class Participate(database.Model):
    application_id = database.Column(database.Integer, primary_key=True)
    event_id = database.Column(
        database.Integer, database.ForeignKey(Event.event_id), unique=False)
    user_id = database.Column(
        database.Integer, database.ForeignKey(User.user_id), unique=False)


# with app.app_context():
    #     add admin
    # student_role = Role(role_name="student")
    # host_role = Role(role_name="host")
    # admin_role = Role(role_name="admin")

    # admin = User(User_email_id="admin123xyz@asso.co.in", User_name="User_Admin",
    #             user_password=generate_password_hash("1234"), role_id=3)

    # database.session.add_all([student_role, host_role, admin_role, admin])
    # database.session.commit()

    # database.drop_all()
    # database.session.commit()
    # database.create_all()
    # database.session.commit()
