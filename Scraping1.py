import requests
from bs4 import BeautifulSoup

# URL della pagina da cui effettuare lo scraping
url = ""

# Effettua la richiesta HTTP alla pagina
response = requests.get(url)

# Controlla lo stato della risposta
if response.status_code == 200:
    # Parsing del contenuto HTML della pagina
    soup = BeautifulSoup(response.content, "html.parser")

    # Trova il div con l'ID "copertina-tab"
    copertina_tab_div = soup.find("div", id="copertina-tab")

    # Verifica se il div è stato trovato
    if copertina_tab_div is not None:
        # Stampa il contenuto del div
        print(copertina_tab_div.text)
    else:
        print("Il div 'copertina-tab' non è stato trovato.")
else:
    print("Errore nella richiesta HTTP:", response.status_code)
