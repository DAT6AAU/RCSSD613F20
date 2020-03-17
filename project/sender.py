import socket


def send_msg(sock, msg):
    sock.sendto(surround_parentheses(msg.encode()), 0, ('127.0.0.1', 6000))


def surround_parentheses(string):
    return "(" + string + ")"


def send_init(sock, team_name):
    send_msg(sock, "init " + team_name + " (version 7)")


def send_move(sock, x, y):
    send_msg(sock, "move " + x + " " + y)
