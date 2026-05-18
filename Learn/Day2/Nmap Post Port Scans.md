# Service Detection
- option -sV: collect and determine service and version infor for the open ports
  control the intensity with --version-intensity LEVEL (0 is lightest and 9 is the most complete)
note: cannot discover the version without establishing a connection fully and communicating with the listening service
# OS Detection
- Nmap can detect the OS based on its behaviour and any telltale signs in its responses
- option used: -O
- --traceroute: to find the routers between you and the target

# Nmap Scripting Engine (NSE)
- --script=default or -sC
- Script Category:
    + auth      	Authentication related scripts
    + broadcast	    Discover hosts by sending broadcast messages
    + brute	        Performs brute-force password auditing against logins
    + default	    Default scripts, same as -sC
    + discovery	    Retrieve accessible information, such as database tables and DNS names
    + dos	        Detects servers vulnerable to Denial of Service (DoS)
    + exploit	    Attempts to exploit various vulnerable services
    + external	    Checks using a third-party service, such as Geoplugin and Virustotal
    + fuzzer	    Launch fuzzing attacks
    + intrusive	    Intrusive scripts such as brute-force attacks and exploitation
    + malware	    Scans for backdoors
    + safe	        Safe scripts that won’t crash the target
    + version	    Retrieve service versions
    + vuln	        Checks for vulnerabilities or exploit vulnerable services
- --script "SCRIPT_NAME" (script file in /usr/share/nmap/scripts)

# Saving the Output
- Three main formats:
  + Normal  : -oN FILENAME 
  + Grepable: -oG FILENAME
  + XML     : -oX FILENAME
  + Save all 3 formats: -oA
- There is a fourth one recommended: Script Kiddie
A fourth format is script kiddie. You can see that this format is useless if you want to search the output for any interesting keywords or keep the results for future reference. However, you can use it to save the output of the scan nmap -sS 127.0.0.1 -oS FILENAME, display the output filename, and look 31337 in front of friends who are not tech-savvy.

- nmap -sS 127.0.0.1 -oS FILENAME