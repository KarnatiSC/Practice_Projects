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

images = [rock,paper,scissors]

computer_choice = random.randint(0,2)
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if  user_choice >= 0 and user_choice <= 2:
    print(f"You Chose: \n {images[user_choice]}")
else:
    print("You chose an invalid number! please choose again")


##Computer Choice
print(f"Computer Chose: \n{images[computer_choice]}")


##Rock, Paper, Scissors logic


if user_choice>=3 or user_choice < 0:
    print("You entered and invalid number. You Lose!!")
elif user_choice == 0 and computer_choice == 2:
    print("You Lose!!")
elif user_choice == 2 and computer_choice == 0:
    print("You Win!!")
elif user_choice > computer_choice:
    print("You Win!!")
elif computer_choice > user_choice:
    print("You Lose!!")
elif computer_choice == user_choice:
    print("It's a draw!")
