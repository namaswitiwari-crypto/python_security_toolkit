import ipaddress


def is_valid_ip(ip_address):
    """Validate an IPv4 or IPv6 address."""
    try:
        ipaddress.ip_address(ip_address)
        return True
    except ValueError:
        return False


def run_dns_spoof_demo():
    """
    Safe demonstration of the DNS spoofing concept.

    The classroom version modifies DNS responses through
    NetfilterQueue. This integrated version does not modify
    live DNS traffic.
    """

    print("\n--- DNS Spoofer Demonstration ---")
    print("[!] AUTHORIZED LAB USE ONLY")
    print("[!] Live DNS-response manipulation is disabled.")

    target_domain = input(
        "Enter lab target domain (example: example.test): "
    ).strip()

    spoof_ip = input(
        "Enter demonstration IP address: "
    ).strip()

    if not target_domain:
        print("[-] Domain cannot be empty.")
        return

    if not is_valid_ip(spoof_ip):
        print("[-] Invalid IP address.")
        return

    print("\n[+] DNS demonstration inputs accepted.")
    print(f"[+] Target domain : {target_domain}")
    print(f"[+] Demo IP       : {spoof_ip}")
    print("[+] DNS spoofing concept ready for authorized lab discussion.")
    print("[!] No live DNS responses were modified.")


def run():
    """Entry point used by the main toolkit."""
    run_dns_spoof_demo()