# Keylogger.py

⚠️ Legal & Ethical Notice

This project is strictly for educational and authorized penetration testing purposes only.
Do NOT use this tool on systems you do not own or do not have explicit written permission to test.
Misuse of this software may violate local, national, or international laws.

📌 Overview

KeyloggerX is a lightweight Python-based keylogger designed to demonstrate input capturing techniques commonly used in offensive security assessments.
The tool logs keystrokes in real time and stores them securely in a local file for further analysis during red team engagements or malware research training.

✨ Features

📝 Real-time keystroke logging

💾 Local secure log storage

🔒 Minimal footprint & simple code structure

🖥️ Cross-platform (Windows, Linux, macOS)

🧪 Perfect for demonstrating how keylogging attacks work

🛠️ Requirements

Python 3.x

pynput library

pip install pynput

🚀 Usage

Run the script with:

python3 keylogger.py


The logs will be saved automatically in a file (you can rename it or configure the path inside the script).

📂 Project Structure
├── keylogger.py      # Main script
└── logs.txt          # Output file (optional / auto-generated)

🔍 Educational Purpose

This repository is part of my cybersecurity learning path, focusing on:

Malware development basics

Understanding attack vectors

Practicing detection and defense strategies

Demonstrating offensive security knowledge in a controlled environment

🛡️ Disclaimer

The author is not responsible for any damage caused by improper use of this tool.
Always follow ethical hacking principles.
