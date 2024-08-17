import argparse
import requests
import colorama
import socket
import whois
from colorama import Fore, Style

colorama.init(autoreset=True)

def print_banner():
    banner = f"""
{Fore.CYAN}{Style.BRIGHT}
  ____  _     ____ _  __ _  __
 |  _ \\| |   |  _ \\ |/ _| |/ /
 | | | | |   | | | | | |_| '_ \\
 | |_| | |___| |_| | |  _| (_) |
 |____/|_____|____/|_|_|  \\___/
 
  {Fore.YELLOW}{Style.BRIGHT}DIRCHK - Directory Buster & Info Tool
  {Fore.LIGHTBLACK_EX}Made by Faizal Imam
    """
    print(banner)

def get_ip_address(url):
    domain = url.replace('http://', '').replace('https://', '').split('/')[0]
    try:
        ip_address = socket.gethostbyname(domain)
        print(Fore.GREEN + f"[*] IP Address of {domain}: {ip_address}")
        return ip_address
    except socket.gaierror:
        print(Fore.RED + f"[!] Could not resolve IP address for {domain}")
        return None

def get_whois_info(domain):
    try:
        w = whois.whois(domain)
        print(Fore.GREEN + "[*] WHOIS Information:")
        print(Fore.LIGHTBLUE_EX + f"    Domain Name: {w.domain_name}")
        print(Fore.LIGHTBLUE_EX + f"    Registrar: {w.registrar}")
        print(Fore.LIGHTBLUE_EX + f"    Creation Date: {w.creation_date}")
        print(Fore.LIGHTBLUE_EX + f"    Expiry Date: {w.expiration_date}")
        print(Fore.LIGHTBLUE_EX + f"    Name Servers: {', '.join(w.name_servers)}")
    except Exception as e:
        print(Fore.RED + f"[!] Failed to retrieve WHOIS information: {e}")

def dir_buster(url, wordlist):
    with open(wordlist, 'r') as file:
        directories = file.read().splitlines()

    print(Fore.GREEN + Style.BRIGHT + "[*] Starting directory busting...")
    
    for directory in directories:
        target_url = f"{url}/{directory}"
        try:
            response = requests.get(target_url)
            if response.status_code == 200:
                print(Fore.LIGHTGREEN_EX + f"[+] Found: {target_url} (Status: 200 OK)")
            else:
                print(Fore.RED + f"[-] Not Found: {target_url} (Status: {response.status_code})")
        except requests.RequestException as e:
            print(Fore.YELLOW + f"[!] Error: {target_url} ({e})")
    
    print(Fore.GREEN + Style.BRIGHT + "[*] Directory busting completed!")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="DIRCHK - Directory Buster & Info Tool")
    parser.add_argument("url", help="Target URL (e.g., http://example.com)")
    parser.add_argument("wordlist", help="Path to the wordlist file")
    
    args = parser.parse_args()
    
    print_banner()
    
    domain = args.url.replace('http://', '').replace('https://', '').split('/')[0]
    get_ip_address(args.url)
    get_whois_info(domain)
    
    dir_buster(args.url, args.wordlist)
