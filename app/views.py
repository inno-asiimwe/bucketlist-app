"""Module contains all the views for the App"""
from app import app, render_template, request, session, url_for, redirect, flash
from app.classes.planner import Planner

PLAN = Planner()

@app.route('/')
def index():
    """View handles the index page of the app"""
    if 'name' in session:
        return render_template('home.html')
    return redirect(url_for('log_in'))

@app.route('/login', methods=['GET', 'POST'])
def log_in():
    """View handles loging in a user"""
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if PLAN.login_user(username, password):
            session['name'] = username
            flash("Login success ...")
            return redirect(url_for('index'))
        flash("Login failed ...")
        return render_template('login.html')
    return render_template('login.html')

@app.route('/logout', methods=['GET', 'POST'])
def log_out():
    """View handles longing out a user"""
    if 'name' in session:
        PLAN.logout_user(session['name'])
        session.pop('name', None)
        return redirect(url_for('log_in'))
    return redirect(url_for('log_in'))

@app.route('/createuser', methods=['GET', 'POST'])
def create_user():
    """View handles creating a new User"""
    if request.method == 'POST':
        PLAN.create_user(request.form['fname'],
                         request.form['lname'],
                         request.form['username'],
                         request.form['password'],
                         request.form['email'])
        return redirect(url_for('index'))
    return render_template('newuser.html')

@app.route('/create_bucketlist', methods=['Get', 'POST'])
def create_bucketlist():
    """View handles creating a new bucketlist"""
    if 'name' in session:
        if request.method == 'POST':
            PLAN.users[session['name']].create_bucketlist(request.form['name'],
                                                          request.form['description'])
            return redirect(url_for('view_bucketlists'))
        return render_template('newbucketlist.html')
    return redirect(url_for('log_in'))

@app.route('/bucketlists')
def view_bucketlists():
    """view lists all bucketlists current"""
    if 'name' in session:
        bucket = PLAN.users[session['name']].view_bucketlists()
        return render_template('bucketlists.html', bucket=bucket)
    return redirect(url_for('log_in'))

@app.route('/bucketlists/<bucketlist_id>/delete')
def delete_bucketlist(bucketlist_id):
    """View handles deleting a bucketlist"""
    if 'name' in session:
        name = PLAN.get_name_from_id(bucketlist_id)
        PLAN.users[session['name']].delete_bucketlist(name)
        return redirect(url_for('view_bucketlists'))
    return redirect(url_for('log_in'))

@app.route('/create_activity/<bucketlist_id>', methods=['GET', 'POST'])
def create_activity(bucketlist_id):
    """view handles creating a bucketlist"""
    if 'name' in session:
        bucketlist = PLAN.get_name_from_id(bucketlist_id)
        if request.method == 'POST':
            PLAN.users[session['name']].create_activity(bucketlist,
                                                        request.form['name'],
                                                        request.form['description'])
            return redirect(url_for('view_activities', bucketlist_id=bucketlist_id))
        return render_template('newactivity.html')
    return redirect(url_for('log_in'))

@app.route('/bucketlists/<bucketlist_id>', methods=['GET', 'POST'])
def view_activities(bucketlist_id):
    """View lists all activities in a bucketlist"""
    if 'name' in session:
        bucketlist = PLAN.get_name_from_id(bucketlist_id)
        activities = PLAN.users[session['name']].view_bucketlist_activities(bucketlist)
        return render_template('activities.html',
                               activities=activities,
                               bucketlist=bucketlist,
                               bucketlist_id=bucketlist_id)
    return redirect(url_for('log_in'))
@app.route('/bucketlists/<bucketlist_id>/<activity_id>/delete')
def delete_activity(bucketlist_id, activity_id):
    """View for deleting an activity"""
    if 'name' in session:
        PLAN.users[session['name']].delete_activity(bucketlist_id, activity_id)
        return redirect(url_for('view_activities', bucketlist_id=bucketlist_id))
    return redirect(url_for('log_in'))
@app.route('/bucketlists/<bucketlist_id>/update', methods=['GET', 'POST'])
def update_bucketlist(bucketlist_id):
    """View for updating bucketlist"""
    if 'name' in session:
        if request.method == 'POST':
            PLAN.users[session['name']].update_bucketlist(bucketlist_id,
                                                          request.form['name'],
                                                          request.form['description'])
            return redirect(url_for('view_bucketlists'))
    return redirect(url_for('log_in'))
