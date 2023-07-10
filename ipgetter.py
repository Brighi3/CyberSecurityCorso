import socket

url1 = "" \

def get_ip_address(url):
    try:
        # Ottiene l'indirizzo IP corrispondente all'URL
        ip_address = socket.gethostbyname(url)
        print(f"L'indirizzo IP per {url} è: {ip_address}")
    except socket.error as e:
        print(f"Impossibile ottenere l'indirizzo IP per {url}: {str(e)}")


get_ip_address(url1)


