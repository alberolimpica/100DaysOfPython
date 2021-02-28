#In this lesson we practice how to print and get data in Python. We also learnt about data types and some basic functions, like how to stringify a number,
#or what's the length of a string, how to deal with variables and switching its values
print("Day 1 - Python Print Function")
print("The function is declared like this:")
print("print('what to print')")

print("There are " + str(len(input("What's your name? "))) + " letters in your name")

name = input("What is your name?")
length = len(name)
print(length)

a = input("a: ")
b = input("b: ")

aux = a
a = b
b = aux 
