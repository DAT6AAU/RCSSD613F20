import listener
import sender
import socket


def connect():
    # Split into function and other script - the sender
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return sock


def recv_msg(sock):
    data, addr = sock.recvfrom(1024)
    return data


def main():
    sock = connect()
    sender.send_init(sock, "Kuntz", False)
    while True:
        data = recv_msg(sock)
        listener.parseSrvMsg(data.decode())


if __name__ == "__main__":
    main()


