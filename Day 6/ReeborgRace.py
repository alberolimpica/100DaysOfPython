#In this exercise we practice the use of while loops and functions.

#to run this code we have to copy and paste it into this web page: https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%203&url=worlds%2Ftutorial_en%2Fhurdle3.json

def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def jump():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
        
while at_goal() != True:
    if front_is_clear():
        move()
    elif wall_in_front():
        jump()

