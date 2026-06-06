# System Utility Tool

`system.py` is a Python script that provides a simple command-line interface for gathering system information, executing commands, and capturing screenshots.

## Features

- **Exfiltrate System Information**: Retrieves details about the operating system, CPU, and total RAM.
- **Exfiltrate User Data**: Retrieves the current username.
- **Exfiltrate Network Information**: Retrieves the local IP address and DNS servers from `/etc/resolv.conf`.
- **Execute Remote Command**: Allows executing shell commands directly and viewing their output.
- **Capture Screenshot**: Captures the current screen, saves it locally as `screenshot.png`, and generates a base64 encoded string of the image.

## Prerequisites

This script requires the `Pillow` library for screen capturing. You can install it using pip:

```bash
pip install Pillow
```

## Usage

Run the script using Python:

```bash
python system.py
```

You will be presented with an interactive menu. Enter the number corresponding to the action you want to perform and follow the prompts.

## Note

- **Security Warning**: The "Execute Remote Command" feature runs arbitrary commands via the shell. Ensure you understand the commands you are executing.
- **Cross-Platform Compatibility**: While some features might work across different operating systems, parts of this script (like reading `/etc/resolv.conf` and calculating RAM via `os.sysconf`) are specifically designed for Unix/Linux-like systems.
