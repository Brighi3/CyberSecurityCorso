from flask import Flask, render_template, request
import re
import matplotlib.pyplot as plt
import numpy as np

app = Flask(__name__)

def calculate_password_security(password):
    # Calcola i punteggi di sicurezza della password
    scores = {
        'length': len(password) / 20 * 100,
        'special_chars': len(re.findall(r'[!@#$%^&*(),.?":{}|<>]', password)) / 3 * 100,
        'case': len(re.findall(r'[a-z]', password)) / 3 * 100 + len(re.findall(r'[A-Z]', password)) / 3 * 100,
        'non_alphanumeric': len(re.findall(r'\W', password)) / 3 * 100
    }
    return scores

def create_column_chart(scores):
    # Crea un grafico a colonne dei punteggi di sicurezza
    labels = ['Lunghezza', 'Caratteri speciali', 'Maiuscole e minuscole', 'Caratteri non alfanumerici']
    scores = [scores['length'], scores['special_chars'], scores['case'], scores['non_alphanumeric']]
    colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99']  # Colori delle colonne

    x = np.arange(len(labels))  # Posizioni delle colonne sull'asse x

    fig, ax = plt.subplots()
    bars = ax.bar(x, scores, color=colors)

    # Aggiungi le etichette alle colonne
    for i, bar in enumerate(bars):
        height = bar.get_height()
        ax.annotate(f'{height:.1f}', xy=(bar.get_x() + bar.get_width() / 2, height),
                    xytext=(0, 3), textcoords="offset points",
                    ha='center', va='bottom')

    ax.set_ylabel('Punteggio')
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.set_title('Punteggi di Sicurezza')

    plt.tight_layout()
    plt.savefig('static/column_chart.png')  # Salva il grafico come immagine
    plt.close()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        password = request.form['password']
        scores = calculate_password_security(password)
        create_column_chart(scores)
        return render_template('result3.html', password=password, scores=scores)
    return render_template('index3.html')

if __name__ == '__main__':
    app.run()
