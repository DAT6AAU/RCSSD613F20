import math

# Returns the coordinates of the third point in a triangle.
def get_thrid_point(ac_length, bc_length, a_coord, b_coord):

    #ab_length = 0  #TODO

    ab = (a_coord[0] + b_coord[0]) * (a_coord[1] + b_coord[1])  # TODO
    #ab = (a_coord[0] * b_coord[0]) + (a_coord[1] * b_coord[1])  # TODO
    print("ab: " + str(ab))

    c_y = (math.pow(ab, 2) + math.pow(ac_length, 2) - math.pow(bc_length, 2)) / (2 * ab)
    c_x = math.sqrt(math.pow(ac_length, 2) - math.pow(c_y, 2))  # +/-

    return [c_x, c_y]


# https://stackoverflow.com/questions/55816902/finding-the-intersection-of-two-circles
def get_intercetions(x0, y0, r0, x1, y1, r1):
    # circle 1: (x0, y0), radius r0
    # circle 2: (x1, y1), radius r1

    d = math.sqrt((x1-x0)**2 + (y1-y0)**2)

    # non intersecting
    if d > r0 + r1:
        return None
    # One circle within other
    if d < abs(r0-r1):
        return None
    # coincident circles
    if d == 0 and r0 == r1:
        return None
    else:
        a = (r0**2-r1**2+d**2)/(2*d)
        h = math.sqrt(r0**2-a**2)
        x2 = x0+a*(x1-x0)/d
        y2 = y0+a*(y1-y0)/d
        x3 = x2+h*(y1-y0)/d
        y3 = y2-h*(x1-x0)/d

        x4 = x2-h*(y1-y0)/d
        y4 = y2+h*(x1-x0)/d

        return [x3, y3, x4, y4]

#result = get_thrid_point(14, 14, [0,0], [0,4])
result = get_intercetions(0, 0, 14, 0, 4, 14)

print(result)
