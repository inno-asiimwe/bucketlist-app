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
    plan.logout_user(session['username'])
    session.pop('username', None)
    return redirect(url_for('log_in'))

@app.route('/createuser', methods = [ 'GET','POST'])
def create_user():
    if request.method == 'POST':
        plan.create_user(request.form['fname'], request.form['lname'], request.form['username'], request.form['password'], request.form['email'])
        return redirect(url_for('index'))
    else:
        return render_template('newuser.html')
        
    
    


