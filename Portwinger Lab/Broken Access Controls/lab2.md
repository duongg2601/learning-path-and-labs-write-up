# Lab: Unprotected admin functionality with unpredictable URL
url: https://portswigger.net/web-security/access-control/lab-unprotected-admin-functionality-with-unpredictable-url

# Overview:
- Unprotected admin panel located at an unpredictable location, but the location is disclosed somewhere in the app
- Access admin panel and delete user carlos to solve lab

# Analysis:

Admin panel location is disclosed in source code of login page:

![alt text](lab2.png)