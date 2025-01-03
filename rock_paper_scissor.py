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


rand_num = random.randint(0,2)
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
print("You Chose: \n")

##User Choice
if user_choice == 0:
    print(rock)
elif user_choice == 1:
    print(paper)
elif user_choice == 2:
    print(scissors)
else:
    print("Please enter 0, 1 or 2 as your choice.")

##Computer Choice
print("Computer Chose: \n")
if rand_num == 0:
    print(rock)
elif rand_num == 1:
    print(paper)
elif rand_num == 2:
    print(scissors)

##Win Declaration if user chooses rock
if user_choice == 0 and rand_num == 0:
    print("Its a draw")
elif user_choice == 0 and rand_num == 1:
    print("You Lose!!")
elif user_choice == 0 and rand_num == 2:
    print("You Win!!")

##Win Declaration if user chooses paper
if user_choice == 1 and rand_num == 0:
    print("You Win!!")
elif user_choice == 1 and rand_num == 1:
    print("Its a draw")
elif user_choice == 1 and rand_num == 2:
    print("You Lose!!")

##Win Declaration if user chooses scissor
if user_choice == 2 and rand_num == 0:
    print("You Lose!!")
elif user_choice == 2 and rand_num == 1:
    print("You Win!!")
elif user_choice == 2 and rand_num == 2:
    print("Its a draw")