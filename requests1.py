import requests1


def test_header(ip_address):
    url = f"http://{ip_address}"
    try:
        response = requests.get(url)
        headers = response.headers
        print(f"Intestazioni del sito web all'indirizzo IP {ip_address}:")
        for header, value in headers.items():
            print(f"{header}: {value}")
    except requests.exceptions.RequestException as e:
        print(f"Errore durante la richiesta: {e}")


# Esempio di utilizzo
ip = ""  # Inserisci qui l'indirizzo IP del sito web da testare
test_header(ip)