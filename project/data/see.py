from enum import Enum


class See:
    time = 0  # simulation cycle of the soccerserver
    see_objects_array = []

    flag_pos_lt = [0, 0]
    flag_pos_ct = [0, 0]
    flag_pos_rt = [0, 0]
    goal_pos_r = [0, 0]
    flag_pos_rb = [0, 0]
    flag_pos_cb = [0, 0]
    flag_pos_lb = [0, 0]
    goal_pos_l = [0, 0]

    def reset(self):
        self.time = 0
        self.see_objects_array = []

    # todo should not be here
    def get_player_pos(self, msg):

        # todo hardcode pos of 8 flags
        #done

        # todo identify which of the hardcoded flags the player sees

        # todo use that data together with distance from player to those points to triangulate pos

        pass


    def get_object_type(self, see_object):
        pass


class SeeObjectType(Enum):
    FLAG = 1
    PLAYER = 2
    GOAL = 3

class SeeObject:
    obj_type = SeeObjectType
    location_identifiers = []  # b | r | l | c
    last_part_numbers_array = []  # todo temp - to be handled
