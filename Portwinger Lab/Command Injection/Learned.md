# OS command injection

OS Command Injection <-> Shell Injection 

Placing the additional command separator & after the injected command is useful because it separates the injected command from whatever follows the injection point. This reduces the chance that what follows will prevent the injected command from executing.

Simple case <lab1>

# Useful command on Linux and Windows:

Purpose of command      Linux       Windows

Name current user       whoami      whoami
Operating System        uname -a    ver
Network config          ifconfig    ipconfig /all
Network connections     netstat -an netstat -an
Running processes       ps -ef      tasklist

# Blind OS command injection vulnerabilities

- Detecting blind OS ci using time delays
& command is a good way to do this: & ping -c 10 1 &
<lab2>