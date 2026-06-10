# Lab: Inconsistent security controls
url: https://portswigger.net/web-security/logic-flaws/examples/lab-logic-flaws-inconsistent-security-controls

# Overview:
This lab's flawed logic allow arbitrary user to access admin functionality that only be available to company staffs. Access admin panel and delete user carlos to solve lab

# Analysis:

First, register an account and log in.

In account manage page, there is an option to change email. We can change email to anything so change it to ...@dontwannaycry.com(prefix of staff's email)
-> Cracked
