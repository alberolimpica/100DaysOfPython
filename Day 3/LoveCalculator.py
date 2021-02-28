#In this exercise we practice how to use the string functions lower() and count(), the use of the f-string to print out a value without having to convert it to a string, and the use of "and or not" operators in an if else statement. 
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

names = name1 + name2
names_to_lower_case = names.lower()
#True
true_result = names_to_lower_case.count('t')
true_result += names_to_lower_case.count('r')
true_result += names_to_lower_case.count('u')
true_result += names_to_lower_case.count('e')

#Love
love_result = names_to_lower_case.count('l')
love_result += names_to_lower_case.count('o')
love_result += names_to_lower_case.count('v')
love_result += names_to_lower_case.count('e')

result = int(str(true_result) + str(love_result))

if result < 10 or result > 90:
  print(f"Your score is {result}, you go together like coke and mentos.")
elif result >= 40 and result <= 50:
  print(f"Your score is {result}, you are alright together.")
else:
  print(f"Your score is {result}")
