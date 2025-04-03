from scapy.all import sniff, IP 

#puxar a lista de https://github.com/stamparm/ipsum

def load_blacklist(filename):
    try:
        with open(filename, "r") as file:
            return set(line.strip() for line in file if line.strip())
    except FileNotFoundError:
        print("Erro: Arquivo de BlackList não encontrado")
        return set()
    
blacklist = "lista.txt"
malicious_ips = load_blacklist(blacklist)

def check_packet(packet):
    print(packet.summary())
    if IP in packet:
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst

        if src_ip in malicious_ips or dst_ip in malicious_ips:
            print(f"ALERTA! Tráfego detectado de/para IP malicioso: {src_ip} -> {dst_ip}")

#INICIA A CAPTURA
sniff(filter="ip", prn=check_packet, store=False, iface="eth0")
