from flask import render_template, request, redirect, url_for, session, flash
import re
from app001 import app
from app001.models import User, Post


@app.route('/login/', methods=['GET', 'POST'])
def login():
    msg = ''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']

        account, check_password = User.login_check(username, password)

        if check_password:
            session['loggedin'] = True
            session['id'] = account['id']
            session['username'] = account['username']

            fromip = request.environ.get('HTTP_X_REAL_IP', request.remote_addr)
            User.update_fromip(fromip, account['id'])

            return redirect(url_for('home'))
        else:
            msg = 'Incorrect username or password!'

    if 'loggedin' in session:
        return redirect(url_for('home'))

    return render_template('login.html', msg=msg)


@app.route('/register', methods=['GET', 'POST'])
def register():
    msg = 'Creating User Page'

    if 'loggedin' in session:
        return redirect(url_for('home'))

    if request.method == 'POST' and 'username' in request.form and 'password' in request.form and 'email' in request.form:
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        username_already_exist = User.check_username_exist(username)
        email_already_exist = User.check_email_exist(email)

        if username_already_exist:
            msg = 'That username is already exist'
        elif email_already_exist:
            msg = 'That email is already exist'
        else:
            User.useradd(username, password, email)
            flash('Create User Success!')
            return redirect(url_for('login'))

    return render_template('register.html', msg=msg)


@app.route('/logout')
def logout():
    session.pop('loggedin', None)
    session.pop('id', None)
    session.pop('username', None)

    return redirect(url_for('login'))


@app.route('/home', methods=['GET', 'POST'])
def home():
    if 'loggedin' in session:

        posts = Post.get_Posts_title(session['id'])

        return render_template('home.html', username=session['username'], posts=posts)
    return redirect(url_for('login'))


@app.route('/post/<int:id>', methods=['GET', 'POST'])
def postviewer(id):
    if 'loggedin' in session:

        post = Post.get_Post(id)

        return render_template('postpage.html', post=post, user=session)

    return redirect('login')



@app.route('/profile')
def profile():
    if 'loggedin' in session:
        user = User.get_information([session['id']])
        return render_template('profile.html', user=user)

    return redirect(url_for('login'))


@app.route('/')
def root():
    if 'loggedin' in session:
        return redirect(url_for('home'))
    else:
        return redirect(url_for('login'))