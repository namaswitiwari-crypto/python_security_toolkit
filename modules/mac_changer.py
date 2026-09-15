import subprocess
import re


def is_valid_mac(mac):
    """Validate a MAC address."""
    pattern = r"^([0-9A-Fa-f]{2}:){5}[0-9A-Fa-f]{2}$"
    return bool(re.match(pattern, mac))


def change_mac(interface, new_mac):
    """
    Change the MAC address of the selected network interface.
    Intended for an authorized lab environment.
    """

    if not interface:
        print("[-] Interface cannot be empty.")
        return

    if not is_valid_mac(new_mac):
        print("[-] Invalid MAC address format.")
        print("[!] Expected format: XX:XX:XX:XX:XX:XX")
        return

    print(f"\n[+] Attempting to change MAC address of: {interface}")

    try:
        subprocess.run(
            ["ifconfig", interface, "down"],
            check=True
        )

        subprocess.run(
            ["ifconfig", interface, "hw", "ether", new_mac],
            check=True
        )

        subprocess.run(
            ["ifconfig", interface, "up"],
            check=True
        )

        print(f"[+] MAC address changed successfully to {new_mac}")

    except FileNotFoundError:
        print("[-] 'ifconfig' was not found.")
        print("[!] This module is intended for a Linux/Kali environment.")

    except PermissionError:
        print("[-] Permission denied.")
        print("[!] Try running with appropriate privileges in your lab.")

    except subprocess.CalledProcessError as error:
        print(f"[-] MAC change command failed: {error}")

    except Exception as error:
        print(f"[-] Unexpected error: {error}")


def run():
    """Collect user input and run the MAC changer."""

    print("\n--- MAC Changer ---")
    print("[!] Use only on an interface you own or are authorized to test.")

    interface = input("Enter interface name: ").strip()
    new_mac = input("Enter new MAC address: ").strip()

    change_mac(interface, new_mac)