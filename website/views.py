from flask import  Blueprint, render_template, request, flash, redirect, url_for,jsonify
from flask_login import  login_required, current_user
from .models import Task, User, Group,Comment
from . import db
from datetime import datetime



views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
@login_required
def home():         
    users = User.query.all()
    user = User.query.filter_by(email=current_user.email).first_or_404()
    
    task_count = Task.query.filter_by(author=user).order_by(Task.date_posted.desc()).count()
    task_group = Group.query.count()
    count = User.query.count()
    workouts = Task.query.filter_by(author=user).order_by(Task.date_posted.desc())
    print(users)
    return render_template('home.html',workouts=workouts, user=current_user, task_group=task_group , users=users , task_count=task_count, count=count)


@views.route("/all", methods=['GET', 'POST'])
@login_required
def user_workouts():
    if request.method == 'POST':
        search = request.form.get('search') 
        workouts = Task.query.filter(Task.title.contains(search)).all()
        
        # workouts = Task.query.filter_by(workout.title.like('%'+search+'%')).all()
        print(workouts)
        if workouts == []:
            flash('No task found', category='error')
        return render_template('all_workouts.html', workouts=workouts, user=current_user)
        
    else:
        user = User.query.filter_by(email=current_user.email).first_or_404()
        workouts = Task.query.filter_by(author=user).order_by(Task.date_posted.desc())
        return render_template('all_workouts.html', workouts=workouts, user=current_user)

            
@views.route('/new')
@login_required
def new_workout():
    return render_template('create_workout.html', user=current_user)
            
@views.route('/new', methods=['GET', 'POST'])
@login_required
def user_workout():
    starttask = request.form.get('start')
    start_datetime = datetime.strptime(starttask, "%Y-%m-%dT%H:%M")

    endtask = request.form.get('end')
    end_datetime = datetime.strptime(endtask, "%Y-%m-%dT%H:%M")
    # end = start_datetime.strftime("%Y-%m-%d")
    workout = Task(
        title=request.form.get('title'),
        date_posted=datetime.now(),
        start=start_datetime,
        end=end_datetime,
        descreption=request.form.get('descreption'),
        # user_id=request.form.get('user_id')
        author=current_user
    )
    
    
    
    db.session.add(workout)
    db.session.commit()
    flash('Your Task has been added!', category='success')
    return redirect(url_for('views.user_workouts'))


@views.route("/Task/<int:workout_id>/update", methods=['GET', 'POST'])
@login_required
def update_workout(workout_id):
    workout = Task.query.get_or_404(workout_id)
    if request.method == "POST":
        workout.title = request.form['title']
        workout.descreption = request.form['descreption']
        start = request.form['start']
        end =  request.form['end']
        workout.start = datetime.strptime(start, "%Y-%m-%dT%H:%M")
        workout.end = datetime.strptime(end, "%Y-%m-%dT%H:%M")
        db.session.commit()
        flash('Your Task has been updated!', category='success')
        return redirect(url_for('views.user_workouts'))

    return render_template('update_workout.html', workout=workout, user=current_user)

@views.route("/workout/<int:workout_id>/delete", methods=['GET', 'POST'])
@login_required
def delete_workout(workout_id):
    workout = Task.query.get_or_404(workout_id)
    workout.deleted = True
    db.session.delete(workout)
    db.session.commit()
    flash('Your Task has been deleted!')
    return redirect(url_for('views.user_workouts'))


@views.route("/workout/<int:id>/completed", methods=['GET', 'POST'])
@login_required
def completed_workout(id):
    workout = Task.query.get_or_404(id)
    workout.deleted = True
    db.session.delete(workout)
    db.session.commit()
    flash('Your Task has been completed!')
    return redirect(url_for('views.user_workouts'))



@views.route('calender')
@login_required
def calender():
    user = User.query.filter_by(email=current_user.email).first_or_404()
    events = Task.query.filter_by(author=user).order_by(Task.date_posted.desc())
    group = Group.query.filter_by(author=user).order_by(Group.date_posted.desc())
    #  = Task.query.all()
    
    calendar_events = []
    for event in events:
        calendar_event = {
            'title': event.title,
            'start': event.start.strftime('%Y-%m-%d'),
            'end': event.end.strftime('%Y-%m-%d'),
        }
        
        calendar_events.append(calendar_event)
    
    for event in group:
        group_event = {
            'title': event.title,
            'start': event.start.strftime('%Y-%m-%d'),
            'end': event.end.strftime('%Y-%m-%d'),
        }
        
        calendar_events.append(group_event)
    
    
    return render_template('calender.html', user=current_user, events=calendar_events)




@views.route('/group_calender')
@login_required
def group_calender():
    
    events = Group.query.all()
    #  = Task.query.all()
    
    calendar_events = []
    for event in events:
        calendar_event = {
            'title': event.title,
            'start': event.start.strftime('%Y-%m-%d'),
            'end': event.end.strftime('%Y-%m-%d'),
        }
        calendar_events.append(calendar_event)
    print(calendar_events)
    
    return render_template('group_calender.html', user=current_user, events=calendar_events)





# # group 

@views.route('/groups', methods=['GET', 'POST'])
@login_required
def groups():
    if request.method == 'POST':
        search = request.form.get('search') 
        groups = Group.query.filter(Group.title.contains(search)).all()
        
    
        if groups == []:
            flash('No task found', category='error')
        return render_template('groups.html', groups=groups, user=current_user)
        
    else:
        groups = Group.query.all()
        return render_template('groups.html', groups=groups, user=current_user)
    
    
@views.route('/new_group_task')
@login_required
def new_group_workout():
    return render_template('create_group.html', user=current_user)

@views.route('/new_group_task', methods=['GET', 'POST'])
@login_required
def group_workout():
    starttask = request.form.get('start')
    start_datetime = datetime.strptime(starttask, "%Y-%m-%dT%H:%M")
    endtask = request.form.get('end')
    end_datetime = datetime.strptime(endtask, "%Y-%m-%dT%H:%M")
    workout = Group(
        title=request.form.get('title'),
        date_posted=datetime.now(),
        start=start_datetime,
        end=end_datetime,
        descreption=request.form.get('descreption'),
        author=current_user
    )
    db.session.add(workout)
    db.session.commit()
    flash('Your Task has been added!', category='success')
    return redirect(url_for('views.groups'))

@views.route("/group/<int:group_id>/delete", methods=['GET', 'POST'])
@login_required
def delete_group_task(group_id):
    group = Group.query.get_or_404(group_id)
    db.session.delete(group)
    db.session.commit()
    flash('Your Task has been deleted!')
    return redirect(url_for('views.groups'))



@views.route("/Task/<int:group_id>/update", methods=['GET', 'POST'])
@login_required
def update_group_task(group_id):
    group = Group.query.get_or_404(group_id)
    if request.method == "POST":
        group.title = request.form['title']
        group.descreption = request.form['descreption']
        start = request.form['start']
        end =  request.form['end']
        group.start = datetime.strptime(start, "%Y-%m-%dT%H:%M")
        group.end = datetime.strptime(end, "%Y-%m-%dT%H:%M")
        db.session.commit()
        flash('Your Task has been updated!', category='success')
        return redirect(url_for('views.groups'))

    return render_template('update_task_group.html', group=group, user=current_user)



# Comment

@views.route("/create-comment/<post_id>", methods=['POST'])
@login_required
def create_comment(post_id):
    text = request.form.get('text')

    if not text:
        flash('Comment cannot be empty.', category='error')
    else:
        post = User.query.filter_by(id=post_id)
        if post:
            comment = Comment(
                text=text, author=current_user.id, post_id=post_id)
            db.session.add(comment)
            db.session.commit()
        else:
            flash('Task does not exist.', category='error')

    return redirect(url_for('views.groups'))


@views.route("/delete-comment/<comment_id>")
@login_required
def delete_comment(comment_id):
    comment = Comment.query.filter_by(id=comment_id).first()

    if not comment:
        flash('Comment does not exist.', category='error')
    elif current_user.id != comment.author and current_user.id != comment.post.author:
        flash('You do not have permission to delete this comment.', category='error')
    else:
        db.session.delete(comment)
        db.session.commit()
    return redirect(url_for('views.groups'))