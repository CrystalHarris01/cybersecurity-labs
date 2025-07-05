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
