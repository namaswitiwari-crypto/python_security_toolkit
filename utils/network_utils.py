import ipaddress
import re


def is_valid_ip(ip_address):
    """Return True when the supplied value is a valid IP address."""
    try:
        ipaddress.ip_address(ip_address)
        return True
    except ValueError:
        return False


def is_valid_mac(mac_address):
    """Return True when the supplied value is a valid MAC address."""
    pattern = r"^([0-9A-Fa-f]{2}:){5}[0-9A-Fa-f]{2}$"
    return bool(re.fullmatch(pattern, mac_address))