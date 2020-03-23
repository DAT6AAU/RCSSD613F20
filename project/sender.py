import socket

# TODO This should be in player.py
is_goalie = False
udp_socket = socket


def set_socket(sock):
    global udp_socket
    udp_socket = sock


def send_msg(msg):
    global udp_socket
    udp_socket.sendto(surround_parentheses(msg).encode(), 0, ('127.0.0.1', 6000))


def surround_parentheses(string):
    return "(" + string + ")"


def send_init(team_name, _is_goalie):
    global is_goalie
    is_goalie = _is_goalie
    msg = "init " + team_name + " (version 7)"
    if _is_goalie:
        msg + " (goalie)"
    send_msg(msg)


def send_commands_for_next_cycle(dict_of_commands):
    msg = ""
    next_command = ""

    for command in dict_of_commands:
        next_command += command[0]
        for arg in command[1]:
            next_command += " " + arg
        next_command = surround_parentheses(next_command)
        msg += next_command
        next_command = ""
    send_msg(msg)

# ***


def send_score_request():
    send_msg("score")


def send_reconnect_request(team_name, player_uni_number):
    send_msg("reconnect " + team_name + " " + str(player_uni_number))


def send_move(x, y):
    send_msg("move " + x + " " + y)


# TODO test
def send_catch(direction):
    if is_goalie:
        send_msg("catch " + str(direction))


# TODO test
def send_change_view(width, quality):
    send_msg("change_view " + width + " " + quality)


# TODO test
def send_dash(power):
    send_msg("dash " + power)


# TODO test
def send_kick(power, direction):
    send_msg("kick " + power + " " + direction)


# TODO test
def send_say(msg):
    send_msg("say " + msg)


# TODO test
def send_sense_body():
    send_msg("sense_body")


# TODO test
def send_turn(moment):
    send_msg("turn " + str(moment))


# TODO test
def send_turn_neck(angle):
    send_msg("turn_neck " + angle)
