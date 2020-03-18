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


def send_reconnect_request(sock, team_name, player_uni_number):
    send_msg(sock, "reconnect " + team_name + " " + str(player_uni_number))


def send_move(sock, x, y):
    send_msg(sock, "move " + x + " " + y)


# TODO test
def send_catch(sock, direction):
    if is_goalie:
        send_msg(sock, "catch " + str(direction))


# TODO test
def send_change_view(sock, width, quality):
    send_msg(sock, "change_view " + width + " " + quality)


# TODO test
def send_dash(sock, power):
    send_msg(sock, "dash " + power)


# TODO test
def send_kick(sock, power, direction):
    send_msg(sock, "kick " + power + " " + direction)


# TODO test
def send_say(sock, msg):
    send_msg(sock, "say " + msg)


# TODO test
def send_sense_body(sock):
    send_msg(sock, "sense_body")


# TODO test
def send_turn(sock, moment):
    send_msg(sock, "turn " + str(moment))


# TODO test
def send_turn_neck(sock, angle):
    send_msg(sock, "turn_neck " + angle)
