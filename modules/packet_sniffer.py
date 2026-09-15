import scapy.all as scapy


def packet_callback(packet):
    """Display basic information about captured packets."""

    if packet.haslayer(scapy.IP):
        source = packet[scapy.IP].src
        destination = packet[scapy.IP].dst
        protocol = packet[scapy.IP].proto

        print(
            f"[PACKET] {source} -> {destination} | "
            f"Protocol: {protocol}"
        )
    else:
        print("[PACKET] Non-IP packet captured")


def start_sniffer(interface, packet_count=10):
    """
    Capture a limited number of packets on an authorized interface.

    A limited packet count keeps the classroom demonstration manageable.
    """

    if not interface:
        print("[-] Interface cannot be empty.")
        return

    try:
        packet_count = int(packet_count)

        if packet_count <= 0:
            print("[-] Packet count must be greater than 0.")
            return

        print(f"\n[+] Starting packet capture on: {interface}")
        print(f"[+] Capturing {packet_count} packets...")
        print("[!] Use only on an interface you are authorized to monitor.\n")

        scapy.sniff(
            iface=interface,
            count=packet_count,
            prn=packet_callback,
            store=False
        )

        print("\n[+] Packet capture completed.")

    except ValueError:
        print("[-] Packet count must be a number.")

    except PermissionError:
        print("[-] Permission denied.")
        print("[!] Appropriate privileges may be required.")

    except Exception as error:
        print(f"[-] Sniffer error: {error}")


def run():
    """Entry point used by the main toolkit."""

    print("\n--- Packet Sniffer ---")

    interface = input("Enter authorized interface: ").strip()
    packet_count = input("Enter number of packets to capture (default 10): ").strip()

    if not packet_count:
        packet_count = "10"

    start_sniffer(interface, packet_count)