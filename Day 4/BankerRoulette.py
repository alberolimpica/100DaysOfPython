#In this exercise we'll practice lists in python, and also the random module
import random
names_string = input("Give me everybody's names, separated by a comma and a space. ")
names = names_string.split(", ")
print(len(names))
person_who_pays = names[random.randint(0, len(names) - 1)]

print(f"{person_who_pays} is going to buy the meal today!")

