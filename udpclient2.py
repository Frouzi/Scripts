import socket

targer_host = "127.0.0.1"
target_port = 9997

#create object socketa
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#send dannie
client.sendto(b"AAABBBCCC", (targer_host, target_port))

#prinimaem dannie
data, addr = client.recvfrom(4096)

print(data.decode())
client.close()