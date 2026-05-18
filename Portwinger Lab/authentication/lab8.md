# Lab: Broken brute-force protection, multiple credentials per request
url: https://portswigger.net/web-security/authentication/password-based/lab-broken-brute-force-protection-multiple-credentials-per-request

# Overview:
This lab is vulnerable due to a logic flaw in its brute-force protection. To solve the lab, brute-force Carlos's password, then access his account page. 

# Info:
- Victim's username: carlos
- candidate passwords list

# Analysis:
- After few tries to log in with carlos username, It seems that our username's IP has been blocked because of logging fail too many times in a certain time(user rate limit)

# Searching for "Guessing multiple credentials per request

- There are kinds of that showed below:
    + Param duplication: 
        username=carlos&password=123&password=456&password=789
    + JSON array:
        {
            "username": "carlos",
            "password": ["123", "456", "789"]
        }
    + Many objects:
        [
            {"username":"carlos","password":"123"},
            {"username":"carlos","password":"456"}
        ]
    + Delimiter-based:
        username=carlos&password=123,456,789

# Try:
- We should try the 2nd method since its more likely our request
- In this lab we dont need to find the exactly password, just concatenate all the candidate password in one request and successfully access