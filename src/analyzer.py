# Importing tools
import re  # Regular expressions (to find patterns in text)
from collections import defaultdict  # Dictionary to store IP counts

# Set the path to the log file and the output report
log_file = "../logs/auth.log"
output_file = "../output/report.txt"

# Pattern to find "Failed password" lines and extract the IP address
pattern = r"Failed password.*from (\d+\.\d+\.\d+\.\d+)"

# This dictionary will count how many times each IP fails
ip_failures = defaultdict(int)

# Read the log file
with open(log_file, "r") as f:
    lines = f.readlines()

# Go through each line and find failed attempts
for line in lines:
    match = re.search(pattern, line)
    if match:
        ip = match.group(1)
        ip_failures[ip] += 1

# Create the report
with open(output_file, "w") as f:
    f.write("Suspicious Login Attempts:\n\n")
    for ip, count in ip_failures.items():
        if count >= 2:  # If the IP failed more than once, report it
            f.write(f"IP {ip} has {count} failed login attempts.\n")

print("Analysis complete. Check the 'output/report.txt' file.")
