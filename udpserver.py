import socket
from unittest import result

from sympy import residue
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #dgram - udp protokol
# AF INET - ip protokol v4
s.bind (('127.0.0.1', 8888)) # reserv na servake adress i port
result = s.recv(1024) #proslushivaet port i zalivaet v result
print('Message:', result.decode('utf-8')) #pechataet soobshenie
s.close() # tormozim prosluivanie porta