#!/usr/bin/python

import socket
import time

target_ip = '18.156.68.123'
target_port = 80
rot = 26
buff_size = 2048

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((target_ip,target_port))
print(s.recv(58))

base = []
for i in range(0,26):
    x = s.recv(88).decode()
    s.sendall("".encode())
    print(x)
    base.append(x)

for i in base:
    print(i)
