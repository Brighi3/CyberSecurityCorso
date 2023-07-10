import mysql.connector
import bcrypt
from flask import Flask, render_template, request
from cryptography.fernet import Fernet
import mysql.connector
import bcrypt
from flask import Flask, render_template, request

# Configurazione del database MySQL
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'password',
    'database': 'mydatabase'
}

# Chiave di crittografia generata casualmente
key = Fernet.generate_key()


def encrypt_password(password):
    cipher_suite = Fernet(key)
    encrypted_password = cipher_suite.encrypt(password.encode('utf-8'))
    return encrypted_password


def decrypt_password(encrypted_password):
    cipher_suite = Fernet(key)
    decrypted_password = cipher_suite.decrypt(encrypted_password)
    return decrypted_password.decode('utf-8')


def insert_access(username, password):
    # Crittografa la password
    encrypted_password = encrypt_password(password)

    # Connessione al database MySQL
    mydb = mysql.connector.connect(**db_config)

    # Creazione del cursore per eseguire le query
    cursor = mydb.cursor()

    # Query SQL per inserire i dati nella tabella "accessi"
    query = "INSERT INTO accessi (username, password) VALUES (%s, %s)"
    values = (username, encrypted_password)

    # Esegui la query per inserire i dati
    cursor.execute(query, values)

    # Esegui il commit delle modifiche al database
    mydb.commit()

    # Chiudi il cursore e la connessione al database
    cursor.close()
    mydb.close()


def print_accessi():
    # Connessione al database MySQL
    mydb = mysql.connector.connect(**db_config)

    # Creazione del cursore per eseguire le query
    cursor = mydb.cursor()

    # Query SQL per ottenere tutti i record dalla tabella "accessi"
    query = "SELECT * FROM accessi"

    # Esegui la query per ottenere i dati
    cursor.execute(query)

    # Recupera tutti i record restituiti dalla query
    accessi = cursor.fetchall()

    # Stampa i dati di ogni record
    for accesso in accessi:
        username = accesso[1]
        encrypted_password = accesso[2]
        data_accesso = accesso[3]

        # Decrittografa la password
        decrypted_password = decrypt_password(encrypted_password)

        # Stampa i dati
        print("Username:", username)
        print("Password:", decrypted_password)
        print("Data accesso:", data_accesso)
        print()

    # Chiudi il cursore e la connessione al database
    cursor.close()
    mydb.close()


# Creazione dell'applicazione Flask
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Connessione al database MySQL
        mydb = mysql.connector.connect(**db_config)

        # Creazione del cursore per eseguire le query
        cursor = mydb.cursor()

        # Query SQL per ottenere il record corrispondente all'utente inserito
        query = "SELECT * FROM accessi WHERE username = %s"
        values = (username,)

        # Esegui la query per ottenere il record
        cursor.execute(query, values)

        # Recupera il primo record restituito dalla query
        accesso = cursor.fetchone()

        # Verifica se il record esiste e se la password corrisponde
        if accesso and bcrypt.checkpw(password.encode('utf-8'), accesso[2].encode('utf-8')):
            return f"Benvenuto, {username}!"
        else:
            # Chiamata alla funzione per inserire i dati nel database
            insert_access(username, password)

            # Chiamata alla funzione per stampare i dati della tabella accessi
            print_accessi()

            return "Registrazione avvenuta correttamente!"

        # Chiudi il cursore e la connessione al database
        cursor.close()
        mydb.close()

    return render_template('register.html')


if __name__ == '__main__':
    app.run()