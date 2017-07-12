from app import app, render_template, request, session, url_for, redirect,flash
from app.classes.planner import Planner

plan = Planner()

@app.route('/')
def index():
    if 'name' in session:
        return render_template('home.html')
    else:
        return redirect(url_for('log_in'))

@app.route('/login', methods=['GET', 'POST'])
def log_in():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if (plan.login_user(username, password)):
            session['name'] = username
            flash("Login success ...")
            return redirect(url_for('index'))
        else:
            flash("Login failed ...")
            return render_template('login.html')
    else:
        return render_template('login.html')
@app.route('/logout', methods=['GET', 'POST'])
def log_out():
    if 'name' in session:
        plan.logout_user(session['name'])
        session.pop('name', None)
        return redirect(url_for('log_in'))
    else:
        return redirect(url_for('log_in'))


@app.route('/createuser', methods = [ 'GET','POST'])
def create_user():
    if request.method == 'POST':
        plan.create_user(request.form['fname'], request.form['lname'], request.form['username'], request.form['password'], request.form['email'])
        return redirect(url_for('index'))
    else:
        return render_template('newuser.html')

@app.route('/create_bucketlist', methods = ['Get','POST'])
def create_bucketlist():
    if 'name' in session:
        if request.method == 'POST':
            plan.users[session['name']].create_bucketlist(request.form['name'], request.form['description'])
            return redirect(url_for('index'))
        else:
            return render_template('newbucketlist.html')
    else:
        return redirect(url_for('log_in'))

        
    
    


