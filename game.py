


#
# todo: write some Python code here to satisfy the exercise objectives
# ... https://github.com/prof-rossetti/intro-to-python/blob/main/exercises/rock-paper-scissors/README.md
#


# ASK FOR USER INPUT

user_choice = input("Please enter either 'rock', 'paper', or 'scissors': ")


# VALIDATE USER INPUTS

#this makes the input case insensitive to validate whether the input is correct, and exits the program
#for a bad input
if user_choice.casefold() in ['rock', 'paper', 'scissors']:
    print("USER CHOSE:", user_choice)
else:
    print("Incorrect entry. Please try again.")
    exit()


# COMPUTER CHOICE


# DETERMINE THE WINNER




# FINAL RESULTS
