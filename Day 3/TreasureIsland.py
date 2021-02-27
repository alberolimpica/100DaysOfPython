print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 
cross_road = input("You are at a cross road. Where do you want to go, left or right? (Type L or R)")
if not(cross_road.lower() == 'l'):
  print("Sadly you fall into a hole...")
  print("GAME OVER")

else:
  crossing_the_lake = input("You come to  lake. There's an island on the middle of the lake. Do you wait for the boat or your rather swim across? (Type W for wait or S for swim)")
  if not(crossing_the_lake.lower() == 'w'):
    print("Oh, no! You are attacked by a trout :o")
    print("GAME OVER")
  else:
    colors = input("You made it to the island! Now, there's a house with three doors with three different colors, Blue, Red and Yellow, which one would you like to open? (Type B for blue, R for red or Y for yellow")
    if colors.lower() == 'b':
      print("You open the blue door and get inside the house. The room is dark and you can't see anything. You keep walking inside the house trying to figure out where the light switch is. Everything is dark and quiet. All of the sudden you feel a warm breez in your neck, you turn around and a group of wild beast are staring at you. You get attacked by them")
      print("GAME OVER")

    elif colors.lower() == 'b':
      print("You open the door and get inside the house. You can't see anithing inside. All of the sudden, the room catch on fire. You are unable to leave. Saddly... this is the end...")
      print("GAME OVER")
    elif colors.lower() == 'y':
      print("You open the yellow door. You enter and find a nice and warm house. In the kitchen there's some fresh apple pie with tea ready for a mid afternoon snack. You rest a couple of minutes while you refuel your energy with such a delightful treats. You keep digging into the house and find an old trunk. You force the rusty locker and open it. What's inside is beyond what you could imagine!")
      print("Well done! You got the treasure!")
    else: 
      print("The night falls and is very dark and cold. The night beasts come out in search for something to eat. You hear some steps approaching you, you panic and try to run for your life. In the harbor you see the boat that took you here, you keep running towards it hoping to escape the island. Soon you realize this place is not longer what you thought it was. The boat seems to have aged a couple of years, there's rust everywhere, the ropes are spoiled and you can see a big crack on the prow. What seemed to be your escape ticket from this nightmare turned out to be the proof that some kind of dark forces acting on the island ")
      print("GAME OVER")

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload
