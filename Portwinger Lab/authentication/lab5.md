# Lab: 
Username enumeration via response timing

# Overview: 
Enumerate a valid username, brute-force this user's password

# Credetnial: 
wiener:peter

# Analysis: 
Server block our IP if we try to log in multiple times

# Solve:
- Append X-Forwarded-For: (number) to bypass Ip-based Defense.
- Test valid username: wiener with long password, We know the responsed time much longer than the invalid one
- Use pitchfork attack, first payload is X-Forwarded-For param, second is username to find the valid username
- Brute force attack when we have the valid username to find the password
- Access to the web with correct answer

# Answer: 
app1:moscow

# Learned:
- Use X-Forwarded-For in header if we are blocked by IP-based defense
- The responsed time of valid username is longer than that of invalid one (try with long password)