# TCP Null Scan, FIN Scan, and Xmas Scan
1. Null Scan
- nmap -sN TARGETS
- all six flag bits are set to zero 
- expect a RST packet if is closed
- use the lack of RST response to figure out the ports that are open or filtered

2. FIN Scan
- nmap -sF TARGETS
- cannot be sure if the port is open or filtered

3. Xmas Scan
- nmap -sX TARGETS
- sets the FIN, PSH, and URG flags
- Like Null and FIN, closed if receives an RST packet. Otherwise, open or filtered

* This free scan types useful when scanning a target behind a stateless(non-stateful) firewall

# TCP Maimon Scan
- FIN and ACK are set
- Receives RST packet if open or closed

# TCP ACK Scan
- nmap -sA TARGETS
- more suitable to discover firewall rule sets and configuration
# Window Scan
- nmap -sW TARGETS
- Similar to ACK
# Custom Scan
- nmap --scanflags CUSTOM_FLAGS TARGETS (example: URGACKPSHRSTSYNFIN sets all flags)

# Spoofing and Decoys
- In brief, scanning with a spoofed IP address is 3 steps:
    + Attacker sends a packet with a spoofed source IP address to the target machine
    + Target machine replies to the spoofed IP as the destination
    + Attacker captures the replies to figure out open ports
- Syntex in general:
    nmap -e NET_INTERFACE -Pn -S SPOOFED_IP TARGETS (-Pn: explicit disable ping scan)

    --spoof-mac: when in the same subnet

- Decoys: make the scan appear to be coming from many IP addresses so that that attacker's IP would be lost among them
    nmap -D 10.10.0.1,10.10.0.2,RND,RND,ME TARGETS (RND is assigned randomly)

# Fragmented Packets
- -f: divide into 8 bytes
- -f -f or -ff: 16 bytes
- If we prefer to increase the size of your packets to make them look innocuous, we can use the option: --data-length NUM (NUM specifies the num of bytes want to append to the packets)

# Idle/Zombie Scan
- 3 steps to discover whether a port is open:
    + Trigger the idle host to respond so that you can record the current IP ID on the idle host
    + Send a SYN packet to a TCP port on the target. The packet should be spoofed to appear as if it was coming from the idle host IP address
    + Trigger the idle machine again to respond so that you can compare the new IP ID with the one received earlier

# Getting more Details
- --reason: provide more details regarding its reasoning and conclusions
- -v or -vv: for verbose output
- -d or -dd: for debugging details