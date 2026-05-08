# H4sh — Python Port Scanner

<img width="300" height="200" alt="Preview" src="https://github.com/user-attachments/assets/f89fd5c4-a4c5-465e-97e5-cc6969dd67d4" />

A CLI port scanner with colorized output and scan persistence.

---

## Features

- Scan custom port range on any IP
- Scan top 100 common ports (with service/protocol labels)
- Auto-save results to `scans/scanned.json`
- Colorized output (green = open, red = closed)

---

## Requirements

- Python 3.x
- Dependencies:

```
colorama
requests
```

Install:

```bash
pip3 install -r requirements.txt
```

---

## Usage

```bash
python3 main.py
```

**Menu:**

```
1 - Scan by port range
2 - Scan top 100 common ports
```

**Range scan** prompts for IP, start port, end port.  
**Top 100 scan** prompts for IP, iterates `lib/top_100_common_ports.json`.

---

## File Structure

```
.
├── main.py
├── requirements.txt
├── lib/
│   └── top_100_common_ports.json
└── scans/
    └── scanned.json          # auto-created on first open port found
```

---


## License

MIT
