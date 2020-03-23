def send_commands_for_next_cycle(dict_of_commands):
    msg = ""
    next_command = ""

    for c in dict_of_commands:
        next_command += c[0]
        for arg in c[1]:
            next_command += " " + arg
        next_command = "(" + next_command + ")"
        msg += next_command
        next_command = ""
    print(msg)


dict_temp1 = [("turn_neck", ["30"]), ("kick", ["30", "20"])]
dict_temp2 = [("change_view", ["narrow", "low"])]
dict_temp3 = [("dash", ["30"]), ("turn_neck", ["-20"])]

send_commands_for_next_cycle(dict_temp1)
send_commands_for_next_cycle(dict_temp2)
send_commands_for_next_cycle(dict_temp3)