# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%204&url=worlds%2Ftutorial_en%2Fhurdle4.json
def turn_right():
    turn_left()
    turn_left()
    turn_left()

#right_is_clear() wall_on_right()
#front_is_clear() or wall_in_front(), at_goal(),
while at_goal() != True:
    if front_is_clear() and right_is_clear():
            turn_right()
    if wall_in_front():
        if right_is_clear():
            turn_right()
        else:
            turn_left()
    if front_is_clear():
        move()
