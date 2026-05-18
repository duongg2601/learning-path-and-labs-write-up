1. # OWASP - Open Worldwide Application Security Project
- non-profit and collaborative online community
- improve application security
- via a set of securiry principles, articles, documentation etc

2. # API - Application Programming Interface
# What is an API?
- API: middleware enabling communication between software components
- Uses requests and responses based on defined protocols
- Application: software with specific functionality
- Interface: contract that defines how system interact
- API documentation: explains request/response structure
- Role: fundamental building block for complex, enterprise-level applications

3. # Vulnerability I - Broken Object Level Authorisaion (BOLA)
# How does it happen?
- API endpoints are utilised for a common practise of retrieving and manipulating data
through object identifiers
- BOLA refers to Insecure Direct Object Reference (IDOR) - which creates a scenario where
the user uses the input functionality and gets access to the resources they are not 
authorised to access
- In an API, such controls are usually implemented through programming in Models 
(Model-View-Controller-Architecture) at the code level

# Mitigation Measures
- An authorisation mechanism that relies on user policies and hierarchies should be
adequately implemented
- Strict access controls methods to check if the logged-in user is authorised to perform
specific actions
- Promote using completely random values (strong encryption and decryption mechanism) for
nearly impossible-to-predict tokens

4. # Vulnerability II - Broken User Authentication (BUA)
# How does it happen?
- BUA reflects a scenario where an API endpoint allows an attacker to access a database
or acquire a higher privilege than the existing one
- Primary reason: 
    + invalid implementation of authentication (incorrect email/pw query)   
    + absence of security mechanisms (authorisation headers, tokens etc)

# Mitigation Measures
- Ensure complex passwords with higher entropy for end users
- Do not expose sensitive credentials in GET or POST requests
- Enable strong JSON Web Tokens (JWT), authorisation headers etc
- Ensure the implementation of multifactor authentication (where possible), account lockout, or a captcha system to mitigate brute force against particular users
- Ensure that passwords are not saved in plain text in the database to avoid further account takeover by the attacker

5. # Vulnerability III - Excessive Data Exposure
# How does it happen?
- Occurs when app tend to disclose more than desired infor to the user through an API response
- Web devs tend to expose all object properties without considering their sensitivity level
- Leave filtration task to the front-end dev before its displayed to the user
=> Attacker can intercept the response through the API and quickly extract the desired confidential data
- The runtime detection tools can give an  alert on this vulnerability. However, 
it cannot differentiate between legitimate data that is supposed to be returned or sensitive data

# Mitigation Measures
- Never leave sensitive data filtration tasks to the front-end dev
- Ensure time-to-time review of the response from the API to guarantee it returns only legitimate data and checks if it poses any security issue
- Avoid using generic methods sush as to_string() and to_json()
- Use API endpoint testing through various test cases and verify through automated and manual tests if the API leaks additional data

6. # Vulnerability IV - Lack of Resources & Rate Limiting
# How does it happen?
- It means that APIS do not enforce any restriction on the frequency of clients's requested resources or file's size
=> Which badly affects the API server performance and leads to the DoS(Denial of Service) or non-availability of service

# Mitigation Measures
- Ensure using a captcha to avoid requests form automated scripts and bots
- Ensure  implementation of a limit, i.e., how often a client can call an API within a specified time and notify instantly when the limit is exceeded
- Ensure to define the maximum data size on all parameters and payloads, i.e., max string length and max number of array elements

7. # Vulnerability V - Broken Function Level Authorisation
# How does it happen?
- A low privileged user bypasses system checks and gets access to confidential data by impersonating a high privileged user(admin)

# Mitigation Measures
- Ensure proper design and testing of all authorisation systems and deny all access by default
- Ensure that the operations are only allowed to the users belonging to the authorised group
- Make sure to review API endpoints against flaws regarding functional level authorisation and keep in mind the apps and group hierarchy's business logic

8. # Vulnerability VI - Mass Assignment
# How does it happen?
- where client-side data is automatically bound with server-side objects or class varibles
- However, hackers exploit the feature by first understanding the app's business logic and sending specially crafted data to the server, acquiring administrative access or inserting tampered data
-> Result in data tampering and privilege escalation from a regular user to an administrator

# Mitigation Measures
- Before using any framework, one must study how the backend insertions and updates are carried out
- Avoid using functions that bind an input from a client to code variables automatically
- Allowlist those properties only that need to get updated from the client side

9. # Vulnerability VII - Security Misconfiguration
# How does it happen?
- Implementation of incorrect and poorly configured security controls that put the security of the whole API at risk
- Factors:
    + improper/incomplete default configuration
    + publically accessible cloud storage
    + Cross-Origin Resource Sharing (CORS)
    + Error messages displayed with sensitive data
-> Intruder can take advance to perform detailed reconnaissance and get unauthorised access to the system

# Mitigation Measures
- Limit access to the administrative interfaces for authorised users and disable them for other users
- Disable default usernames and passwords for public-facing devices (routers, Web App Firewall etc.)
- Disable directory listing and set proper permissions for every file and folder
- Remove unnecessary pieces of code snippets, error logs etc. and turn off debugging while the code is in production

10. # Vulnerability VIII - Injection
# How does it happen?
- occurs when user input is not filtered and is directly processed by an API
-> enabling attacker to perform unintended API actions without authorisation
- An injection may come from:
    + SQL
    + OS commands
    + Extensible Markup Language (XML) etc.

# Likely Impact:
- Information disclosure, data loss, DoS, and complete account takeover
- Successful injection may also cause the intruders to access the sensitve data or even create new functionality and perform RCE

# Mitigation Measures:
- Ensure to use a well-known library for client-side input validation
- If a framework is not used, all client-provided data must be validated first and then filtered and sanitised
- Add necessary security rules to the WAF. Most of the time, injection flaws can be mitigated at the network level
- Make use of built-in filters in frameworks like Laravel, Code Ignitor etc., to validate and filter data

11. # Vulnerability IX - Improper Assets Management
# How does it happen?
- where wwe have two versions of an API available in our system. Everything is wholly switched to the new one, but the previous version has not been deleted yet
-> Plenty of other obsolete features of old version make it possible to find vulnerable scenarios

# Mitigation Measures
- Access to previouly developed sensitive and deprecated API calls must be blocked at the network level
- API developed for R&D, QA, prodution etc., must be segregated and hosted on separate servers
- Ensure documentation of all API aspects, including authentication, redirects, errors, CORS policy, and rate limit
- Adopt open standards to generate documentation automatically

12. # Vulnerability X - Insufficient Logging & Monitoring
# How does it happen?
- When try to track the hacker, there is not enough evidence available due to the absence of logging and monitoring mechanisms
- Only focus on infrastructure logging but lack API logging and monitoring
-> Lack infor like IP address, endpoints accessed, input data etc., along with timestamp, enables the identification of threat attack patterns
- Solution nowaday: Security Information and Event Management (SIEM)

# Mitigation Measures:
- Ensure use of SIEM system for log management
- Keep track of all denied accesses, failed authentication attempts, and input validation errors, using a format imported by SIEM and enough detail to identify the intruder
- Handle logs as sensitive data and ensure their integrity at rest and transit. Moreover, implement custom alerts to detect suspicious activities as well


