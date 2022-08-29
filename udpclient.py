#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  5 10:15:25 2022

@author: alekseevev
"""

import socket

target_host = "127.0.0.1"
target_port = 9997
    
#ojbect
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#dannie =>
client.sendto(b"AAABBBCCC", (target_host,target_port))

#prinimaem dannie
data, addr = client.recvfrom(4096)

print(data.decode())
client.close()
