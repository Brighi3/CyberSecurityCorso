import requests
import time
import socket
from urllib.parse import urlparse

# Mappatura dei livelli di gravità CVSS
CVSS_SEVERITY_MAP = {
    'None': 0,
    'Low': 1,
    'Medium': 4,
    'High': 7,
    'Critical': 10
}

def get_cvss_severity(score):
    # Mappa il punteggio CVSS alla corrispondente gravità
    if score < 4.0:
        return 'Low'
    elif score < 7.0:
        return 'Medium'
    elif score < 9.0:
        return 'High'
    else:
        return 'Critical'

def run_scan(url, ports):
    # Esecuzione della scansione
    print(f"Avvio della scansione di {url}...")
    vulnerabilities = []

    for port in ports:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(2)
            result = s.connect_ex((url, port))
            s.close()

            if result == 0:
                vulnerabilities.append((port, 'Open'))
            else:
                vulnerabilities.append((port, 'Closed'))

        except socket.error:
            vulnerabilities.append((port, 'Error'))

    return vulnerabilities

def analyze_services(url):
    # Connessione al sito
    try:
        response = requests.get(url)
    except requests.exceptions.RequestException as e:
        print("Errore durante la connessione al sito:", str(e))
        return

    # Ottenere i servizi del sito
    services = response.headers
    return services

def truncate_url(url):
    # Tronca l'header dall'URL
    parsed_url = urlparse(url)
    truncated_url = parsed_url.netloc
    return truncated_url

def print_vulnerabilities(vulnerabilities):
    # Statistiche delle vulnerabilità
    total_vulnerabilities = len(vulnerabilities)
    vulnerabilities_by_type = {}
    vulnerabilities_by_severity = {
        'Open': 0,
        'Closed': 0,
        'Error': 0
    }

    # Stampa le vulnerabilità individuate
    print("Risultati della scansione delle vulnerabilità:")
    if total_vulnerabilities > 0:
        for port, status in vulnerabilities:
            print("Porta: ", port)
            print("Stato: ", status)
            print("------------------------------------------------------")

            # Aggiorna le statistiche delle vulnerabilità
            vulnerability_type = status
            vulnerabilities_by_type.setdefault(vulnerability_type, 0)
            vulnerabilities_by_type[vulnerability_type] += 1
            vulnerabilities_by_severity[status] += 1
    else:
        print("Nessuna vulnerabilità rilevata.")

    # Stampa le statistiche delle vulnerabilità
    print("Statistiche delle vulnerabilità:")
    print("Numero totale di vulnerabilità: ", total_vulnerabilities)
    print("Vulnerabilità per tipo:")
    for vulnerability_type, count in vulnerabilities_by_type.items():
        print(f"- {vulnerability_type}: {count}")
    print("Vulnerabilità per gravità:")
    for severity, count in vulnerabilities_by_severity.items():
        print(f"- {severity}: {count}")
    return  vulnerability_type, vulnerabilities_by_severity

def print_services(services):
    # Stampa i servizi del sito
    print("Servizi del sito:")
    for key, value in services.items():
        print(f"{key}: {value}")

def save_results_to_file(file_name, vulnerabilities, vulnerabilities_by_type, vulnerabilities_by_severity, services=None):
    # Salva i risultati su file
    with open(file_name, 'w') as file:
        file.write("Risultati della scansione delle vulnerabilità:\n")
        for port, status in vulnerabilities:
            file.write(f"Porta: {port}\n")
            file.write(f"Stato: {status}\n")
            file.write("------------------------------------------------------\n")

        file.write("Statistiche delle vulnerabilità:\n")
        file.write(f"Numero totale di vulnerabilità: {len(vulnerabilities)}\n")
        file.write("Vulnerabilità per tipo:\n")
        for vulnerability_type, count in vulnerabilities_by_type.items():
            file.write(f"- {vulnerability_type}: {count}\n")
        file.write("Vulnerabilità per gravità:\n")
        for severity, count in vulnerabilities_by_severity.items():
            file.write(f"- {severity}: {count}\n")

        if services:
            file.write("\nServizi del sito:\n")
            for key, value in services.items():
                file.write(f"{key}: {value}\n")

    print(f"Risultati salvati nel file '{file_name}'.")

def main():
    while True:
        vulnerabilities_by_type = {}
        vulnerabilities_by_severity = {
            'Open': 0,
            'Closed': 0,
            'Error': 0
        }
        url = input("Inserisci l'URL del sito da analizzare: ")
        truncated_url = truncate_url(url)
        port_range = input("Inserisci l'intervallo di porte da analizzare (es. 1-100): ")
        port_start, port_end = map(int, port_range.split('-'))
        ports = list(range(port_start, port_end + 1))

        vulnerabilities = run_scan(truncated_url, ports)
        vulnerabilities_by_type, vulnerabilities_by_severity = print_vulnerabilities(vulnerabilities)

        services = analyze_services(url)
        if services:
            print_services(services)

        # Opzione per salvare i risultati
        save_results = input("Vuoi salvare i risultati? (s/n): ")
        if save_results.lower() == 's':
            file_name = input("Inserisci il nome del file per salvare i risultati: ")
            save_results_to_file(file_name, vulnerabilities, vulnerabilities_by_type, vulnerabilities_by_severity, services)
            print("Risultati salvati.")

        # Opzione per avviare un'altra analisi
        repeat = input("Vuoi avviare un'altra analisi? (s/n): ")
        if repeat.lower() != 's':
            break

        # Pulisci la console
        print("\n" * 50)

if __name__ == '__main__':
    main()
