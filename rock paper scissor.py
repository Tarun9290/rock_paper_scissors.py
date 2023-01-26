
#Rock-Paper-Scissors:
#
#Create a program that plays the game rock-paper-scissors against the user. 
#The program should prompt the user for their choice (rock, paper, or scissors), 
#and then randomly generate its own choice.
#The program should then determine the winner and print the result.



import random

while True:
    user_choice = input("Rock, paper, or scissors? (q to quit) ")

    if user_choice == "q":
        break
    elif user_choice not in ["rock", "paper", "scissors"]:
        print("Invalid choice.")
        continue

    # generate computer's choice
    computer_choice = random.choice(["rock", "paper", "scissors"])

    # determine winner
    if user_choice == computer_choice:
        print("Tie!")
    elif user_choice == "rock" and computer_choice == "scissors":
        print("You win!")
    elif user_choice == "paper" and computer_choice == "rock":
        print("You win!")
    elif user_choice == "scissors" and computer_choice == "paper":
        print("You win!")
    else:
        print("You lose.")
