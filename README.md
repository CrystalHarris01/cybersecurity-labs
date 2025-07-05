# Cybersecurity Labs & Utilities 🛡️

A growing collection of Python-based tools and cybersecurity exercises built to demonstrate core concepts from network defense, threat detection, and security policy. Ideal for learners studying for CompTIA A+, Network+, and Security+ certifications or pursuing cybersecurity education through programs like WGU’s BSCSIA.

## 🔢 What's Included

- 🔍 **Network Scanner** – Scan IP ranges and identify open ports
- 🔐 **Password Strength Checker** – Detect weak or predictable passwords
- ✉️ **Phishing Email Analyzer** – Flag suspicious headers and links
- 📄 **Log Parser** – Identify anomalies in system logs
- 🧪 **Malware Simulation (Safe)** – Demonstrate common attack behavior (harmless)
- 📘 **Security Policy Template** – A basic policy for small orgs or personal use

## 📃 Project Structure

```
cybersecurity-labs/
├── README.md
├── LICENSE
├── network_scanner/
│   └── network_scanner.py
├── password_strength_checker/
│   └── checker.py
├── phishing_email_analyzer/
│   └── analyze_email.py
├── log_parser/
│   └── parse_logs.py
├── malware_simulation/
│   └── harmless_payload_demo.py
└── reports/
    └── security_policy_template.md
```

## 🔧 Getting Started

Clone the repo:
```bash
git clone https://github.com/yourusername/cybersecurity-labs.git
cd cybersecurity-labs
```

Run any tool:
```bash
cd network_scanner
python3 network_scanner.py
```

Each folder includes usage instructions and required libraries.

## 👤 Author
Crystal Harris  
Cybersecurity Student @ Western Governors University (BSCSIA)  
CompTIA A+ Certified | Pursuing Network+ & Security+  
WiCyS Target Challenge – Tier One Completer

[LinkedIn](#) | [WiCyS](https://www.wicys.org/) | [GitHub](#)

---

Stay tuned – this lab is evolving as I grow. Contributions and suggestions are welcome! ✨

---

## 🔍 network_scanner/network_scanner.py

```python
import socket
import ipaddress
from concurrent.futures import ThreadPoolExecutor

network = '192.168.1.0/24'
open_ports = []

def scan_target(ip, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(0.5)
            result = s.connect_ex((str(ip), port))
            if result == 0:
                open_ports.append((str(ip), port))
    except:
        pass

print(f"[*] Scanning network: {network}")
with ThreadPoolExecutor(max_workers=100) as executor:
    for ip in ipaddress.IPv4Network(network):
        for port in [22, 23, 80, 443, 3389]:
            executor.submit(scan_target, ip, port)

print("\n[*] Open Ports Found:")
for ip, port in open_ports:
    print(f"{ip}:{port}")
```

---

## 🔐 password_strength_checker/checker.py

```python
import re
import math

def password_entropy(password):
    charset = 0
    if re.search(r"[a-z]", password): charset += 26
    if re.search(r"[A-Z]", password): charset += 26
    if re.search(r"[0-9]", password): charset += 10
    if re.search(r"[^a-zA-Z0-9]", password): charset += 32
    entropy = len(password) * math.log2(charset) if charset else 0
    return round(entropy, 2)

pwd = input("Enter password to test: ")
entropy = password_entropy(pwd)
print(f"Entropy: {entropy} bits")
if entropy < 40:
    print("Weak password")
elif entropy < 60:
    print("Moderate password")
else:
    print("Strong password")
```

---

## ✉️ phishing_email_analyzer/analyze_email.py

```python
import email
import re
from email import policy
from email.parser import BytesParser

with open("sample_email.eml", "rb") as f:
    msg = BytesParser(policy=policy.default).parse(f)

print("\n[+] From:", msg["From"])
print("[+] Subject:", msg["Subject"])
print("[+] SPF/DKIM Failures (simulated):")
print("\t- SPF: FAIL")
print("\t- DKIM: FAIL")

print("\n[+] Suspicious Links:")
for match in re.findall(r"https?://[\w./-]+", msg.get_body(preferencelist=('plain')).get_content()):
    print("\t", match)
```

---

## 📄 log_parser/parse_logs.py

```python
import re

with open("auth.log", "r") as f:
    logs = f.readlines()

failures = {}
for line in logs:
    match = re.search(r"Failed password for (invalid user )?(\w+) from ([\d.]+)", line)
    if match:
        ip = match.group(3)
        failures[ip] = failures.get(ip, 0) + 1

print("\n[+] Potential Brute Force IPs:")
for ip, count in failures.items():
    if count > 5:
        print(f"{ip} - {count} failed attempts")
```

---

## 🧪 malware_simulation/harmless_payload_demo.py

```python
import base64

# Harmless simulation of a payload using base64 encoding
def simulate_payload():
    encoded = base64.b64encode(b"echo Simulated Attack Payload").decode("utf-8")
    print("Encoded Payload:", encoded)
    decoded = base64.b64decode(encoded).decode("utf-8")
    print("Decoded Action:", decoded)

simulate_payload()
```

---

## 📘 reports/security_policy_template.md

```markdown
# Sample Security Policy Template

## Purpose
To establish baseline security controls for protecting sensitive data and maintaining system integrity.

## Scope
Applies to all users, devices, and services within the organization.

## Key Policies
- Use of strong, unique passwords for all accounts
- Mandatory MFA for remote access
- Timely patching of operating systems and applications
- Regular security awareness training
- Incident reporting within 24 hours of detection
```

---

