#In this exercise we'll practice the use of the for loops, so we cannot use len() or sum()

student_heights = input("Input a list of student heights separated by a space ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

total_students = 0
total_heights = 0
for heights in student_heights:
  total_students += 1
  total_heights += heights

print(int(total_heights/total_students))
