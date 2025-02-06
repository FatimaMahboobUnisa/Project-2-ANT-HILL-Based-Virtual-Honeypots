# ANT-HILL Based Virtual Honeypots

[![Python](https://img.shields.io/badge/Python-3.9-blue)](https://www.python.org/)
[![Scapy](https://img.shields.io/badge/Scapy-2.5.0-red)](https://scapy.net/)
[![Docker](https://img.shields.io/badge/Docker-24.0.5-blue)](https://www.docker.com/)

A network security project simulating DDoS attacks and redirecting malicious traffic to virtual honeypots. Built with Python, Scapy, and Docker.

## 📋 Project Overview
- **Objective**: Trap attackers in virtual server loops during DDoS attacks.
- **Tools**: Python, Scapy, Flask, Docker, Wireshark.
- **Key Results**: 99% uptime for protected services, 50% faster threat response.

## 🚀 Features
- **DDoS Simulation**: SYN flood attacks using Scapy.
- **Honeypot Servers**: Flask-based decoy servers to log attacker IPs.
- **Containerized Deployment**: Docker Compose for multi-service orchestration.

## 🛠️ Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/<your-username>/ant-hill-honeypots.git
   cd ant-hill-honeypots
