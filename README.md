# DIRCHK - Directory Buster & Info Tool

DIRCHK is a command-line tool for directory busting and domain information retrieval. It identifies accessible directories on web servers and provides detailed WHOIS information for domains.

## Features

- **Directory Buster**: Tests for the existence of directories listed in a wordlist.
- **Domain Information**: Retrieves WHOIS details for the target domain.
- **IP Address Retrieval**: Fetches the IP address of the target domain.

## Requirements

- Python 3.11 or later
- `requests`
- `colorama`
- `python-whois`

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/yourrepository.git
   cd yourrepository
2. **Install The required Packages**
   ```bash
    pip install requests colorama python-whois

3. **USAGE**
   ```bash
    python DIRCHK.py <url> <wordlist>
# Output 
  ```bash
 ____  _     ____ _  __ _  __
 |  _ \| |   |  _ \ |/ _| |/ /
 | | | | |   | | | | | |_| '_ \
 | |_| | |___| |_| | |  _| (_) |
 |____/|_____|____/|_|_|  \___/

  DIRCHK - Directory Buster & Info Tool
  Made by Faizal Imam

[*] IP Address of example.com: 93.184.216.34
[*] WHOIS Information:
    Domain Name: example.com
    Registrar: Example Registrar
    Creation Date: 1995-08-22
    Expiry Date: 2025-08-21
    Name Servers: ns1.example.com, ns2.example.com
[*] Starting directory busting...
[+] Found: http://example.com/admin (Status: 200 OK)
[-] Not Found: http://example.com/private (Status: 404)
[*] Directory busting completed!

