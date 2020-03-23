# constants
number = -1
name = ""
team_name = "?"
field_side = "left"    # behøver vi den?
starting_position = (-1,-1)

# properties
# view_mode = (-1,-1) # (0=high 1=low , 0=narrow 1=normal 2=wide) -- lad os ignorerer den for nu
stamina = -1 # hvad er stamina effort?

position = (-1,-1)  # måske opdelt i zoner
body_direction = -1  # 0-360
head_direction = -1  # 0-180
# uml viser, body_direction, face_direction og neck_direction. Er der noget jeg har misforstået?

ball_position = (-1,-1)
ball_possession_now = -1   # 0 = none, 1 = us, 2 = them, 3 = don't know

can_I_see_the_ball = False
do_I_have_the_ball = False

visible_players = []
visible_markers = []


# expected values - ved ikke hvor meget af det der blier relevant
stamina_expected = -1
position_expected = -1
# etc
#

# *** objective (states!?)
# offense
# defense
# ?

# *** actions
# locate ball
# run towards ball
# block enemy_with_ball
# block enemy_without_ball
# etc

# *** commands
# dash(power)
# turn(moment)
# kick(power, direction)
# turn_neck(angle)
# catch(direction)
# say(message)
# change_view(width, quality)

# *** not handled here
# move(x, y)
# sense_body()
# score()


""" setup functions  -- bare lidt tanker
pre-match
halftime
other: hjørne, indkast.... 
"""

""" main loop once a cycle
update() #info fra dataklassen (sense_body og score)
?change_objective?()
?update_actions?()
decide_commands_for_next_cycle()
send(list_of_command-args_tuples)
"""
