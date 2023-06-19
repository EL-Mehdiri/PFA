from flask import Flask, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from flask_admin import Admin, AdminIndexView, BaseView, expose
from flask_admin.contrib.sqla import ModelView

db = SQLAlchemy()
DB_NAME = 'database.db'




def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'mysecretkey'
    app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{DB_NAME}"
    db.init_app(app)
    
    
    
    from .views import views
    from .auth import auth
    
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    
    from .models import User , Task,  Comment, Group, UserView, TaskView, GroupView, CommentView
    
    login = LoginManager(app)
    
    @login.user_loader
    def load_user(user_id):
        return User.query.get(user_id)
    
    # class MyModelView(ModelView):
    #     def is_accessible(self):
    #         return current_user.is_authenticated
        
    #     def inaccessible_callback(self, name, **kwargs):
    #         return redirect(url_for('auth.login'))

    # class MyAdminIndexView(AdminIndexView):
    #     def is_accessible(self):
    #         return current_user.is_authenticated
    #     def inaccessible_callback(self, name, **kwargs):
    #         return redirect(url_for('auth.login'))
    
    
    admin = Admin(app,  name="Task Zineth")
    admin.add_view(UserView(User, db.session))
    admin.add_view(TaskView(Task, db.session))
    admin.add_view(CommentView(Comment, db.session))
    admin.add_view(GroupView(Group, db.session))
    create_database(app)
    
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)
    
    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))
    return app

def create_database(app):
    if not path.exists('website/' + DB_NAME):
        with app.app_context():
            db.create_all()
        