import socket
import sys

def sendMsg(msg, sock):
	sock.sendto(msg, 0, ('127.0.0.1', 6000))


numberOfInputArgs = len(sys.argv)
teamName = sys.argv[1]
playerX = sys.argv[2]
playerY = sys.argv[3]

print 'Input arguments: ', str(sys.argv)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Init string
initString = '(init ' + teamName
# Is this player a goalie?
if(len(sys.argv) == 5):
	initString += 'goalie'
initString += ')'
sendMsg(initString, sock)

#Move string
moveString = '(move ' + playerX + playerY + ')'
sendMsg(moveString, sock)

raw_input("Kick-off and press key to continue.")

while(True):
	data, add = sock.recvfrom(1024)
	print(data)
	#raw_input("Prs")
	sendMsg('(dash 100)', sock)
	sendMsg('(kick 100 0)', sock)
