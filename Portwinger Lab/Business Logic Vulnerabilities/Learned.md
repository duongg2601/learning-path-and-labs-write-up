# What are business logic vuls
- Definition: Business logic vulnerabilities are flaws in the design and implementation of an application that allow attackers to elicit unintended bahavior
- Logic flaws are often invisible to people who aren't explicitly looking for them as they typically won't be exposed by normal use of the app. However, an attacker may be able to exploit behavior quirks by interacting with the app in ways that devs never intended

# Examples of Business Logic Vuls
1. Excessive trust in client-side controls
- Client-side validation can be bypassed by web proxy
- Never trust user input received from the client
- Always perform validation and integrity checks on the server side
-> Lack of server-side validation can lead to serious security vuls and business impact.
<lab1>

2. Failing to handle unconventional input
- High-level logic vul<lab2>
- Low-level logic flaw<lab3>
- Inconsistent handling of exceptional input<lab4>

# Making flawed assumptions about user behavior
- This can lead to a wide range of issues where devs have not considered potentially dangerous scenarios that violate these assumptions.

1. Trusted users won't always remain trustworthy
- Some apps make mistake of assuming robust measures, having passed strict controls initially, the user and their data can be trusted indefinitely
-> Relatively lax enforcement of the same controls from that point on.
- If business rules and security measures are not applied consistently throughout the app, this can lead to potentially dangerous loopholes that may be exploited by an attacker.
<lab5-Inconsistent_security_controls>