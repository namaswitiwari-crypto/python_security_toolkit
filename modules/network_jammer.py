def run_jammer_demo():
    """
    Safe demonstration of the network-jammer concept.

    The classroom version uses NetfilterQueue to intercept packets.
    This integrated version does not modify, drop, or disrupt traffic.
    """

    print("\n--- Network Jammer Demonstration ---")
    print("[!] AUTHORIZED LAB USE ONLY")
    print("[!] Active traffic disruption is disabled.")

    interface = input("Enter lab interface name: ").strip()

    if not interface:
        print("[-] Interface name cannot be empty.")
        return

    print(f"\n[+] Lab interface selected: {interface}")
    print("[+] Demonstration mode initialized.")
    print("[+] Packet interception/queue handling concept acknowledged.")
    print("[!] No packets were dropped, modified, or blocked.")


def run():
    """Entry point used by the main toolkit."""
    run_jammer_demo()