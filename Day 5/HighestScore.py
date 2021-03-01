# in this exercise we'll keep practicing the for loop. We aren't allowed to use the max() function
student_scores = input("Input a list of student scores, each one separated by a space: ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)

highest_score = 0
for score in student_scores:
  if highest_score < score:
    highest_score = score

print(f"The highest score in the class is: {highest_score}")
