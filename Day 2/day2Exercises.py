#We learnt how to play with different types of data and some basic operations

two_digit_number = input("Type a two digit number: ")

result = int(two_digit_number[0]) + int(two_digit_number[1]) 
print(result)

print("BMI calculator")
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

bmi = int(float(weight) / (float(height)**2))
print(bmi)


print("Time until 90 calculator")
age = input("What is your current age?")

years_until_90 = 90 - int(age)

result_in_days = years_until_90 * 365
result_in_weeks = years_until_90 * 52
result_in_months = years_until_90 * 12

print(f"You have {result_in_days} days, {result_in_weeks} weeks, or {result_in_months} months left until you turn 90")
