import socket


def sendMsg(msg, sock):
    sock.sendto(msg.encode(), 0, ('127.0.0.1', 6000))


def recvMsg():
    data, addr = sock.recvfrom(1024)
    return data

# Split into function and other script - the sender
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sendMsg('(init Kuntz (version 7))', sock)
sendMsg('(move -15 0)', sock)