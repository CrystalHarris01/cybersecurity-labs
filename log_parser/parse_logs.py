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
