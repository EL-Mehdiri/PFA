from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db   ##means from __init__.py import db
from flask_login import login_user, login_required, logout_user, current_user


auth = Blueprint('auth', __name__)



@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in successfully!', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect password, try again.', category='error')
        else:
            flash('Email does not exist.', category='error')

    return render_template("login.html", user=current_user)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))


@auth.route('/signup', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        firstname = request.form.get('firstname')
        lastname = request.form.get('lastname')
        username = request.form.get('username')
        job = request.form.get('job')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email already exists.', category='error')
        elif len(email) < 4:
            flash('Email must be greater than 3 characters.', category='error')
        elif len(firstname) < 2:
            flash('First name must be greater than 1 character.', category='error')
        elif password1 != password2:
            flash('Passwords don\'t match.', category='error')
        elif len(password1) < 7:
            flash('Password must be at least 7 characters.', category='error')
        else:
            new_user = User(email=email, firsname=firstname,lastname=lastname,username=username,job=job, password=generate_password_hash(
                password1, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            flash('Account created!', category='success')
            return redirect(url_for('auth.login'))

    return render_template("signup.html", user=current_user)

@auth.route('/profil/<int:user_id>/update', methods=['GET', 'POST'])
@login_required
def profile(user_id):         
    user = User.query.get(user_id)
    if request.method == "POST":
        #if email already existed dont update 
        user = User.query.filter_by(email=request.form["email"]).first()
        if not (user is None or user== current_user ):
            flash('This Email Already Exist! Please Try Another One...',category="error")
            return redirect(url_for('views.home')) 
        else :
            user = User.query.get(user_id)
            user.email = request.form["email"] 
            
        
            user.firsname = request.form['firsname']
            user.lastname = request.form['lastname']
            user.job = request.form['job']
            user.username = request.form['username']
            # user.password = request.form.get('password')
            # user.password=generate_password_hash(user.password, method='sha256')
            db.session.commit()
            flash('Your profil has been updated!', category='success')
            return redirect(url_for('views.home'))
    return render_template('profil.html', user=user )
@auth.route('/password/<int:user_id>/update', methods=['GET', 'POST'])
@login_required
def change_password(user_id):         
    user = User.query.get(user_id)
    if request.method == "POST":
        password = request.form.get('password')
        password1 = request.form.get('password1')
        if password != password1:
            flash('Passwords don\'t match.', category='error')
        else :
            user = User.query.get(user_id)
            user.password = request.form.get('password')
 
            user.password=generate_password_hash(user.password, method='sha256')
            db.session.commit()
            flash('Your password has been updated!', category='success')
        return redirect(url_for('views.home'))
    return render_template('change_password.html', user=user )