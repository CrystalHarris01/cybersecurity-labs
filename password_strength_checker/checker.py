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
