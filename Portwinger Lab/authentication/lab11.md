# Lab: Brute-forcing a stay-logged-in cookie
url: https://portswigger.net/web-security/authentication/other-mechanisms/lab-brute-forcing-a-stay-logged-in-cookie

# Overview:
This lab allows users to stay logged in even after they close their browser session. The cookie used to provide this functionality is vulnerable to brute-forcing.

To solve the lab, brute-force Carlos's cookie to gain access to his My account page.

    Your credentials: wiener:peter
    Victim's username: carlos
    Candidate passwords

# Analysis:
- First, access the credentials to examine the stay-log-in cookie
- Base64 decode let us know the prefix is wiener: 
- Use hashcat to the rest string and figure out its used MD5 hash

# Solve:
- Log out, use the GET /my-account?id=wiener, only when we use the valid stay-log-in cookie then the status-code=200, other is 302
- Use intruder to brute force attack, payload is stay-log-in cookie. 
- Change id=carlos instead
- Add
    + Hash: MD5
    + Add Prefix: carlos:
    + Base64-encode
to the payload processing

# Learned:
- How to use payload processing option
- A static cookie is the vulnerable in this lab, even if its encoded or hashed.