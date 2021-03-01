#In this exercise we'll practice the use of for loops and the range function to calculate the sum of all odd numbers from 1 to 100 

sum = 0
for number in range(1, 101):
  if number % 2 == 0:
    sum += number
print(sum)

#This could also be done like this, using the step attribute in the range function
sum = 0
for number in range(0, 101, 2):
  sum += number
print(sum)
