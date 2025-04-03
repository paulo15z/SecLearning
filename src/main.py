from scapy.all import sniff, IP 
import winsound
import os

#puxar a lista de https://github.com/stamparm/ipsum

def load_blacklist(filename):
    try:
        with open(filename, "r") as file:
            return set(line.strip() for line in file if line.strip())
    except FileNotFoundError:
        print("Erro: Arquivo de BlackList não encontrado")
        return set()

base_dir = os.path.dirname(os.path.abspath(__file__))
lista_path = os.path.join(base_dir, "lista.txt")

malicious_ips = load_blacklist(lista_path)

def check_packet(packet):
    print(packet.summary()) #mostra os pacotes sendo lidos
    if IP in packet:
        src_ip = packet[IP].src #source
        dst_ip = packet[IP].dst #destiny

        if src_ip in malicious_ips or dst_ip in malicious_ips:
            print(f"ALERTA! Tráfego detectado de/para IP malicioso: {src_ip} -> {dst_ip}")
            winsound.Beep(1000, 500) #ALARME

#INICIA A CAPTURA
print("Monitorando >///< ... ")
sniff(filter="ip", prn=check_packet, store=False, iface="eth0", promisc=True)
