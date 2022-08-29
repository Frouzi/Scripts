#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  5 10:20:40 2022

@author: alekseevev
"""

import socket
import threading

IP = '0.0.0.0'
PORT = 9998

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((IP,PORT))
    server.listen(5)
    print(f'[*] Listening on {IP}:{PORT}')
    
    while True:
        client,addres = server.accept()
        print(f'[*] Accepted connectio from {addres[0]}:{addres[1]}')
        client_handler = threading.Thread(target=hanlde_client, args=(client,))
        client_handler.start()
        
    def handle_client(client_socket):
        with  client_socket as sock:
            request = sock.recv(1024)
            pritn(f'[*] Received: {request.decode("utf-8")}')
            sock.send(b'ACK')
            
if __name__ == '__main__':
    main()
        