from flask_mysqldb import MySQL
import MySQLdb.cursors
from app001 import app
import bcrypt

app.secret_key = 'this is secret key'

app.config['MYSQL_HOST'] = 'myflaskdb.ch8eewmwhrfk.us-east-2.rds.amazonaws.com'
app.config['MYSQL_USER'] = 'admin'
app.config['MYSQL_PASSWORD'] = '134679as!#'
app.config['MYSQL_DB'] = 'myFlaskApp'
app.config['MYSQL_PORT'] = 3306

mysql = MySQL(app)


class User():
    def login_check(input_username, input_password):
        input_password = input_password.encode('utf-8')

        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM accounts WHERE username = %s', [input_username])

        account = cursor.fetchone()
        check_password = bcrypt.checkpw(input_password, account['password'].encode('utf-8'))
        return account, check_password

    def get_information(id):
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM accounts WHERE id = %s', id)
        account = cursor.fetchone()
        return account

    def update_fromip(fromip, id):
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('UPDATE `myFlaskApp`.`accounts` SET `fromip`=%s WHERE `id`=%s', (fromip, str(id)))
        mysql.connection.commit()

    def useradd(username, password, email):
        # bcrypt hash transfer
        password = (bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())).decode('utf-8')
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('INSERT INTO `accounts` (`username`, `password`, `email`) VALUES (%s, %s, %s)',
                       (username, password, email))
        mysql.connection.commit()

    def check_username_exist(username):
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM accounts WHERE username = %s', (username, ))
        account = cursor.fetchone()
        return account

    def check_email_exist(email):
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM accounts WHERE email = %s', (email, ))
        account = cursor.fetchone()
        return account




