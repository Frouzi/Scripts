import socket
from urllib import response

target_host = "www.google.com"
target_port = 80

#create object socketa
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#connect client
client.connect((target_host, target_port))

#send dannie
client.send(b"GET / HTTP/1.1\r\nHost: google.com\r\n\r\n")

#prinimaem dannie
response = client.recv(4096)

print(response.decode())
client.close
