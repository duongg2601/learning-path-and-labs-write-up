# Lab:
Password reset broken logic

# Overview
This lab's password reset functionality is vulnerable. To solve the lab, reset Carlos's password then log in and access his "My account" page.

Your credentials: wiener:peter
Victim's username: carlos

# Solve:
- Use our credential to get forgot password email, change the forgot password renew POST's username=carlos instead of wiener.
- The vulnerability is the lack of validate username in the reset password POST


