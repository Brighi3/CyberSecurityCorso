import socket


def service_scan(target_ip, start_port, end_port):
    for port in range(start_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)  # Imposta il timeout della connessione a 1 secondo

        result = sock.connect_ex((target_ip, port))
        if result == 0:
            try:
                service = socket.getservbyport(port)
                print(f"Port {port} is open - Service: {service}")
            except socket.error:
                print(f"Port {port} is open - Service: Unknown")
        sock.close()


# Esempio di utilizzo
target_ip = ""  # Indirizzo IP del target
start_port = 1  # Porta di partenza della scansione
end_port = 100  # Porta di fine della scansione

service_scan(target_ip, start_port, end_port)