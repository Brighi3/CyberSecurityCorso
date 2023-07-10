from bs4 import BeautifulSoup
import requests

# URL della pagina HTML da analizzare
url = ''

# Effettua una richiesta GET alla pagina
response = requests.get(url)

# Controlla lo stato della richiesta
if response.status_code == 200:
    # Crea un oggetto BeautifulSoup a partire dal contenuto HTML della pagina
    soup = BeautifulSoup(response.content, 'html.parser')

    # Esempi di operazioni che è possibile eseguire con Beautiful Soup

    # Trova tutti gli elementi <a> e stampa i loro testi e attributi href
    links = soup.find_all('a')
    for link in links:
        print('Testo:', link.text)
        print('Href:', link.get('href'))
        print('---')

    # Trova il primo elemento con una determinata classe e stampa il suo testo
    element = soup.find(class_='my-class')
    if element:
        print('Testo del primo elemento con la classe "my-class":', element.text)

else:
    print('Errore nella richiesta HTTP:', response.status_code)