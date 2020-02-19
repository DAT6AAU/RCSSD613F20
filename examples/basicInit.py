import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.sendto('(init TeamName)', 0, ('127.0.0.1', 6000))
