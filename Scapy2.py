from scapy.all import sniff
from scapy.layers.inet import IP


# Funzione di callback chiamata per ogni pacchetto catturato
def packet_callback(packet):
    if packet.haslayer(IP):
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        print(f"Packet: {src_ip} -> {dst_ip}")


# Avvia lo sniffing di rete sulla tua interfaccia di rete
sniff(filter="ip", prn=packet_callback, count=10)