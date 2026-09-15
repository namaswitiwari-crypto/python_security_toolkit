import ipaddress


def is_valid_ip(ip_address):
    """Check whether the supplied value is a valid IPv4 address."""
    try:
        ipaddress.ip_address(ip_address)
        return True
    except ValueError:
        return False


def run_arp_spoof_demo():
    """
    Lab-only ARP spoofing demonstration.

    The classroom concept involves placing an authorized lab machine
    between a victim and gateway by manipulating ARP information.
    The active packet-sending portion is intentionally disabled here.
    """

    print("\n--- ARP Spoofing Demonstration ---")
    print("[!] AUTHORIZED LAB USE ONLY")
    print("[!] Active ARP manipulation is disabled in this toolkit build.")

    target_ip = input("Enter lab target IPv4 address: ").strip()
    gateway_ip = input("Enter lab gateway IPv4 address: ").strip()

    if not is_valid_ip(target_ip):
        print("[-] Invalid target IP address.")
        return

    if not is_valid_ip(gateway_ip):
        print("[-] Invalid gateway IP address.")
        return

    if target_ip == gateway_ip:
        print("[-] Target and gateway cannot be the same.")
        return

    print("\n[+] Input validation successful.")
    print(f"[+] Lab target   : {target_ip}")
    print(f"[+] Lab gateway  : {gateway_ip}")
    print("[+] Demonstration ready.")
    print("[!] No ARP packets were modified or sent.")


def run():
    """Entry point used by the main toolkit."""
    run_arp_spoof_demo()