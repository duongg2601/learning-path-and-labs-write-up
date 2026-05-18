# Introduction 
- Is defined as a weakness or flaw in the design, implementation or behaviours of a system or application
- Type of vulnerabilities:
    + Operating System              :   These types of vulnerabilities are found within Operating Systems (OSs) and often result in privilege escalation.
    + (Mis)Configuration-based      :   These types of vulnerability stem from an incorrectly configured application or service. For example, a website exposing customer details.
    + Weak or Default Credentials   :   Applications and services that have an element of authentication will come with default credentials when installed. For example, an administrator dashboard may have the username and password of "admin". These are easy to guess by an attacker. 
    + Application Logic             :   These vulnerabilities are a result of poorly designed applications. For example, poorly implemented authentication mechanisms that may result in an attacker being able to impersonate a user.
    + Human-Factor                  :   Human-Factor vulnerabilities are vulnerabilities that leverage human behaviour. For example, phishing emails are designed to trick humans into believing they are legitimate.

# Scoring Vulnerabilities (CVSS & VPR)
1. Common Vulnerability Scoring System (CVSS)
- score is determined by some of the following factors:
    + How easy is it to exploit the vul?
    + Do exploits exist for this?
    + How does this vul interface with the CIA triad?
- Advantages:
    + CVSS has been around for a long time
    + CVSS is popular in organisations
    + CVSS is a free framework to adopt and recommend by organisations such as NIST
- Disadvantages:
    + was never designed to help prioritise vulnerabilities, instead, just assign a value of severity
    + heavily assesses vuls on an exploit being available. However, only 20% of all have an exploit available
    + Vuls rarely change scoring after assessment despite the fact that new developments such as exploits may be found

2. Vulnerability Priority Rating (VPR)
-  Vulnerabilities are given a score with a heavy focus on the risk a vulnerability poses to the organisation itself, rather than factors such as impact (like with CVSS).
- Advantages:
    + VPR is a modern framework that is real-world
    + VPR considers over 150 factors when calculating risk
    + VPR is risk-driven and used by organisations to help prioritise patching vuls
    + Scorings are not final and are very dynamic, meaning the priority a vul should be given can change as the vul ages
- Disadvantages:
    + is not open-source like some other vul management frameworks
    + can only be adopted apart of a commercial platform
    + does not consider the CIA triad to the extent that CVSS does; meaning that risk to the confidentiality, integrity and availability of data does not play a large factor in scoring vuls when using VPR

# Vulnẻabilities Database
1. NVD - National Vulnerability Database
- is a website that lists all publically categorised vuls.
- vuls are classified under "Common Vuls and Exposures" (CVE for short)
- CVE format: CVE-YEAR_IDNUMBER

2. Exploit-DB
- more useful for hackers
- retains exploits for software and apps stored under the name, author and version of that