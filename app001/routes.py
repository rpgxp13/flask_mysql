from flask import render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re
from app001 import app

app.secret_key = 'this is secret key'

app.config['MYSQL_HOST'] = 'myflaskdb.ch8eewmwhrfk.us-east-2.rds.amazonaws.com'
app.config['MYSQL_USER'] = 'admin'
app.config['MYSQL_PASSWORD'] = '134679as!#'
app.config['MYSQL_DB'] = 'myFlaskApp'
app.config['MYSQL_PORT'] = 3306

mysql = MySQL(app)


@app.route('/login/', methods=['GET', 'POST'])
def login():
    return render_template('login.html', msg='testing now')