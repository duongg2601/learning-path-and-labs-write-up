# Lab: 
Broken brute-force protection, IP block

# Overview: 
This lab is vulnerable due to a logic flaw in its password brute-force protection. To solve the lab, brute-force the victim's password, then log in and access their account page. 

# Info: 
- credential: wiener:peter
- victim's username: carlos

# Analysis:
- After few tests with credential wiener:peter, We got that two things: 
    + Server block us 1 mins after 3 failed log
    + It resets when we logged in

# Ideal: 
Log in with credential after each victim's try

# Solve:
- Make a new password list is a combination of possible pass of carlos and wiener's one(peter)
- Answer: correct password of carlos is 1234567

# Learned:
- This vulnerability is a kind of logic flaw
- Keyword: Flawed brute-force protection
 + Locking the account that the remote user is trying to access if they make too many failed login attempts
 + Blocking the remote user's IP address if they make too many login attempts in quick succession
