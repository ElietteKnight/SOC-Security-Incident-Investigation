from collections import Counter
import re

log_file = "logs/authentication-log.txt"

failed_attempts = Counter()
successful_logins = []

with open(log_file, "r") as file:
    for line in file:
        user_match = re.search(r"user=(\S+)", line)
        ip_match = re.search(r"src_ip=(\S+)", line)

        if not user_match or not ip_match:
            continue

        user = user_match.group(1)
        ip = ip_match.group(1)

        if "FAILED_LOGIN" in line:
            failed_attempts[(ip, user)] += 1

        elif "SUCCESSFUL_LOGIN" in line:
            successful_logins.append((ip, user))

print("=== Authentication Log Analysis ===")

for (ip, user), count in failed_attempts.items():
    print(f"\nSource IP: {ip}")
    print(f"Target User: {user}")
    print(f"Failed Attempts: {count}")

    if count >= 10:
        print("Alert: Potential brute-force activity detected")

        if (ip, user) in successful_logins:
            print("CRITICAL: Successful login occurred after repeated failures")
