from flask import Flask, render_template, request
import mysql.connector
import bcrypt
import itertools
from datetime import datetime
from cryptography.fernet import Fernet

app = Flask(__name__)

# Configurazione del database
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '',
    'database': 'prova'
}


def encrypt_password(password):
    # Genera un salt casuale
    salt = bcrypt.gensalt()

    # Crittografa la password utilizzando il salt
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)

    # Restituisce la password crittografata come stringa
    return hashed_password.decode('utf-8')


def insert_access(username, password):
    # Crittografa la password
    print()
    encrypted_password = encrypt_password(password)

    # Connessione al database MySQL
    mydb = mysql.connector.connect(**db_config)

    # Creazione del cursore per eseguire le query
    cursor = mydb.cursor()

    # Ottieni la data e l'ora corrente
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    # Query SQL per inserire i dati nella tabella "accessi"
    query = "INSERT INTO accessi (username, password, data_accesso) VALUES (%s, %s, %s)"
    values = (username, encrypted_password, current_time)

    # Esegui la query per inserire i dati
    cursor.execute(query, values)

    # Applica le modifiche al database
    mydb.commit()

    # Chiudi il cursore e la connessione al database
    cursor.close()
    mydb.close()


def verify_password(plain_password, hashed_password):
    # Confronta la password in chiaro con la versione crittografata
    return bcrypt.checkpw(plain_password.encode('utf-8'), hashed_password.encode('utf-8'))


def get_password(username):
    # Connessione al database MySQL
    mydb = mysql.connector.connect(**db_config)

    # Creazione del cursore per eseguire le query
    cursor = mydb.cursor()

    # Query SQL per ottenere la password associata all'username
    query = "SELECT password FROM accessi WHERE username = %s"
    values = (username,)

    # Esegui la query per ottenere la password
    cursor.execute(query, values)

    # Ottieni il risultato della query
    result = cursor.fetchone()

    # Chiudi il cursore e la connessione al database
    cursor.close()
    mydb.close()

    if result:
        # Restituisce la password crittografata come stringa
        return result[0]
    else:
        return None


@app.route('/', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Chiamata alla funzione per inserire i dati nel database
        insert_access(username, password)
        '''print_accessi()'''

        return "Registrazione avvenuta con successo!"
    return render_template('register.html')


'''def print_accessi():
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
        decrypted_password = ""
        # Decrittografa la password
        characters = list(range(32, 127))  # Caratteri ASCII stampabili
        password_length = 1  # Lunghezza iniziale della password
        found = False
        while password_length <= 30 and not found:
            print("password_length: ", password_length)
            for combination in itertools.product(characters, repeat=password_length):
                password = encrypt_password(''.join(chr(char) for char in combination))
                print(password)
                if password == encrypted_password:
                    found = True
                    decrypted_password = password
                    break
            password_length += 1

        # Stampa i dati
        print("Username:", username)
        print("Password:", str(decrypted_password))
        print("Data accesso:", data_accesso)
        print()

    # Chiudi il cursore e la connessione al database
    cursor.close()
    mydb.close()
'''

if __name__ == '__main__':
    app.run(debug=True)
