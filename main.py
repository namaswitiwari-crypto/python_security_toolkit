from modules.network_scanner import run as run_network_scanner
from modules.mac_changer import run as run_mac_changer
from modules.arp_spoofer import run as run_arp_spoofer
from modules.packet_sniffer import run as run_packet_sniffer
from modules.network_jammer import run as run_network_jammer
from modules.dns_spoofer import run as run_dns_spoofer
from modules.arp_spoof_detector import run as run_arp_spoof_detector


def show_banner():
    print("\n" + "=" * 60)
    print("         PYTHON SECURITY TOOLKIT")
    print("       Integrated Ethical Hacking Framework")
    print("=" * 60)
    print("Use this toolkit only in an authorized lab environment.")
    print("=" * 60)


def show_menu():
    print("\nChoose a module:")
    print("1. MAC Changer")
    print("2. Network Scanner")
    print("3. ARP Spoofer")
    print("4. Packet Sniffer")
    print("5. Network Jammer")
    print("6. DNS Spoofer")
    print("7. ARP Spoof Detector")
    print("0. Exit")


def run_toolkit():
    show_banner()

    while True:
        show_menu()

        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            run_mac_changer()

        elif choice == "2":
            run_network_scanner()

        elif choice == "3":
            run_arp_spoofer()

        elif choice == "4":
            run_packet_sniffer()

        elif choice == "5":
            run_network_jammer()

        elif choice == "6":
            run_dns_spoofer()

        elif choice == "7":
            run_arp_spoof_detector()

        elif choice == "0":
            print("\n[+] Exiting Python Security Toolkit.")
            break

        else:
            print("\n[-] Invalid choice. Please enter a number from 0 to 7.")


if __name__ == "__main__":
    run_toolkit()