# Lab:
Lab: 2FA bypass using a brute-force attack

# Overview:
This lab's two-factor authentication is vulnerable to brute-forcing. You have already obtained a valid username and password, but do not have access to the user's 2FA verification code. To solve the lab, brute-force the 2FA code and access Carlos's account page.

Victim's credentials: carlos:montoya 

Note: As the verification code will reset while you're running your attack, you may need to repeat this attack several times before you succeed. This is because the new code may be a number that your current Intruder attack has already attempted.

# Analysis:
- The 2FA has csrf token param, it will be changed after two failed verifying attempts.
- We need the cookie session to find a new csrf each failed attempt
- First, 
the 1st login cookie session
this request spawns a csrf(its uses for 1st login)
- Then we use two info above to login and receive a new cookie session used for 2nd verify
- We use this to the 2nd GET request and then recieve a 2nd csrf
- Use this to the 2nd POST

# Solve:
- We need to use session handling rule and macro, we macro the GET log, POST log and GET log2 every time we POST log2 to update the valid session cookie and csrf token
- Then use send POST log2 to intruder to brute force the mfa-code, make sure to set the max concurrent request to 1.

# Learning:
- In this lab, we have learned about session, csrf token to defense brute force attacking
- How to use session handling rule and macro

- But intruder run so slow, python request helps us to fasten this task more quickly. Source code in lab10.py
link here: https://medium.com/@anaselsaba123/portswigger-lab-write-up-2fa-bypass-using-a-brute-force-attack-69f41ef36168
(I dont know the code at all but will try to figure it out soon)