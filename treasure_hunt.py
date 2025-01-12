from art import logo_treasure_hunt

print(logo_treasure_hunt)
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
#First Obstacle
choice1 = input("You have reached the first obstacle!"
                "\nYou're at a crossroad."
                "\n      Type 'left' to go left and 'right' to go right\n").lower()

if choice1 == "left":
    choice2 = input("You have reached a river! There is an island in the middle of the river."
                    "\n      Type 'wait' to wait for a boat! or 'swim' if you want to swim across the river!!\n").lower()

    if choice2 == "wait":
        #Final Obstacle
        choice3 = input("You have reached the island and entered the building on the island."
                        "\n      You have three doors in front of you: red, blue and yellow!"
                        "\n      Type which one of them you want to go through!\n").lower()
        if choice3 == "yellow":
            print("You Won! The treasure is right before you!")
        elif choice3 == "red":
            print("You have been Burned by fire!!\nGAME OVER!!!")
        elif choice3 == "blue":
            print("You have been Eaten by Beasts.\nGAME OVER!!!")
        else:
            print("Game Over!!!")
    else:
        print("You were impatient and have been attacked by trout!!\nGAME OVER!!!")
else:
    print("You didn't see where you were going! You fell into a hole and perished!!\nGAME OVER!!!")
