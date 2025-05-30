SIEM Log Analyzer 🛡️

A beginner-friendly Python project that simulates a basic Security Information and Event Management (SIEM) tool. It reads authentication logs and identifies suspicious login attempts based on repeated failures from the same IP address.

🔍 What It Does

- Reads a sample log file (`auth.log`)
- Detects failed login attempts
- Tracks and reports suspicious IP addresses
- Generates a text report with the findings

🧠 Why This Project?

This project is a simple way to learn:
- How log analysis works in cybersecurity
- How SOC teams detect brute force attacks
- Python basics like file handling, regex, and dictionaries

📁 Project Structure

siem-log-analyzer/
│
├── logs/
│ └── auth.log # Sample log file with login records
│
├── src/
│ └── analyzer.py # Main Python script
│
├── output/
│ └── report.txt # Output report with suspicious IPs
│
└── README.md # Project overview (this file)


## ▶️ How to Run It

1. Make sure Python is installed:
   ```bash
   python --version
2.Navigate to the src directory:
   ```bash
    cd src
```
3. Run the script:
   ```bash
   python analyzer.py
4. Check output/report.txt for the results.


