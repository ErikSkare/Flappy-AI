import math


# from https://stackoverflow.com/questions/24727773/detecting-rectangle-collision-with-a-circle
def collision_rect_circle(rleft, rtop, width, height,
              center_x, center_y, radius):

    rright, rbottom = rleft + width, rtop + height

    cleft, ctop     = center_x-radius, center_y-radius
    cright, cbottom = center_x+radius, center_y+radius

    if rright < cleft or rleft > cright or rbottom < ctop or rtop > cbottom:
        return False

    for x in (rleft, rleft+width):
        for y in (rtop, rtop+height):
            if math.hypot(x-center_x, y-center_y) <= radius:
                return True


    if rleft <= center_x <= rright and rtop <= center_y <= rbottom:
        return True

    return False

