from data import sense_body
import re

uniformNumber = -1
sideOfField = 'N'
currentPlayMode = 'NULL'

# Score
game_time = -1
score_our = -1
score_their = -1


def parseSrvMsg(msg):
    # trim parentheses
    msg = msg[1:len(msg) - 2]

    if msg.startswith('error'):
        parse_error(msg)
    elif msg.startswith('server_param'):
        parse_param_server(msg)
    elif msg.startswith('player_param'):
        parse_param_player(msg)
    elif msg.startswith('player_type'):
        parse_player_type(msg)
    elif msg.startswith('init'):
        parse_init(msg)
    elif msg.startswith('change_player_type'):
        parse_change_player_type(msg)
    elif msg.startswith('sense_body'):
        parse_sense_body(msg)
    elif msg.startswith('see'):
        parse_see(msg)
    elif msg.startswith('hear'):
        parse_hear(msg)
    elif msg.startswith('score'):
        parse_score(msg)
    elif msg.startswith('reconnect'):
        parse_reconnect(msg)
    else:
        print("Receive unknown msg from server:")
        print(msg)
        print(RuntimeError())

    # debug_print_variables()


def parse_init(msg):
    global sideOfField
    global uniformNumber
    global currentPlayMode

    print("Parsing init msg")
    msgComponents = msg.split()
    sideOfField = msgComponents[1]
    uniformNumber = msgComponents[2]
    currentPlayMode = msgComponents[3]


def remove_surrounding_parenthesis(string):
    return string[1:len(string)-2]


def parse_param_server(msg):
    print("Not yet implemented: server_param")


def parse_param_player(msg):
    print("Not yet implemented: param_player")


def parse_player_type(msg):
    print("Not yet implemented: player_type")


# Syntax:
def parse_change_player_type(msg):
    print("Not yet implemented: change_player_type")


def parse_sense_body(msg):
    body_data = sense_body.SenseBodyData()

    split_space = msg.split(" ")
    body_data.time = split_space[1]

    msg_without_parenthesis = remove_surrounding_parenthesis(msg)
    split_parenthesis = re.findall('\[[^\]]*\]|\([^\)]*\)|\"[^\"]*\"|\S+', msg)

    # remove msg keyword and time
    data_array = split_parenthesis[2:len(split_parenthesis)-1]

    # check for keywords
    for element in data_array:

        element_array = element.split(" ")

        if element_array[0] == "(view_mode":
            body_data.view_mode_vertical = element_array[1]
            body_data.view_mode_horizontal = element_array[2]
        elif element_array[0] == "(stamina":
            body_data.stamina_stamina = element_array[1]
            body_data.stamina_effort = element_array[2]
        elif element_array[0] == "(speed":
            # TODO should be two parameters? But is only one?
            pass
        elif element_array[0] == "(head_angle":
            body_data.head_angle = element_array[1]
        elif element_array[0] == "kick":
            body_data.count_kick = element_array[1]
        elif element_array[0] == "(dash":
            body_data.count_dash = element_array[1]
        elif element_array[0] == "(turn":
            body_data.count_turn = element_array[1]
        elif element_array[0] == "(say":
            body_data.count_say = element_array[1]
        else:
            print("parsing of sense_body failed. Could not find parsing for element: " + element)

def parse_see(msg):
    print("Not yet implemented: see")


def parse_hear(msg):
    print("Not yet implemented: hear")


# TODO test
def parse_reconnect(msg):
    global sideOfField
    global currentPlayMode

    print("Parsing reconnect msg")
    msg_components = msg.split()
    sideOfField = msg_components[1]
    currentPlayMode = msg_components[2]


# error illegal_command_form, illegal syntax on msg send to server
# error no_more_player_or_goalie_or_illegal_client_version, joining full team
# error no_more_team_or_player, reconnect response, not yet seen
def parse_error(msg):
    print("Error msg received from server!")
    print("msg: " + msg)
    raise RuntimeError()


def parse_score(msg):
    global game_time
    global score_our
    global score_their

    print("Parsing score msg")
    msg_components = msg.split()
    game_time = msg_components[1]
    score_our = msg_components[2]
    score_their = msg_components[3]


def debug_print_variables():
    print("Current variable status:")
    print("Uniform number: " + str(uniformNumber))
    print("Side of field: " + sideOfField)
    print("Current playmode: " + currentPlayMode)
    print("Game time: " + str(game_time))
    print("Our score: " + str(score_our))
    print("Their score: " + str(score_their))
