# Brute-Force Attack Investigation

## Incident Summary

A review of authentication logs identified repeated failed login attempts against the `admin` account from the same source IP address.

The activity was followed by a successful login, which may indicate that the account credentials were successfully guessed or compromised.

## Evidence Reviewed

Log file:

`logs/authentication-log.txt`

## Key Findings

- Targeted account: `admin`
- Source IP address: `185.220.101.45`
- Failed login attempts: 27
- Successful login: Yes
- Approximate activity window: 8 minutes
- Attack pattern: Multiple failed authentication attempts followed by successful authentication

## Analyst Assessment

The repeated login failures from a single source IP within a short period are consistent with possible password-guessing or brute-force activity.

The successful login occurring after the failed attempts increases the severity of the incident because it suggests the attacker may have successfully accessed the administrator account.

## Severity

**High**

## Indicators of Compromise

- Suspicious IP: `185.220.101.45`
- Target account: `admin`
- 27 failed authentication attempts
- Successful authentication after repeated failures
- High-frequency authentication activity

## Recommended Response Actions

1. Temporarily disable or lock the affected administrator account.
2. Reset the administrator password.
3. Review MFA logs and authentication methods.
4. Investigate or block the suspicious source IP.
5. Review system activity after the successful login.
6. Search for additional login attempts involving other accounts.
7. Review endpoint and network logs for additional suspicious behavior.
8. Escalate the incident if evidence of unauthorized access is discovered.

## Conclusion

The authentication pattern presents a strong indication of suspicious login activity and should be investigated as a potential account compromise.

Further analysis would be required to determine whether the successful login resulted in unauthorized system access.
