import socket

# TODO This should be in player.py
is_goalie = False


def send_msg(sock, msg):
    sock.sendto(surround_parentheses(msg).encode(), 0, ('127.0.0.1', 6000))


def surround_parentheses(string):
    return "(" + string + ")"


def send_init(sock, team_name, _is_goalie):
    global is_goalie
    is_goalie = _is_goalie
    msg = "init " + team_name + " (version 7)"
    if _is_goalie:
        msg + " (goalie)"
    send_msg(sock, msg)


def send_score_request(sock):
    send_msg(sock, "score")


def send_move(sock, x, y):
    send_msg(sock, "move " + x + " " + y)
