import mysql.connector


def create_table():
    # Configura la connessione al database MySQL
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database=""
    )

    # Crea il cursore per eseguire le query
    cursor = mydb.cursor()

    # Definisci la query SQL per creare la tabella
    query = """
    CREATE TABLE IF NOT EXISTS accessi (
        id INT AUTO_INCREMENT PRIMARY KEY,
        username VARCHAR(255),
        password VARCHAR(255),
        data_accesso DATETIME
    )
    """

    # Esegui la query per creare la tabella
    cursor.execute(query)

    # Chiudi la connessione al database
    cursor.close()
    mydb.close()


# Chiamata alla funzione per creare la tabella
create_table()
