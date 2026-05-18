# Lab3: SQL injection UNION attack, determining the number of columns returned by the query
url: https://portswigger.net/web-security/sql-injection/union-attacks/lab-determine-number-of-columns

# Overview:
- This lab contains a SQL injection vulnerability in the product category filter. The results from the query are returned in the application's response, so you can use a UNION attack to retrieve data from other tables. The first step of such an attack is to determine the number of columns that are being returned by the query. You will then use this technique in subsequent labs to construct the full attack.

-To solve the lab, determine the number of columns returned by the query by performing a SQL injection UNION attack that returns an additional row containing null values.

# Solution:
1. ADD '+ORDER+BY+1-- to category param
increment 1 to 2,3,4...
    Internal Server Error appears in 4 so 3 is the actual number of columns
2. ADD '+UNION+SELECT+NULL--
       '+UNION+SELECT+NULL,NULL--
       ect
    Internal Server Error appears in every situation except the actual number of culumns is 3

