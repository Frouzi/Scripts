#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  5 10:06:51 2022

@author: alekseevev
"""

import socket

target_host = "www.google.com"
target_port = 80

#sozdaem object socketa
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#podkl client
client.connect((target_host, target_port))

#otpravlyaem dannie
client.send(b"GET / HTTP/1.1\r\nHost: google.com\r\n\r\n")

#prinimaem dannie
response = client.recv(4096)

print(response.decode())
client.close()