import socket


def sendMsg(msg, sock):
	sock.sendto(msg, 0, ('127.0.0.1', 6000))


sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sendMsg('(init Kuntz)', sock)
sendMsg('(move -15 0)', sock)


while(True):
	raw_input("Press to continue.")
	sendMsg('(dash 100)', sock)
	raw_input("P")
	sendMsg('(kick 100 0)', sock)

raw_input("Press to continue.")
