# Network Mapper  

Network Mapper is a Python-based tool designed to gather information about target machines. This project includes functionalities like firewall detection, OS fingerprinting, port scanning, traceroute, and more, making it a powerful tool for ethical hacking and cybersecurity enthusiasts.  

## Features  
- 🔥 Firewall Detection  
- 🌐 Domain and DNS Enumeration  
- 🖥️ OS Detection  
- ⚙️ Service Version Detection  
- 🚦 Traceroute  
- 🔎 WHOIS Lookup  
- 🛠️ Port Scanning  

## Requirements  
To use the Network Mapper, you’ll need to install the following packages:  
- **nmap**: For OS fingerprinting, port scanning, traceroute, and service version detection.  
- **python-nmap**: A Python wrapper for Nmap.  
- **dnspython**: For DNS lookups and DNS enumeration.  
- **whois**: For WHOIS information retrieval.  
- **requests**: For HTTP header analysis, SSL certificate retrieval, etc.  
- **scapy**: For ARP scans and ping sweeps.  

## Installation  
Follow these steps to install the required packages:  

```bash
pip install python-nmap dnspython python-whois requests scapy asyncio pyopenssl

```
## How Run Project ->

1. Clone the repository:
```bash
git clone https://github.com/amitkumar9297/network-mapper.git
```

2. Navigate to the project directory:
```bash
cd network-mapper
```

3. Run the script:
```bash
python network_mapper.py
```
