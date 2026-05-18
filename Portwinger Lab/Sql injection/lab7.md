# Lab7: Blind SQL injection with conditional responses

# Overview:
-This lab contains a blind SQL injection vulnerability. The application uses a tracking cookie for analytics, and performs a SQL query containing the value of the submitted cookie.

-The results of the SQL query are not returned, and no error messages are displayed. But the application includes a Welcome back message in the page if the query returns any rows.

-The database contains a different table called users, with columns called username and password. You need to exploit the blind SQL injection vulnerability to find out the password of the administrator user.

-To solve the lab, log in as the administrator user.

# Solution:
+ The GET request header has Cookie: TrackingId
+ Add this syntax to this:
    ' AND SUBSTR((SELECT password FROM users WHERE username='administrator'),1,x) > 'a
+ The password contains lowercase alphabet and numbers
+ Use > < and = to check the correct one in order
+ increment x(x=1 first) every time we find the correct privious letter
+ There is a 'Welcome Back' response if the AND boolean in Cookie is true, we use this to determine whether the letters is right or wrong