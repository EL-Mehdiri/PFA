from . import db 
from flask_login import UserMixin, current_user
from flask_admin.contrib.sqla import ModelView
from datetime import datetime
from flask import abort, flash
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
class UserView(ModelView):
    def is_accessible(self):
        if current_user.username == "admin":
            return True
        else:
            flash("You are not authorized to view this page")
    form_columns = ['username', 'email', 'date_created']
    column_exclude_list = ['password']
    can_create = False
    can_edit = False
    can_view_details = True


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
    
class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(200), nullable=False)
    date_created = db.Column(db.DateTime(timezone=True), default=func.now())
    author = db.Column(db.Integer, db.ForeignKey('user.id', ondelete="CASCADE"), nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey('group.id', ondelete="CASCADE"), nullable=False)

class UserView(ModelView):
    def is_accessible(self):
        if current_user.is_authenticated and current_user.email == "admin@admin.com":
            return True
        else:
            abort(404)
            
    form_columns = ['username', 'email']
    column_exclude_list = ['password']
    can_create = False
    can_edit = False
    can_view_details = True


class TaskView(ModelView):
    def is_accessible(self):
        if current_user.is_authenticated and current_user.email == "admin@admin.com":

            return True
        else:
            abort(404)
    form_columns = ['title', "descreption", 'date_posted','start', 'end']

class CommentView(ModelView):
    def is_accessible(self):
        if current_user.is_authenticated and current_user.email == "admin@admin.com":
            return True
        else:
            abort(404)
    form_columns = ['text', 'date_created', "author"]
    can_create = False
    can_view_details = True
    
class GroupView(ModelView):
    def is_accessible(self):
        if current_user.is_authenticated and current_user.email == "admin@admin.com":
            return True
        else:
            abort(404)
    form_columns = ['title', 'date_posted', "start" , "end", "descreption", "comments"]
    can_create = False
    can_view_details = True


