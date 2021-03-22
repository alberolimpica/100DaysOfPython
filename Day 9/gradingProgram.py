#In this exercise we'll practice the use of dictionaries, how to create and populate them.
student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}

student_grades = {}

student_grades= {}
for student in student_scores:
  if int(student_scores[student]) >= 91:
    student_grades[student] = "Outstanding"
  elif int(student_scores[student]) >= 81:
    student_grades[student] = "Exceeds Expectations"
  elif int(student_scores[student]) >= 71:
    student_grades[student] = "Acceptable"
  elif int(student_scores[student]) < 71:
    student_grades[student] = "Fail"
    
print(student_grades)
