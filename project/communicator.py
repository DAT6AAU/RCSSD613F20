import listener
import socket


def connect():
    # Split into function and other script - the sender
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    send_msg('(init Kuntz (version 7))', sock)
    send_msg('(move -15 0)', sock)
    return sock


def send_msg(msg, sock):
    sock.sendto(msg.encode(), 0, ('127.0.0.1', 6000))


def recv_msg(sock):
    data, addr = sock.recvfrom(1024)
    return data


def main():
    sock = connect()
    while True:
        data = recv_msg(sock)
        listener.parseSrvMsg(data.decode())


if __name__ == "__main__":
    main()


