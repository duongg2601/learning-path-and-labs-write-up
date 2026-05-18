# TCP and UDP ports:
- six states:
    + Open              : a service is listening on the specified port
    + Closed            : no service is listening, although the port is accessible
    + Filtered          : cannot determine open or closed because the port is not accessible
    + Unfiltered        : cannot determine open or closed although the port is accessible (encounter when using an ACK scan -sA)
    + Open|Filtered     : cannot determine open or filtered
    + Closed|Filtered   : cannot determine closed or filtered

# TCP Flags
- TCP header: is the first 24 bytes of a TCP segment, includes:
    + Source + Destination Port: 16 + 16 bits
    + Sequence Number          : 32      bits
    + Ack Number               : 32      bits
    + Data Offset              : 4       bits
      Reverved                 : 6       bits
      TCP Flags                : 6       bits
      Window                   : 16      bits
    + Checksum + Urgent Pointer: 16 + 16 bits
    + Options + Padding        : 24 + 8  bits
- TCP Flags:
    + URG: Urgent flag, indicates that the incoming data is urgent. A TCP segment with URG flag set is processed immediately without consideration of having wait on previously sent TCP segments
    + ACK: Acknowledgement flag indicates that the ack number is significant. Used to ack the receipt of a TCP segment
    + PSH: Push flag asking TCP to pass the data to the app promptly
    + RST: Reset flag is used to reset the connection
    + SYN: Synchronize flag is used to initiate a TCP 3-way handshake and synchronize sequence numbers with other host
    + FIN: The sender has no more data to send

# TCP Connect Scan
- nmap -sT TARGETS
- -F: enable fast mode, 100 most common ports instead of 1000
- -r: scan ports in consecutive order, be useful when testing whether ports open in a consistent manner, for instance, when a target boots up
# TCP SYN Scan
- nmap -sS TARGETS
- tear down the connection once it receives a response, dont need to complete 3-way handshake
# UDP Scan
- If port closed, this leads to ICMP Destination Unreachable
- nmap -sU -F -v TARGETS (UDP port scan takes longer than TCP one, so can use -F option to speed up scan)

# Fine-Tuning Scope and Performance
- Specify the ports scanned instead of 1000 default ports:
    + port list      : -p22,80,443
    + port range     : -p1-1023
    + all ports      : -p-
    + ten most common: --top-ports 10
- Scan timing: -T<0-5>
    + paranoid  (0): slowest
    + sneaky    (1): real engagement where stealth is more important
    + polite    (2)
    + normal    (3): normal when dont specify
    + aggressive(4): CTFs and learning practice
    + insane    (5): fastest, but can affect the accuracy due to packet loss
- Alternative: 
    + --min-rate <number> and --max-rate <number> (per sencond) 
    + --min-parallelism <numprobes>
      --max-parallelism <numprobes>