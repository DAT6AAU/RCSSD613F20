import socket


def sendMsg(msg, sock):
	sock.sendto(msg, 0, ('127.0.0.1', 6000))


sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sendMsg('(init Kuntz)', sock)
sendMsg('(move -15 0)', sock)

raw_input("Kick-off and press key to continue.")

while(True):
	data, add = sock.recvfrom(1024)
	print(data)
	#raw_input("Prs")
	sendMsg('(dash 100)', sock)
	sendMsg('(kick 100 0)', sock)
