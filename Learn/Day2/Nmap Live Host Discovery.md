# ARP queries
- Used when we are on the same subnet
- aim to obtain MAC address => communicate at the link layer

# nmap syntax:
- nmap -sL TARGETS (list of hosts scanned without actually scan)
- nmap -iL list_of_host.txt (provide list of hosts scanned )
- -n: dont nmap to the DNS server
- range scanned: ip.ip.ip.0-255 or MACHINE_IP/30(scan 4 ip)

# Nmap Host Discovery Using ARP
- Nmap follow this approaches to discover live hosts:
    + When a privileged user tries to scan target on a local network, Nmap uses ARP res
    + When outside, Nmap uses ICMP echo res, TCP ACK to port 80, TCP SYN to port 443, and ICMP timestamp res
    + When an unprivileged user tries to scan outside the local net, Nmap resorts to a TCP 3-way handshake by sending SYN packets to ports 80 and 443

- Nmap perform only ARP scan without port-scanning: nmap -PR -sn TARGETS
    + -PR: ARP res
    + -sn: without port scan
- arp-scan: + arp-scan --localnet(or -l)
            + sudo arp-scan -I eth0 -l

# Nmap Host Discovery Using ICMP
- ping request (ICMP Type8/Echo)
- ping reply (ICMP Type 0)
- ARP query precedes an ICMP request if target is on the same subnet
- nmap -PE -sn TARGETS

- ICMP echo res tend to be blocked, we consider ICMP Timestamp or ICMP Address Mask res
- Nmap uses a timestamp res(ICMP Type 13) and check whether it will get a Timestamp reply(ICMP Type 14) by adding the -PP option
    sudo nmap -PP -sn TARGETS
- Similarly with address mask queries (ICMP Type 17 and 18) by -PM option
    nmap -PM -sn TARGETS

- note: its essential to learn mmultiple approaches to achieve the same result if one is blocked

# Nmap Host Discovery Using TCP and UDP
* TCP SYN Ping: nmap -PS80 -sn TARGETS
* TCP ACK Ping: nmap -PA80 -sn TARGETS
* UDP Ping: If we send a UDP packet to a closed UDP port, we expect to get an ICMP unreachable packet (ICMP Type 3, Code 3)
    nmap -PU -sn TARGETS
* Masscan examples:
    + masscan TARGETS -p443
    + masscan TARGETS -80,443
    + masscan TARGETS -p22-25
    + masscan TARGETS --top-ports 100

# Using Reverse-DNS Lookup
Nmap’s default behaviour is to use reverse-DNS online hosts. Because the hostnames can reveal a lot, this can be a helpful step. However, if you don’t want to send such DNS queries, you use -n to skip this step.

By default, Nmap will look up online hosts; however, you can use the option -R to query the DNS server even for offline hosts. If you want to use a specific DNS server, you can add the --dns-servers DNS_SERVER option.