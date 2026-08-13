# Brute-Force Detection Rule

## Detection Objective

Identify potential brute-force authentication attacks by detecting a high number of failed login attempts from the same source IP address within a short period of time.

## Detection Logic

Generate an alert when:

- 10 or more failed login attempts occur
- From the same source IP address
- Against the same user account
- Within a 5-minute period

## Example Detection Condition

IF:

Failed Login Attempts >= 10

AND

Source IP = Same IP Address

AND

Target User = Same Account

AND

Time Window <= 5 Minutes

THEN:

Generate a Potential Brute-Force Attack Alert.

## Example Alert

Alert Name: Possible Brute-Force Authentication Attack

Severity: High

Source IP: 185.220.101.45

Target Account: admin

Failed Attempts: 10+

Recommended Action: Investigate authentication logs and determine whether unauthorized access occurred.

## Analyst Notes

A high number of failed login attempts does not automatically confirm malicious activity.

Possible legitimate causes may include:

- Forgotten passwords
- Misconfigured applications
- Expired credentials
- Automated services using outdated passwords

Analysts should review additional evidence before confirming an incident.
