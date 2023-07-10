from flask import Flask, render_template, request
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('form.html')


@app.route('/send_email', methods=['POST'])
def send_email():
    sender_email = request.form['sender_email']
    sender_password = request.form['sender_password']
    recipient_email = request.form['recipient_email']
    subject = request.form['subject']
    message = request.form['message']

    # Configura i dettagli del server SMTP di Gmail
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587

    # Crea un oggetto SMTP
    smtp_obj = smtplib.SMTP(smtp_server, smtp_port)

    # Avvia la connessione con il server SMTP
    smtp_obj.starttls()

    # Effettua il login all'account Gmail
    smtp_obj.login(sender_email, sender_password)

    # Crea il messaggio email
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = subject

    # Aggiungi il corpo del messaggio
    msg.attach(MIMEText(message, 'plain'))

    # Invia l'email
    smtp_obj.send_message(msg)

    # Chiudi la connessione con il server SMTP
    smtp_obj.quit()

    return 'Email inviata con successo!'


# Resto del codice

if __name__ == '__main__':
    app.run()

