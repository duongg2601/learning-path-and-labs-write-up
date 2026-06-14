# Vertical privilege escalation

1. Unprotected functionality
- Where an application does not enforce any protection for sensitive functionality
- Unprotected admin functionality <lab1>
- Unprotected admin functionality with unpredictable URL <lab2>

2. Parameter-based access control methods
- User role controlled by request parameter <lab3>
- User role can be modified in user profile <lab4>

3. Broken access control resulting from platform misconfiguration
- Some apps enforce access controls at the platform layer, restrict access to specific URLs and HTTP methods based on the user's role.
    Ex: DENY: POST, /admin/deleteUser, managers
- Some app frameworks support various non-standard HTTP headers that can be used to override the URL in the original request, such as X-Original-URL and X-Rewrite-URL.
- If a website uses rigorous front-end controls to restrict access based on the URL, but the application allows URL to be overriden via a request header, then it might be possible to bypass the access controls using a request like the following:
    POST / HTTP/1.1
    X-Original-URL: /admin/deleteUser
    ...
<lab5>

- Some websites tolerate different HTTP request methods when performing an action. If an attacker can use the GET(or another) method to perform actions on a restricted URL, they can bypass the access control that is implemented at the platform layer
<lab6>

4. Broken access control resulting from URL-matching discrepancies

# Horizontal privilege escalation
- Occurs if a user is able to gain access to resources belonging to another user, instead of their own resources of that type

# Horizontal to vertical privilege escalation
- A horizontal privilege escalation attack can be turned into a vertical one, by compromising a more privileged user(ex: admin user)

# IDOR
- A subcategory of access control vuls
- Occur if an app uses user-supplied input to access objects directly and an attacker con modify the input to obtain unauthorized access

# Access control vuls in multi-step processes
- Many websites implement important function over a series of steps:
    + A variety of inputs and actions need to be captured
    + The user needs to review and confirm details before the action is performed
- For example, the admin function to update user details might involve the following steps:
    + Load the form that contain details for a specific user
    + Submit the changes
    + Review the changes and confirm
- Sometimes, a website implement rigorous access controls over some of these steps, but ignore others.

# Referer-based access control
- Some websites base access controls on the Referer header submitted in the HTTP request. The Referer header can be added to requests by browsers to indicate which page intiated a request

# Location-based access control
- Some websites enforce controls based on the user's geographical location
- This access controls can often be circumvented by the use of web proxies, VPNs, or manipulation of client-side geolocation mechanisms

# How to prevent access control vuls
Principles:
    + Never rely on obfuscation alone for access control
    + Unless a resource is intended to be publicly accessible, deny access by default
    + Wherever possible, use a single application-wide mechanism for enforcing access controls
    + At the code level, make it mandatory for developers to declare the access that is allowed for each resource, and deny access by default
    + Thoroughly audit and test access controls to ensure they work as designed. 