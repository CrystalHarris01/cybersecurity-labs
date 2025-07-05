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
