import listener
import sender
import socket


def connect():
    # Split into function and other script - the sender
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sender.set_socket(sock)
    return sock


def recv_msg(sock):
    data, addr = sock.recvfrom(1024)
    return data


def debug_send_msgs():
    #sender.send_score_request()
    #sender.send_msg("disconnect")
    #sender.send_reconnect_request("Kuntz", 2)

    pass


def main():
    sock = connect()
    sender.send_init("Kuntz", False)

    while True:
        data = recv_msg(sock)
        string = data.decode()
        debug_send_msgs()
        listener.parseSrvMsg(string[:len(string)-1])


if __name__ == "__main__":
    main()
