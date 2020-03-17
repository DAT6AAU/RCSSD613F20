import socket


def sendMsg(msg, sock):
	sock.sendto(msg, 0, ('127.0.0.1', 6000))


sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#sock.sendto('(init Kuntz)', 0, ('127.0.0.1', 6000))
sendMsg('(init Jon)', sock)
sendMsg('(move 0 -34)', sock)

input()
