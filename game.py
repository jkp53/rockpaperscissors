


#
# todo: write some Python code here to satisfy the exercise objectives
# ... https://github.com/prof-rossetti/intro-to-python/blob/main/exercises/rock-paper-scissors/README.md
#


# ASK FOR USER INPUT

user_choice = input("Please enter either 'rock', 'paper', or 'scissors': ")



# VALIDATE USER INPUTS

#this stores the valid choices in a list
valid_choices = ['rock', 'paper', 'scissors']
#this makes the input case insensitive to validate whether the input is correct, and exits the program
#for a bad input
if user_choice.casefold() in valid_choices:
    print("USER CHOSE:", user_choice)
else:
    print("Incorrect entry. Please try again.")
    exit()


# COMPUTER CHOICE
#this randomizes the computer's choice and assigns the choice to a variable
import random
computer_choice = random.choice(valid_choices)
print("COMPUTER CHOSE:", computer_choice)



# DETERMINE THE WINNER




# FINAL RESULTS
