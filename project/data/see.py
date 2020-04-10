from enum import Enum
import math


class See:
    time = 0  # simulation cycle of the soccerserver
    see_objects_array = []
    hardcoded_flags = []

    def __init__(self):
        self.time = 0
        self.last_part_numbers_array = []
        self.setup_hardcoded_flags()

    def setup_hardcoded_flags(self):
        self.hardcoded_flags.append(HardcodedFlag(0, 0, ["l", "t"]))
        self.hardcoded_flags.append(HardcodedFlag(0, 0, ["c", "t"]))
        self.hardcoded_flags.append(HardcodedFlag(0, 0, ["r", "t"]))
        self.hardcoded_flags.append(HardcodedFlag(0, 0, ["r"]))
        self.hardcoded_flags.append(HardcodedFlag(0, 0, ["r", "b"]))
        self.hardcoded_flags.append(HardcodedFlag(0, 0, ["c", "b"]))
        self.hardcoded_flags.append(HardcodedFlag(0, 0, ["l", "b"]))
        self.hardcoded_flags.append(HardcodedFlag(0, 0, ["l"]))

    def reset(self):
        self.time = 0
        self.see_objects_array = []

    # todo should not be here
    def get_player_pos(self):
        # todo hardcode pos of 8 flags
        #done

        # todo identify two hardcoded flags that the player can see
        # TODO: Optimize: stop at two flags found
        found_flags = []
        for see_flag in self.see_objects_array:
            for hardcoded_flag in self.hardcoded_flags:
                # Does the types match?
                if see_flag.obj_type is hardcoded_flag.flag_type:
                    is_matching = True
                    # Does their identifiers match?
                    for i1, i2 in zip(see_flag.location_identifiers, hardcoded_flag.location_identifiers):
                        if i1 is not i2:
                            is_matching = False
                    if is_matching:
                        found_flags.append(see_flag)

        # todo use that data together with distance from player to those points to triangulate pos
        if len(found_flags) == 0:
            print("Tried finging player pos. But does not see any hardcoded flags.")
            return
        else:
            chosen_flags = self.pick_two_falgs(found_flags)
        # TODO Get hardcoded pos of the two chosen flags
        chosen_flag_one_pos = self.get_pos_of_flag_from_identifiers(chosen_flags[0].location_identifiers)
        chosen_flag_two_pos = self.get_pos_of_flag_from_identifiers(chosen_flags[1].location_identifiers)
        print("Chosen flag one pos: " + str(chosen_flag_one_pos))
        print("Chosen flag two pos: " + str(chosen_flag_two_pos))
        print(RuntimeError())
        # TODO Get distance to the two chosen flags
        positions = self.get_intercetions(chosen_flag_one_pos[0], chosen_flag_one_pos[1], 0,
                                          chosen_flag_two_pos[0], chosen_flag_two_pos[1], 0)  # TODO pass the info
        # TODO Pick the right coordinate
        # TODO Return it
        pass

    # Takes list of chars. Returns list with two ints.
    def get_pos_of_flag_from_identifiers(self, identifiers):
        print("get_pos_of_flag_from_iden: received idenents: " + str(identifiers))
        for hardcoded_flag in self.hardcoded_flags:
            # print("HC.flag.iden: " + str(hardcoded_flag.location_identifiers) + " " + str(len(hardcoded_flag.location_identifiers)))
            if len(hardcoded_flag.location_identifiers) != len(identifiers.location_identifiers):
                break
            is_matching = True
            # Does the identifiers match?
            for iden_given, iden_hard in zip(identifiers, hardcoded_flag.location_identifiers):
                if iden_given is not iden_hard:
                    is_matching = False
            if is_matching:
                return hardcoded_flag.location

        return None # TODO no matching flag found

    # Takes a list of flags and returns two of them
    # These should be picked with a specific policy
    # TODO Improve to select closest flags?
    def pick_two_falgs(self, flags):
        chosen_flags = []
        if len(flags) < 2:
            print("Error choosing two flags. Given list only contains amount of flags: " + str(len(flags)))
            print(RuntimeError())

        print("Number of given flags: " + str(len(flags)))
        print("Flags: " + str(flags))

        chosen_flags.append(flags[0])
        chosen_flags.append(flags[1])

        return chosen_flags



    # Returns the coordinates of the third point in a triangle.
    # Params: x0, y0 = point A and r0 is its distance to the point C (unknown location)
    # Params: x1, y1 = point B and r1 is its distance to the point C (unknown location)
    # https://stackoverflow.com/questions/55816902/finding-the-intersection-of-two-circles
    @staticmethod
    def get_intercetions(x0, y0, r0, x1, y1, r1):
        # circle 1: (x0, y0), radius r0
        # circle 2: (x1, y1), radius r1

        d = math.sqrt((x1 - x0) ** 2 + (y1 - y0) ** 2)

        # non intersecting
        if d > r0 + r1:
            return None
        # One circle within other
        if d < abs(r0 - r1):
            return None
        # coincident circles
        if d == 0 and r0 == r1:
            return None
        else:
            a = (r0 ** 2 - r1 ** 2 + d ** 2) / (2 * d)
            h = math.sqrt(r0 ** 2 - a ** 2)
            x2 = x0 + a * (x1 - x0) / d
            y2 = y0 + a * (y1 - y0) / d
            x3 = x2 + h * (y1 - y0) / d
            y3 = y2 - h * (x1 - x0) / d

            x4 = x2 - h * (y1 - y0) / d
            y4 = y2 + h * (x1 - x0) / d

            return [x3, y3, x4, y4]


class SeeObjectType(Enum):
    FLAG = 1
    PLAYER = 2
    GOAL = 3
    UNKNOWN = 4  # Identifiers: F


class SeeDataObject:
    obj_type = SeeObjectType
    location_identifiers = []  # b | r | l | c
    direction = None
    distance = None
    last_part_numbers_array = []  # todo temp - to be handled

    def __init__(self):
        self.location_identifiers = []
        self.last_part_numbers_array = []
        self.direction = None
        self.distance = None


class HardcodedFlag:
    flag_type = SeeObjectType
    location_identifiers = []  # b | r | l | c
    location = []

    def __init__(self, x, y, identifiers):
        self.location = [x, y]
        self.location_identifiers = identifiers
