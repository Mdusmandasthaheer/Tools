import random
import subprocess
import sys
import pyfiglet

maccloner= pyfiglet.figlet_format('Maccloner')
print(maccloner)
print("                               by usman")
company_macs = {
    "Apple": "00:03:93",
    "ASUS": "1c:1b:0d",
    "Belkin": "04:bd:88",
    "Cisco": "00:26:08",
    "D-Link": "90:94:e4",
    "Linksys": "00:14:bf",
    "Netgear": "00:26:f2",
    "TP-Link": "40:f2:01",
    "Huawei": "00:1e:10",
    "Lenovo": "0c:da:41",
    "LG": "00:1c:62",
    "Microsoft": "98:0c:82",
    "Motorola": "00:24:8c",
    "Nokia": "00:26:e1",
    "Samsung": "00:11:22",
    "Sony": "00:0d:93",
    "Xiaomi": "34:80:b3"
}

def print_usage():
    print("\nUsage: python MACCloner.py [-company] [-h]")
    print("Options:\n")
    print("  -company   print all the supported router company names")
    sys.exit()

def print_company_names():
    print("[+] Supported router companies:")
    for company_name in company_macs:
        print(f"- {company_name}")
    sys.exit()

if len(sys.argv) > 1:
    if "-h" in sys.argv:
        print_usage()
    elif "-company" in sys.argv:
        print_company_names()

interface = input("\n[+] Enter the network interface (e.g. wlan0) \n \n-> ")

print("\n# Supported router companies:")
for company_name in company_macs:
    print(f"- {company_name}")

company_name = input("\n[+] Enter the router company name (e.g. Netgear)\n \n -> ")

if company_name not in company_macs:
    print(f"Sorry, {company_name} is not a supported router company :(")
    exit()

company_mac_prefix = company_macs[company_name]
new_mac_suffix = ":".join([f"{random.randint(0x00, 0xff):02x}" for _ in range(3)])
new_mac = f"{company_mac_prefix}:{new_mac_suffix}"

print(f"\n[+] Cloning MAC for {interface} to  ","[",new_mac,"]")

subprocess.call(["ifconfig", interface, "down"])
subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
subprocess.call(["ifconfig", interface, "up"])

