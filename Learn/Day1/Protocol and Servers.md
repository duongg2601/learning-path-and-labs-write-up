# Sniffing Attack
- It refers to using a network packet capture tool to collect infor about the target
- When a protocol communicates in cleartext, the data exchanged can be captured by a third party to analyse

- A sniffing attack can be conducted using an Ethernet(802.3) network card, provided that the user has proper permissions
- Programs available to capture network packets:
    + Tcpdump: free open source CLI program
    + Wireshark: free open source GUI program
    + Tshark: CLI alternative to Wireshark

- Should mention that this attack requires access to the network traffic (via wiretap or a switch with port mirroring for example)

# Man-in-the-Middle (MITM) Attack
- Occurs when a victim(A) believes they are communicating with a legitimate destination(B) but is unknowingly communicating with an attacker(E)
- This attack is relatively simple to carry out if the two parties do not confirm the authenticity and integrity of each message

- Tools to carry out: Ettercap and Bettercap
- Solutions:
    + Proper authentication along with encryption or signing of the exchanged messages
    + Examples: Public Key Infrastructure(PKI), trusted root certificates, Transport Layer Security(TLS) protect from MITM attacks

# Secure Sockets Layer (SSL) and Transport Layer Security (TLS)

- Protocol ports with TLS:
    + HTTP: 80  -> HTTPS: 443
    + FTP : 21  -> FTPS : 990
    + SMTP: 25  -> SMTPS: 465
    + POP3: 110 -> POP3S: 995
    + IMAP: 143 -> IMAPS: 993
    + SSH : 22
    + telnet: 23
    + DNS : 53

    + DNS-over-TLS(DoT)

- HTTPS requires an additional step to encrypt the traffic. The new step takes place after establishing a TCP connection and before sending HTTP requests:
    1. Establish a TCP connection
    2. Establish SSL/TLS connection*
    3. Send HTTP requests to the webserver
- Four steps of establishing an SSL/TLS connection:
    1. Client sends a ClientHello to server to indicate its capabilities, such as supported algorithms
    2. Server responds with a ServerHello, indicating the selected connection params. Server provides its certificate if required.(Certificate is a digital file to identify itself, signed by a third party). Moreover, it might send additional infor necessary to generate master key, in its ServerKeyExchange message, before sending the ServerHelloDone message to indicate that its done with the negotiation
    3. Client responds with a ClientKeyExchange, which contains additional infor required to generate master key. Furthermore, it switches to use encryption and informs the server using the ChangeCipherSpec message
    4. Server switches to use encryption as well and informs client in the ChangeCipherSpec message
- In brief: A client was able to agree on a secret key with a server that has a public certificate signed by certificate authorities trusted by our systems

# Secure Shell (SSH)
- was created to provide a secure way for remote system administration
- SSH server listens on port 22 by default
- SSH client can authenticate using:
    + A username and a password
    + A private and public key(after the SSH server is configured to recognize the corresponding public key)
- Command: ssh username@ip.ip.ip.ip
- We can use SSH to transfer files using SCP(Secure Copy Protocol)
    + syntax: scp mark@10.49.190.120:/home/mark/archive.tar.gz ~
this command will copy a file named archive.tar.gz from the remote system in /home/mark to ~(root of home dir of current logged-in user)
    + syntax: scp backup.tar.bz2 mark@10.49.190.120:/home/mark/
this command will copy file from the local system to the dir on the remote system

# hydra option:
+ -l username
+ -P WordList.txt
+ server service (ip + port number)
+ -s PORT
+ -V or -vV
+ -d (display debugging output if verbose is not helping)