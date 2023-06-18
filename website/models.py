from . import db 
from flask_login import UserMixin, current_user
# from sqlalchemy.sql import func
from flask_admin.contrib.sqla import ModelView
from datetime import datetime
from hashlib import md5
from sqlalchemy.sql import func


    

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    firsname = db.Column(db.String(100))
    lastname = db.Column(db.String(100))
    username = db.Column(db.String(200))
    job = db.Column(db.String(200))
    workouts = db.relationship('Task', backref='author', lazy=True)
    groups = db.relationship('Group', backref='author', lazy=True)
    comments = db.relationship('Comment', backref='user', passive_deletes=True)
    # role = db.Column(db.String(20))
    
    def avatar(self, size):
        digest = md5(self.email.lower().encode('utf-8')).hexdigest()
        return 'https://www.gravatar.com/avatar/{}?d=identicon&s={}'.format(digest, size)



class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Integer, nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    start = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    end = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    descreption = db.Column(db.Text, nullable=False)
    deleted = db.Column(db.Boolean, default=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.firsname'), nullable=False)
# group 

class Group(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Integer, nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    start = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    end = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    descreption = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.firsname'), nullable=False)
    comments = db.relationship('Comment', backref='Group', passive_deletes=True)
    # group_user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    
class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(200), nullable=False)
    date_created = db.Column(db.DateTime(timezone=True), default=func.now())
    author = db.Column(db.Integer, db.ForeignKey('user.id', ondelete="CASCADE"), nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey('group.id', ondelete="CASCADE"), nullable=False)


    # tasks = db.relationship('Task', backref='group', lazy=True)

# class Task(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(100), nullable=False)
#     group_id = db.Column(db.Integer, db.ForeignKey('group.id'), nullable=False)
#     assigned_to = db.relationship('User', secondary='task_assignments')

# # class Userr(db.Model):
# #     id = db.Column(db.Integer, primary_key=True)
# #     name = db.Column(db.String(100), nullable=False)

# task_assignments = db.Table('task_assignments',
#     db.Column('task_id', db.Integer, db.ForeignKey('task.id'), primary_key=True),
#     db.Column('user_id', db.Integer, db.ForeignKey('user.id'), primary_key=True)
# )