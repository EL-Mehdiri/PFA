from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager
from flask_admin import Admin

db = SQLAlchemy()
DB_NAME = 'database.db'




def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'mysecretkey'
    app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{DB_NAME}"
    app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'
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
    

    admin = Admin(app,  name="Task Zineth", template_mode='bootstrap3')
    
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
        