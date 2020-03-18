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
    elif msg.startswith('init'):
        parse_init(msg)
    elif msg.startswith('sense_body'):
        parse_sense_body(msg)
    elif msg.startswith('see'):
        parse_see(msg)
    elif msg.startswith('hear'):
        parse_hear(msg)
    elif msg.startswith('score'):
        parse_score(msg)
    else:
        print("Receive unknown msg from server:")
        print(msg)
        print(RuntimeError())

    debug_print_variables()


def parse_init(msg):
    global sideOfField
    global uniformNumber
    global currentPlayMode

    print("Parsing init msg")
    msgComponents = msg.split()
    sideOfField = msgComponents[1]
    uniformNumber = msgComponents[2]
    currentPlayMode = msgComponents[3]


def parse_sense_body(msg):
    print("Not yet implemented")


def parse_see(msg):
    print("Not yet implemented")


def parse_hear(msg):
    print("Not yet implemented")


def parse_error(msg):
    print("Error msg received from server!")
    print("msg: " + msg)
    raise RuntimeError()


def parse_server_param(msg):
    print("Not yet implemented: server_param")


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
