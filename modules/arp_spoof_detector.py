import scapy.all as scapy


def get_mac(ip_address):
    """Get the MAC address associated with an IP on the local network."""
    try:
        request = scapy.ARP(pdst=ip_address)
        broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
        arp_request_broadcast = broadcast / request

        answered = scapy.srp(
            arp_request_broadcast,
            timeout=2,
            verbose=False
        )[0]

        if answered:
            return answered[0][1].hwsrc

        return None

    except Exception as error:
        print(f"[-] Could not resolve MAC address: {error}")
        return None


def check_arp_packet(packet):
    """Check an ARP reply for a possible IP/MAC mismatch."""

    if packet.haslayer(scapy.ARP) and packet[scapy.ARP].op == 2:
        source_ip = packet[scapy.ARP].psrc
        source_mac = packet[scapy.ARP].hwsrc

        original_mac = get_mac(source_ip)

        if original_mac and original_mac.lower() != source_mac.lower():
            print(
                f"[WARNING] Possible ARP inconsistency detected: "
                f"{source_ip} -> {source_mac}"
            )
        else:
            print(
                f"[OK] ARP mapping observed: "
                f"{source_ip} -> {source_mac}"
            )


def start_detector(interface, packet_count=10):
    """
    Monitor a limited number of ARP packets on an authorized interface.
    """

    if not interface:
        print("[-] Interface cannot be empty.")
        return

    try:
        packet_count = int(packet_count)

        if packet_count <= 0:
            print("[-] Packet count must be greater than 0.")
            return

        print(f"\n[+] Starting ARP spoof detector on: {interface}")
        print(f"[+] Monitoring {packet_count} ARP packets...")
        print("[!] Use only on an authorized network/interface.\n")

        captured = 0

        def process_packet(packet):
            nonlocal captured

            if packet.haslayer(scapy.ARP):
                check_arp_packet(packet)
                captured += 1

        scapy.sniff(
            iface=interface,
            store=False,
            prn=process_packet,
            stop_filter=lambda packet: captured >= packet_count
        )

        print("\n[+] ARP monitoring completed.")

    except ValueError:
        print("[-] Packet count must be a valid number.")

    except PermissionError:
        print("[-] Permission denied.")
        print("[!] Appropriate privileges may be required.")

    except Exception as error:
        print(f"[-] Detector error: {error}")


def run():
    """Entry point used by the main toolkit."""

    print("\n--- ARP Spoof Detector ---")

    interface = input("Enter authorized interface: ").strip()
    packet_count = input(
        "Enter number of ARP packets to monitor (default 10): "
    ).strip()

    if not packet_count:
        packet_count = "10"

    start_detector(interface, packet_count)