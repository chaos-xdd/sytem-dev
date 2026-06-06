import os
import platform
import getpass
import socket
import subprocess
import time
import base64
import io
from PIL import ImageGrab

def exfiltrate_system_info():
    system_info = {
        "OS": platform.system(),
        "CPU": platform.processor(),
        "RAM": os.sysconf("SC_PHYS_PAGES") * os.sysconf("SC_PAGE_SIZE"),
    }
    return system_info

def exfiltrate_user_data():
    user_data = {
        "Username": getpass.getuser(),
        "Password": "Not implemented (for security reasons)",
    }
    return user_data
def exfiltrate_network_info():
    dns_servers = []
    try:
        with open("/etc/resolv.conf", "r") as f:
            for line in f:
                if line.strip().startswith("nameserver"):
                    dns_servers.append(line.strip().split()[1])
    except FileNotFoundError:
        dns_servers = ["Could not read /etc/resolv.conf"]
    network_info = {
        "IP Address": socket.gethostbyname(socket.gethostname()),
        "DNS Servers": dns_servers,
    }
    return network_info

def execute_remote_command(command):
    try:
        output = subprocess.check_output(command, shell=True)
        return output.decode("utf-8")
    except subprocess.CalledProcessError as e:
        return f"Error: {e}"

def capture_screenshot():
    try:
        img = ImageGrab.grab()
    except Exception as e:
        print(f"Screenshot failed: {e}")
        return None
    img.save("screenshot.png")
    # Encode screenshot as base64 for exfiltration
    buffer = io.BytesIO()
    img.save(buffer, format="PNG")
    encoded = base64.b64encode(buffer.getvalue()).decode("utf-8")
    return encoded

def main():
    while True:
        print("1. Exfiltrate System Information")
        print("2. Exfiltrate User Data")
        print("3. Exfiltrate Network Information")
        print("4. Execute Remote Command")
        print("5. Capture Screenshot")
        print("6. Quit")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            system_info = exfiltrate_system_info()
            print("System Information:")
            for key, value in system_info.items():
                print(f"{key}: {value}")
        elif choice == "2":
            user_data = exfiltrate_user_data()
            print("User Data:")
            for key, value in user_data.items():
                print(f"{key}: {value}")
        elif choice == "3":
            network_info = exfiltrate_network_info()
            print("Network Information:")
            for key, value in network_info.items():
                print(f"{key}: {value}")
        elif choice == "4":
            command = input("Enter a command: ")
            output = execute_remote_command(command)
            print("Output:")
            print(output)
        elif choice == "5":
            screenshot_data = capture_screenshot()
            if screenshot_data:
                print("Screenshot saved as screenshot.png")
                print(f"Base64 encoded data ({len(screenshot_data)} chars) ready for exfiltration.")
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    main()