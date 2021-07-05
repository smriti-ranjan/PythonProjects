import random

rock = ''' rock
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = ''' paper
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = ''' scissors
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


print("Rock wins against scissors.\nScissors win against paper.\nPaper wins against rock.")
rps = [rock, paper, scissors]
user_choice = int(input("What do you choose?\tType 0 for Rock, 1 for Paper and 2 for Scissors.\n"))

if user_choice>=3 or user_choice<0:
  print("Invalid choice")
else:
  print(rps[user_choice])

computer_choice = random.randint(0,2)
print(rps[computer_choice])

if user_choice==0 and computer_choice == 2: 
  print("You won!")
elif user_choice==2 and computer_choice == 1: 
  print("You won!")
elif user_choice==1 and computer_choice == 0: 
  print("You won!")
elif user_choice==computer_choice: 
  print("Its a tie!")  
else: 
  print("You lose!")

