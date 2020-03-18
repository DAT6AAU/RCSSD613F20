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


def debug_send_msgs(sock):
    #sender.send_score_request(sock)
    #sender.send_msg(sock, "disconnect")
    #sender.send_reconnect_request(sock, "Kuntz", 2)

    pass


def main():
    sock = connect()
    sender.send_init(sock, "Kuntz", False)

    while True:
        data = recv_msg(sock)
        debug_send_msgs(sock)
        listener.parseSrvMsg(data.decode())


if __name__ == "__main__":
    main()
