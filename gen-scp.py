#!/usr/bin/env python3

import os
import sys
import getpass

def get_public_ip():
    # Use a service like ifconfig.me to get the public IP
    try:
        ip = os.popen('curl ifconfig.me 2>/dev/null').read().strip()
        return ip
    except Exception as e:
        print(f"Error fetching public IP: {e}")
        return None

def get_absolute_path():
    # Assuming you want the absolute path of the current directory
    try:
        absolute_path = os.path.abspath(sys.argv[1])
        return absolute_path
    except Exception as e:
        print(f"Error getting absolute path: {e}")
        return None

def generate_scp_command(username, public_ip, absolute_path):
    return f"scp {username}@{public_ip}:{absolute_path} ."

if __name__ == "__main__":
    username = getpass.getuser()  # Get the current username
    public_ip = get_public_ip()
    absolute_path = get_absolute_path()

    if not public_ip or not absolute_path:
        print("Failed to get necessary information. Exiting.")
        sys.exit(1)

    scp_command = generate_scp_command(username, public_ip, absolute_path)
    print(scp_command)