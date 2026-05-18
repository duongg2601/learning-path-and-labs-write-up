# Lab5: SQL injection UNION attack, retrieving data from other tables
url: https://portswigger.net/web-security/sql-injection/union-attacks/lab-retrieve-data-from-other-tables

# Overview:
-This lab contains a SQL injection vulnerability in the product category filter. The results from the query are returned in the application's response, so you can use a UNION attack to retrieve data from other tables. To construct such an attack, you need to combine some of the techniques you learned in previous labs.

-The database contains a different table called users, with columns called username and password.

-To solve the lab, perform a SQL injection UNION attack that retrieves all usernames and passwords, and use the information to log in as the administrator user.

# Solution:
- Use previous skill to figure our:
    + The actual number of columns
    + Which column has string data type
    + The diffirent table and its column(This skill is essential in practise but not mention here)
- Then use 'UNION SELECT username,password FROM users to list the credential we need to access the admin account