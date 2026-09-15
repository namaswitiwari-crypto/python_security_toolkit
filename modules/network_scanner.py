import scapy.all as scapy


def scan_network(target):
    """
    Scan an authorized local network/range using ARP
    and return discovered IP and MAC addresses.
    """

    if not target:
        print("[-] Target cannot be empty.")
        return

    print(f"\n[+] Scanning authorized target: {target}")
    print("[+] Please wait...\n")

    try:
        arp_request = scapy.ARP(pdst=target)
        broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
        arp_request_broadcast = broadcast / arp_request

        answered, unanswered = scapy.srp(
            arp_request_broadcast,
            timeout=2,
            verbose=False
        )

        if not answered:
            print("[-] No devices were discovered.")
            return

        print("IP Address\t\tMAC Address")
        print("-" * 45)

        for sent, received in answered:
            print(f"{received.psrc}\t\t{received.hwsrc}")

    except PermissionError:
        print("[-] Permission denied. Try running VS Code with appropriate privileges.")
    except Exception as error:
        print(f"[-] Scanner error: {error}")


def run():
    print("\n--- Network Scanner ---")
    target = input("Enter authorized IP/range (example: 192.168.1.0/24): ").strip()

    if not target:
        print("[-] Please enter a target IP or range.")
        return

    scan_network(target)