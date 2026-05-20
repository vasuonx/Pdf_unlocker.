#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
PDF Password Unlocker Tool
For Termux (Android) - Pure Python Version
No CMake/C++ compilation needed!
Author: PDF Tool
"""

import os
import sys
import time

# ANSI Color Codes for Termux
colors = {
    'RED': '[1;31m',
    'GREEN': '[1;32m',
    'YELLOW': '[1;33m',
    'BLUE': '[1;34m',
    'MAGENTA': '[1;35m',
    'CYAN': '[1;36m',
    'WHITE': '[1;37m',
    'ORANGE': '[38;5;208m',
    'PINK': '[38;5;205m',
    'LIME': '[38;5;118m',
    'RESET': '[0m'
}

def banner():
    """Display colorful banner"""
    os.system('clear' if os.name != 'nt' else 'cls')

    # Colorful ASCII Banner with different colors for each line
    banner_lines = [
        ("⠀⠀⠀⠀⠀⠀⢀⠂⠀⢠⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⡀⠀⠱⡀⠀⠀⠀⠀⠀⠀", colors['RED']),
        ("⠀⠀⠀⠀⠀⣠⠏⠀⢠⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢷⡀⠀⢷⡀⠀⠀⠀⠀⠀", colors['ORANGE']),
        ("⠀⠀⠀⠀⢰⡟⠀⢀⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣧⠀⠀⣿⡄⠀⠀⠀⠀", colors['YELLOW']),
        ("⠀⠀⠀⢠⣿⠁⠀⣼⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⣇⠀⠘⣷⡀⠀⠀⠀", colors['GREEN']),
        ("⠀⠀⠀⣾⡇⠀⢰⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⡀⠀⢻⣇⠀⠀⠀", colors['CYAN']),
        ("⠀⠀⢰⣿⡇⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣇⠀⢸⣿⠀⠀⠀", colors['BLUE']),
        ("⠀⠀⣾⣿⠁⠀⠻⣿⡷⠶⠶⢶⠾⠿⣦⣀⣔⡆⡔⣤⣠⣾⠿⢶⠶⠶⠶⢿⡿⠛⠀⢸⣿⣇⠀⠀", colors['MAGENTA']),
        ("⠀⢠⣿⣿⣀⣀⣀⣤⣤⣶⠿⠿⠿⣶⣽⣿⣿⣿⣿⣿⣿⣷⡾⠿⠿⠷⣶⣤⣤⣀⣀⣸⣿⣿⡀⠀", colors['PINK']),
        ("⠀⠀⠻⢿⡿⠟⠋⠉⠁⢀⣴⣶⣶⣶⣿⣿⣿⣿⣿⣿⣿⣷⣶⣶⣶⣦⡀⠈⠉⠛⠻⣿⡿⠋⠀⠀", colors['LIME']),
        ("⠀⠀⠀⠀⠀⠀⠀⣀⣴⡿⠋⢁⣠⣾⠟⣿⣿⣿⣿⣿⣟⠿⣶⣄⠈⠻⣿⣦⡀⠀⠀⠀⠀⠀⠀⠀", colors['RED']),
        ("⠀⠀⠀⠀⢀⣠⣾⠟⠉⠀⣶⣿⡟⠁⢸⣿⣿⣿⣿⣿⣿⡆⠘⢿⣿⡆⠀⠙⠿⣶⣄⠀⠀⠀⠀⠀", colors['ORANGE']),
        ("⡀⢀⣠⣶⡿⠋⠁⠀⠀⠀⣿⣿⡇⠀⠸⣿⣿⣿⣿⣿⣿⠀⠀⢸⣿⣧⠀⠀⠀⠈⠻⢿⣦⣄⠀⡀", colors['YELLOW']),
        ("⣿⣿⡟⠉⠀⠀⠀⠀⠀⠀⣿⣿⡇⠀⠀⢿⣿⣿⣿⣿⡏⠀⠀⢸⣿⣿⠀⠀⠀⠀⠀⠀⠙⢿⣿⡟", colors['GREEN']),
        ("⢿⣿⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⡇⠀⠀⠸⣿⣿⣿⣿⠃⠀⠀⢸⣿⣿⠀⠀⠀⠀⠀⠀⠀⢸⣿⡇", colors['CYAN']),
        ("⢸⣿⡆⠀⠀⠀⠀⠀⠀⠀⣿⣿⡇⠀⠀⠀⢹⣿⣿⠇⠀⠀⠀⢸⣿⡏⠀⠀⠀⠀⠀⠀⠀⢸⣿⡇", colors['BLUE']),
        ("⠸⣿⡇⠀⠀⠀⠀⠀⠀⠀⣿⣿⡇⠀⠀⠀⠀⠋⠏⠀⠀⠀⠀⢸⣿⡇⠀⠀⠀⠀⠀⠀⠀⣿⣿⠁", colors['MAGENTA']),
        ("⠀⢿⣷⠀⠀⠀⠀⠀⠀⠀⢹⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⠇⠀⠀⠀⠀⠀⠀⠀⣿⡏⠀", colors['PINK']),
        ("⠀⠘⣿⠀⠀⠀⠀⠀⠀⠀⠘⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⠀⠀⠀⠀⠀⠀⠀⢠⣿⠁⠀", colors['LIME']),
        ("⠀⠀⢹⡇⠀⠀⠀⠀⠀⠀⠀⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⡏⠀⠀⠀⠀⠀⠀⠀⣾⠇⠀⠀", colors['RED']),
        ("⠀⠀⠈⢿⡀⠀⠀⠀⠀⠀⠀⢸⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠇⠀⠀⠀⠀⠀⠀⢰⡟⠀⠀⠀", colors['ORANGE']),
        ("⠀⠀⠀⠈⢇⠀⠀⠀⠀⠀⠀⠈⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⡟⠀⠀⠀⠀⠀⠀⠀⡜⠀⠀⠀⠀", colors['YELLOW']),
        ("⠀⠀⠀⠀⠈⢆⠀⠀⠀⠀⠀⠀⢸⣇⠀⠀⠀⠀⠀⠀⠀⠀⣾⠃⠀⠀⠀⠀⠀⠀⠜⠀⠀⠀⠀⠀", colors['GREEN']),
        ("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⡀⠀⠀⠀⠀⠀⠀⢠⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀", colors['CYAN']),
        ("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠳⡀⠀⠀⠀⠀⠠⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀", colors['BLUE']),
    ]

    print("\n")
    for line, color in banner_lines:
        print(f"{color}{line}{colors['RESET']}")

    # Tool name in center with rainbow effect
    title = "║      PDF PASSWORD UNLOCKER TOOL      ║"
    subtitle = "║         For Termux / Hari         ║"
    border = "════════════════════════════════════════"

    print(f"\n{colors['MAGENTA']}{border}{colors['RESET']}")
    print(f"{colors['YELLOW']}{title}{colors['RESET']}")
    print(f"{colors['CYAN']}{subtitle}{colors['RESET']}")
    print(f"{colors['MAGENTA']}{border}{colors['RESET']}")
    print(f"{colors['GREEN']}     [ Pure Python - No CMake Needed ]  {colors['RESET']}")
    print(f"{colors['MAGENTA']}{border}{colors['RESET']}\n")

def install_check():
    """Check and install required packages"""
    try:
        import pypdf
        return True
    except ImportError:
        print(f"{colors['RED']}[!] pypdf module not found!{colors['RESET']}")
        print(f"{colors['YELLOW']}[*] Installing pypdf (Pure Python - No compilation)...{colors['RESET']}")
        os.system("pip install pypdf")
        try:
            import pypdf
            return True
        except:
            return False

def unlock_pdf(input_file, password, output_file):
    """Remove password from PDF using pypdf"""
    try:
        from pypdf import PdfReader, PdfWriter

        print(f"{colors['CYAN']}[*] Opening encrypted PDF...{colors['RESET']}")
        reader = PdfReader(input_file)

        # Check if PDF is encrypted
        if not reader.is_encrypted:
            print(f"{colors['YELLOW']}[!] PDF is not password protected!{colors['RESET']}")
            print(f"{colors['YELLOW']}[!] Copying file without changes...{colors['RESET']}")
            writer = PdfWriter(clone_from=reader)
            writer.write(output_file)
            print(f"{colors['GREEN']}[✓] File copied to: {output_file}{colors['RESET']}")
            return True

        # Try to decrypt
        print(f"{colors['CYAN']}[*] Attempting to decrypt...{colors['RESET']}")
        result = reader.decrypt(password)

        if result == 0:
            print(f"{colors['RED']}[✗] Wrong password! Please try again.{colors['RESET']}")
            return False

        print(f"{colors['GREEN']}[✓] Password correct! Decrypting...{colors['RESET']}")

        # Create writer and clone decrypted content
        writer = PdfWriter(clone_from=reader)

        # Save without password
        writer.write(output_file)

        print(f"{colors['GREEN']}[✓] Password removed successfully!{colors['RESET']}")
        print(f"{colors['GREEN']}[✓] Saved as: {output_file}{colors['RESET']}")
        return True

    except FileNotFoundError:
        print(f"{colors['RED']}[✗] File not found: {input_file}{colors['RESET']}")
        return False
    except Exception as e:
        print(f"{colors['RED']}[✗] Error: {str(e)}{colors['RESET']}")
        return False

def main():
    banner()

    if not install_check():
        print(f"{colors['RED']}[✗] Failed to install pypdf. Please install manually:{colors['RESET']}")
        print(f"{colors['YELLOW']}    pip install pypdf{colors['RESET']}")
        sys.exit(1)

    print(f"{colors['GREEN']}[✓] All requirements satisfied!{colors['RESET']}\n")

    # Get input from user
    input_file = input(f"{colors['CYAN']}[?] Enter PDF file path: {colors['RESET']}").strip()

    if not os.path.exists(input_file):
        print(f"{colors['RED']}[✗] File does not exist!{colors['RESET']}")
        sys.exit(1)

    password = input(f"{colors['CYAN']}[?] Enter PDF password: {colors['RESET']}")

    # Generate output filename
    if input_file.lower().endswith('.pdf'):
        output_file = input_file[:-4] + "_unlocked.pdf"
    else:
        output_file = input_file + "_unlocked.pdf"

    print(f"\n{colors['YELLOW']}[*] Processing...{colors['RESET']}")
    time.sleep(1)

    success = unlock_pdf(input_file, password, output_file)

    if success:
        print(f"\n{colors['GREEN']}═══════════════════════════════════════════{colors['RESET']}")
        print(f"{colors['GREEN']}     PDF UNLOCKED SUCCESSFULLY! 🔓        {colors['RESET']}")
        print(f"{colors['GREEN']}═══════════════════════════════════════════{colors['RESET']}")
    else:
        print(f"\n{colors['RED']}═══════════════════════════════════════════{colors['RESET']}")
        print(f"{colors['RED']}     FAILED TO UNLOCK PDF! ✗              {colors['RESET']}")
        print(f"{colors['RED']}═══════════════════════════════════════════{colors['RESET']}")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{colors['RED']}\n[!] Exiting...{colors['RESET']}")
        sys.exit(0)
