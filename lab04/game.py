''' Rock Paper Scissors
fall of 2014
lab04
@authors Jake Schott (jps29) and Ethan Clark (elc3)
'''

#Import random functions
import random

#Ask user for their rock, paper, scissors choice.
user_choice = int(input("Please enter 0 for rock, 1 for paper, or 2 for scissors:"))
computer_choice = random.randint(0,2)

#Determine who is the winner!!!
if user_choice == 0: 
    if computer_choice is 1:
        print("Computer wins!")
    elif computer_choice is 2:
        print("You win!")
    else: 
        print("It is a draw!")
elif user_choice == 1: 
    if computer_choice == 2:
        print("Computer wins!")
    elif computer_choice == 0:
        print("You win!")
    else:
        print("It is a draw!")
else:
    if computer_choice == 0:
        print("Computer wins!")
    elif computer_choice == 1:
        print("You win!")
    else:
        print("It is a draw!")