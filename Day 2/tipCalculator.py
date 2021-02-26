#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
#HINT 1: https://www.google.com/search?q=how+to+round+number+to+2+decimal+places+python&oq=how+to+round+number+to+2+decimal
#HINT 2: https://www.kite.com/python/answers/how-to-limit-a-float-to-two-decimal-places-in-python

print("Welcome to the tip calculator!")

total_bill = float(input("Please, enter the total amount of your bill: "))
tip_percentage = float(input("What percentage would you like to leave as a tip? "))
people_to_split = float(input("How many people do you want to split the bill with? "))

total_to_pay =total_bill * (1 + (tip_percentage / 100))
total_to_pay_per_person = round(total_to_pay / people_to_split, 2)
total_to_pay_per_person = "{:.2f}".format(total_to_pay_per_person)

print(f"Each person should pay: {total_to_pay_per_person} CU")
