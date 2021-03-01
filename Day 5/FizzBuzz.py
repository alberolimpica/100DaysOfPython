#This is one of the most asked questions in programming interviews, the FizzBuzz. 
#Print all numbers from 1 to 100 and when a number is divisible by 3 it should print Fizz, 
#if is divisible by 5 it should print Buzz and if is divisible by 3 AND 5 it should print FizzBuzz

for number in range(1, 101):
  if number % 3 == 0 and number % 5 == 0:
    print("Fizz Buzz")
  elif number % 3 == 0:
    print("Fizz")
  elif number % 5 == 0:
    print("Buzz")
  else:
    print(number)

