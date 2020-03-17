import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#server_add = ('127.0.0.1', 6000)
#sock.bind(server_add)

while True:
	data, addr = sock.recvfrom(1024)
	print data
