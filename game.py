


#
# todo: write some Python code here to satisfy the exercise objectives
# ... https://github.com/prof-rossetti/intro-to-python/blob/main/exercises/rock-paper-scissors/README.md
#
print("Welcome Player 1 to my Rock-Paper-Scissors game...")

# ASK FOR USER INPUT

user_choice = input("Please choose either 'rock', 'paper', or 'scissors': ").casefold()

# VALIDATE USER INPUTS

#this stores the valid choices in a list
valid_choices = ['rock', 'paper', 'scissors']

#this exits the program if the user doesn't enter one of the valid choices
if user_choice in valid_choices:
    print("YOU CHOSE:", user_choice)
else:
    print("Oops, incorrect entry. Please try again.")
    exit()


# COMPUTER CHOICE
#this randomizes the computer's choice and assigns the choice to a variable
import random
computer_choice = random.choice(valid_choices)
print("THE COMPUTER CHOSE:", computer_choice)



# DETERMINE THE WINNER

if user_choice == computer_choice:
    print("The game ends in a tie.")
elif ((user_choice == "rock") and (computer_choice == "scissors")):
        print("You won! since", user_choice, "beats", computer_choice)
elif ((user_choice == "paper") and (computer_choice == "rock")):
        print("You won! since", user_choice, "beats", computer_choice)
elif ((user_choice == "scissors") and (computer_choice == "paper")):
        print("You won! since", user_choice, "beats", computer_choice)
elif ((user_choice == "rock") and (computer_choice == "paper")):
        print("Bummer, the computer won since", computer_choice, "beats", user_choice)
elif ((user_choice == "scissors") and (computer_choice == "rock")):
        print("Bummer, the computer won since", computer_choice, "beats", user_choice)
elif ((user_choice == "paper") and (computer_choice == "scissors")):
        print("Bummer, the computer won since", computer_choice, "beats", user_choice)




# FINAL RESULTS
