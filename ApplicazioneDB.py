from flask import Flask, render_template, request
import mysql.connector
from datetime import datetime

app = Flask(__name__)

# Configurazione del database
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '',
    'database': 'prova'
}

def insert_access(username, password):
    # Connessione al database MySQL
    mydb = mysql.connector.connect(**db_config)

    # Creazione del cursore per eseguire le query
    cursor = mydb.cursor()

    # Ottieni la data e l'ora corrente
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    # Query SQL per inserire i dati nella tabella "accessi"
    query = "INSERT INTO accessi (username, password, data_accesso) VALUES (%s, %s, %s)"
    values = (username, password, current_time)

    # Esegui la query per inserire i dati
    cursor.execute(query, values)

    # Applica le modifiche al database
    mydb.commit()

    # Chiudi il cursore e la connessione al database
    cursor.close()
    mydb.close()

@app.route('/', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Chiamata alla funzione per inserire i dati nel database
        insert_access(username, password)

        return "Registrazione avvenuta con successo!"
    return render_template('register.html')

if __name__ == '__main__':
    app.run(debug=True)
