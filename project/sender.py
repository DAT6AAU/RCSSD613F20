import socket


def send_msg(sock, msg):
    sock.sendto(surround_parentheses(msg).encode(), 0, ('127.0.0.1', 6000))


def surround_parentheses(string):
    return "(" + string + ")"


def send_init(sock, team_name, isGolie):
    msg = "init " + team_name + " (version 7)"
    if isGolie:
        msg + " (goalie)"
    send_msg(sock, msg)


def send_move(sock, x, y):
    send_msg(sock, "move " + x + " " + y)
