import socket

uniformNumber = -1
sideOfField = 'N'
currentPlayMode = 'NULL'


def sendMsg(msg, sock):
    sock.sendto(msg.encode(), 0, ('127.0.0.1', 6000))


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
    else:
        print("Receive unknown msg from server:")
        print(msg)
        print(RuntimeError())


# debug_printVariables()


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


def debug_print_variables():
    print("Current variable status:")
    print("Uniform number: " + str(uniformNumber))
    print("Side of field: " + sideOfField)
    print("Current playmode: " + currentPlayMode)


sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sendMsg('(init Kuntz (version 7))', sock)
sendMsg('(move -15 0)', sock)

while True:
    data, addr = sock.recvfrom(1024)
    parseSrvMsg(data.decode())
