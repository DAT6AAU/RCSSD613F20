from data import sense_body
from data import see
import re

uniformNumber = -1
sideOfField = 'N'
currentPlayMode = 'NULL'

# Score
game_time = -1
score_our = -1
score_their = -1

body_data = sense_body.SenseBodyData()
see_data = see.See()


def parseSrvMsg(msg):
    #print("START: " + msg)
    # trim parentheses
    #msg = msg[1:len(msg) - 2]
    msg = remove_surrounding_parenthesis(msg)
    #print("START2: " + msg)

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
    #print("first: " + string[0] + " last: " + string[len(string)-1])
    if string[0] != "(" or string[len(string)-1] != ")":
        print("remove_surrounding_parenthesis. String is not surrounded by parenthesis:")
        print(string)
        print(RuntimeError())


    return string[1:len(string)-1]


def parse_param_server(msg):
    print("Not yet implemented: server_param")


def parse_param_player(msg):
    print("Not yet implemented: param_player")


def parse_player_type(msg):
    print("Not yet implemented: player_type")


# Syntax:
def parse_change_player_type(msg):
    print("Not yet implemented: change_player_type")


# TODO Atm. we only overwrite values which we have received. So old values are maintained.
def parse_sense_body(msg):
    global body_data

    split_space = msg.split(" ")
    body_data.time = split_space[1]

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
        elif element_array[0] == "(kick":
            body_data.count_kick = element_array[1]
        elif element_array[0] == "(dash":
            body_data.count_dash = element_array[1]
        elif element_array[0] == "(turn":
            body_data.count_turn = element_array[1]
        elif element_array[0] == "(say":
            body_data.count_say = element_array[1]
        elif element_array[0] == "(turn_neck":
            body_data.count_turn_neck = element_array[1]
        elif element_array[0] == "(catch":
            body_data.count_catch = element_array[1]
        elif element_array[0] == "(move":
            body_data.count_move = element_array[1]
        else:
            print("parsing of sense_body failed. Could not find parsing for element: " + element)


def parse_see(msg):
    global see_data
    see_data.reset()

    # print("Passing see: " + msg)

    space_splitted = msg.split(" ")
    see_data.time = space_splitted[1]

    first_parenthesis_index = 0
    for c in msg:
        first_parenthesis_index += 1
        if c == "(":
            break

    msg_removed_start = msg[first_parenthesis_index-1:]
    # print("Msg with start removed: " + msg_removed_start)

    objects = split_parenthesis_into_array(msg_removed_start)
    for obj in objects:
        see_object = see.SeeDataObject()
        # todo get first parenthesis: x
        # print("Before split: ")
        # print(obj)
        split_parenthesis = re.findall('\[[^\]]*\]|\([^\)]*\)|\"[^\"]*\"|\S+', obj)
        # print("split parenthesis: ")
        # print(split_parenthesis)
        # todo parse this: parse_see_identifiers(x, see_object)

        parse_see_identifiers(remove_surrounding_parenthesis(split_parenthesis[0]), see_object)

        # todo get distance numbers: y
        # print("Split parent: ")
        # print(split_parenthesis)
        for elem in split_parenthesis[1:]:
            see_object.last_part_numbers_array.append(elem)
            # print("Element:")
            # print(elem)

        print("See object: ")
        print(see_object.last_part_numbers_array)
        see_data.see_objects_array.append(see_object)

    # print("OBJECTS: ")
    # print(see_data.see_objects_array)

    see_data.get_player_pos()


# help function for parse_see. Should receive a string containing chars separated by spaces.
# Sets type and location identifiers in given see_obj
def parse_see_identifiers(iden_string, see_object):
    identifiers = iden_string.split(" ")

    #print(iden_string)
    #print("identiifer array: ")
    #print(identifiers)
    #see_object = see.SeeObject

    if identifiers[0] == "f":
        see_object.obj_type = see.SeeObjectType.FLAG
    elif identifiers[0] == "g":
        see_object.obj_type = see.SeeObjectType.GOAL
    elif identifiers[0] == "p":
        see_object.obj_type = see.SeeObjectType.PLAYER
    else:
        print("error parsing see identifiers. Did not recognize: " + identifiers[0])
        print(RuntimeError())

    if len(identifiers) > 1:
        for c in identifiers[1:]:
            see_object.location_identifiers.append(c)

    # print(see_object.obj_type)  # TODO Debugging
    # print(see_object.location_identifiers)  # TODO Debugging
    # print(RuntimeError())  # TODO Debugging


# Returns array where each element is the string split between each outer parentheses
def split_parenthesis_into_array(string):
    #print("input string: " + string)
    result_array = []

    in_parenthesis_block = False
    count_extra_start_parenthesis = 0
    content = ""

    for c in string:
        if not in_parenthesis_block:
            if c == "(":
                in_parenthesis_block = True
                content += "("
        else:
            content += c
            if c == "(":
                count_extra_start_parenthesis += 1
            elif c == ")":
                if count_extra_start_parenthesis == 0:
                    result_array.append(remove_surrounding_parenthesis(content))
                    in_parenthesis_block = False
                    content = ""
                else:
                    count_extra_start_parenthesis -= 1

    return result_array


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
