# Lab: Weak isolation on dual-use endpoint
url: https://portswigger.net/web-security/logic-flaws/examples/lab-logic-flaws-weak-isolation-on-dual-use-endpoint

# Overview:
- Flawed assumption about the user's privilege level based on their input
-> Exploit the logic oof its account management features to gain access
- Access administrator account and delete user carlos to solve lab
- Credentials: wiener-peter

# Analysis:

First log in wiener account

I tried to examine the change password function, try to remove each parameter

Origin param:
    csrf=Nv9GZPH9b7hb1C2jYxka5CBAzgdUXdXW&username=wiener&curren-password=peter&new-password-1=123&new-password-2=123

- Try remove csrf, <No>: need csrf token
             username <No>: incorrect current password
             current <Yes>: when I remove current password, we can change new password without submitting correct current password

-> Modify username to administrator and whatever new password we want and exploit.

# Learne:
First time, I only tried to remove the parameter but not the field name so it didn't work.
-> The server response this two cases diffirently
