import mysql.connector
from flask_wtf import FlaskForm
from flask_wtf.csrf import CSRFProtect
from wtforms import Form, StringField, PasswordField, validators
import datetime
import os
from dotenv import load_dotenv
from passlib.hash import bcrypt
from flask import Flask, request, render_template

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
csrf = CSRFProtect(app)
load_dotenv('Flask_8.env')
db_username = os.getenv('DB_USERNAME')
db_password = os.getenv('DB_PASSWORD')
db_name = os.getenv('DB_NAME')
class LoginForm(Form):
    username = StringField('Username', validators=[validators.DataRequired()])
    password = PasswordField('Password', validators=[validators.DataRequired()])

# Funzione per criptare la password utilizzando bcrypt
def encrypt_password(password):
    hashed_password = bcrypt.hash(password)
    return hashed_password

# Funzione per registrare un nuovo utente nel database
def register_user(username, password):
    encrypted_password = encrypt_password(password)

    # Connessione al database
    connection = mysql.connector.connect(
        host='localhost',
        user=db_username,
        password=db_password,
        database=db_name
    )
    cursor = connection.cursor()

    # Inserimento dei dati nel database
    print("Username: ", username," Password:", encrypted_password)
    insert_query = "INSERT INTO users (username, password, access_date) VALUES (%s, %s, %s)"
    current_date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    cursor.execute(insert_query, (username, encrypted_password, current_date))
    connection.commit()

    cursor.close()
    connection.close()

# Funzione per effettuare il login dell'utente
def login(username, password):
    # Validazione dei dati di input
    form = LoginForm(request.form)
    if not form.validate():
        return render_template('login3.html', message="Input non valido.")
    # Connessione al database
    connection = mysql.connector.connect(
        host='localhost',
        user=db_username,
        password=db_password,
        database=db_name
    )
    cursor = connection.cursor()

    # Verifica dell'utente nel database
    select_query = "SELECT * FROM users WHERE username = %s"
    cursor.execute(select_query, (username,))
    user = cursor.fetchone()

    if user is None:
        return render_template('login3.html', message="L'utente non esiste.")
    else:
        stored_password = user[2]
        if bcrypt.verify(password, stored_password):
            current_date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            return render_template('welcome2.html', username=username, access_date=current_date)
        else:
            return render_template('login3.html', message="Password errata.")

    cursor.close()
    connection.close()

@app.route('/')
def index():
    form = LoginForm()  # Crea un'istanza del form di login
    return render_template('login3.html', form=form)

@app.route('/login', methods=['POST'])
def handle_login():
    username = request.form['username']
    password = request.form['password']
    return login(username, password)

@app.route('/register')
def register():
    form = LoginForm(request.form)
    if not form.validate():
        return render_template('register2.html', message="Input non valido.")
    return render_template('register2.html')

@app.route('/register', methods=['POST'])
def handle_register():
    username = request.form['username']
    password = request.form['password']
    register_user(username, password)
    return render_template('registration_success.html')

if __name__ == '__main__':
    app.run()
