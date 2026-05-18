# Lab: 
2FA broken logic

# Overview:
This lab's two-factor authentication is vulnerable due to its flawed logic. To solve the lab, access Carlos's account page.
    + Your credentials: wiener:peter
    + Victim's username: carlos

# Solve:
- First, we use our credentials to access
- The server redirects us to the second factor authentication but we already logged in and just go to email page to get the verification code
- And then I add the code and change the verify username at cookie header but it failed to log in
- Now Im thinking about doing brute force the verify code (with turbo intruder)
- And it works

# Learned:
- I tried to use param duplication but i didnt work because the server only accept the last param
- So we need to brute force victim's verify code