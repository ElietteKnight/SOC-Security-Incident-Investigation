# Splunk Brute-Force Detection Query

## Purpose

This query demonstrates how a SOC analyst could identify repeated failed login attempts using Splunk.

## Example SPL Query

```spl
index=authentication "FAILED_LOGIN"
| rex "user=(?<user>\S+)"
| rex "src_ip=(?<src_ip>\S+)"
| stats count as failed_attempts by src_ip user
| where failed_attempts >= 10
| sort - failed_attempts
