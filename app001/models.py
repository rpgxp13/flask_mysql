from flask_mysqldb import MySQL
import MySQLdb.cursors
from app001 import app

app.secret_key = 'this is secret key'

app.config['MYSQL_HOST'] = 'myflaskdb.ch8eewmwhrfk.us-east-2.rds.amazonaws.com'
app.config['MYSQL_USER'] = 'admin'
app.config['MYSQL_PASSWORD'] = '134679as!#'
app.config['MYSQL_DB'] = 'myFlaskApp'
app.config['MYSQL_PORT'] = 3306

mysql = MySQL(app)


class User():
    def login_check(username, password):
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM accounts WHERE username = %s AND password = %s', (username, password))
        account = cursor.fetchone()
        return account

    def get_information(id):
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM accounts WHERE id = %s', id)
        account = cursor.fetchone()
        return account

    def update_fromip(fromip, id):
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('UPDATE `myFlaskApp`.`accounts` SET `fromip` = %s WEHERE `id` = %s', (fromip, id))
        mysql.connection.commit()


