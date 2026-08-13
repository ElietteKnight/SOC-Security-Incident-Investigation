# SOC Security Incident Investigation

## Project Overview

This project demonstrates a simulated Security Operations Center (SOC) investigation of suspicious authentication activity.

The goal of this project is to practice identifying potential cyber threats, analyzing security logs, documenting indicators of compromise, determining incident severity, and recommending remediation steps.

## Scenario

A SOC analyst receives an alert showing multiple failed login attempts against an administrator account followed by a successful login.

The activity may indicate a brute-force attack or compromised credentials.

## Skills Demonstrated

- Security log analysis
- Incident investigation
- Brute-force attack detection
- Identification of Indicators of Compromise (IOCs)
- Incident severity classification
- Security remediation
- SOC documentation
- Threat analysis

## Investigation

During the investigation, authentication logs will be reviewed to determine:

- Which account was targeted
- How many failed login attempts occurred
- The source IP address
- Whether a successful login occurred
- Whether the activity appears malicious

## Incident Details

Target Account: admin

Source IP: 185.220.101.45

Failed Login Attempts: 27

Successful Login: Yes

Time Period: 8 minutes

## Initial Assessment

The repeated failed login attempts followed by a successful authentication may indicate a brute-force or password-guessing attack.

Severity: High

## Indicators of Compromise

- 185.220.101.45
- 27 failed authentication attempts
- Successful administrator login
- High number of login attempts within a short period

## Recommended Remediation

- Temporarily disable or lock the affected account
- Reset the account password
- Verify MFA activity
- Block or investigate the suspicious IP address
- Review additional authentication logs
- Check for unauthorized system activity
- Review affected systems for persistence
- Escalate the incident if additional compromise is discovered

## Project Status

🟡 Investigation in progress
    Cybersecurity SOC analyst project focused on investigating suspicious login activity, brute-force attacks, incident response, and security remediation.
