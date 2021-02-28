import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
rock_paper_scissors = [rock, paper, scissors]

print("Welcome to the rock - paper - scissors game!")
print("You will be playing against the computer")
users_choice = int(input("Please, choose one of the following options: \n Type 1 for rock \n Type 2 for paper \n Type 3 for scissors \n"))

computers_choice = random.randint(1, 3)
if users_choice >= 1 and users_choice <= 3:
  print(f"Your choice: \n {rock_paper_scissors[users_choice - 1]}")
  print(f"Computer's choice: \n {rock_paper_scissors[computers_choice - 1 ]}")

  if users_choice == 1:
    if computers_choice == 3:
      print("Rock beats scissors, you win!")
    else:
      print("Paper beats rock, you lost!")
  elif users_choice == 2:
    if computers_choice == 1:
      print("Paper beats rock, you win!")
    else:
      print("Scissors beat paper, you lost")
  elif users_choice == computers_choice:
    print("It is a draw!")
  elif users_choice == 3:
    if computers_choice == 1:
      print("Rock beats scissors, you lost")
    else:
      print("Scissors beat paper, you win")   
else:
  print("Wrong number!")
