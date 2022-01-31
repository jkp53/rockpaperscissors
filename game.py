


#
# todo: write some Python code here to satisfy the exercise objectives
# ... https://github.com/prof-rossetti/intro-to-python/blob/main/exercises/rock-paper-scissors/README.md


#Player Name Customization

import os

player_name = os.getenv("PLAYER_NAME", default="Player One")

# todo: write some Python here to determine the winner
def determine_winner(user_choice, computer_choice):
        if (user_choice == computer_choice):
                return "Tie game"
        elif ((user_choice == "rock") and (computer_choice == "scissors")):
                return "You win"
        elif ((user_choice == "paper") and (computer_choice == "rock")):
                return("You win")
        elif ((user_choice == "scissors") and (computer_choice == "paper")):
                return("You win")
        elif ((user_choice == "rock") and (computer_choice == "paper")):
                return("Bummer, computer wins")
        elif ((user_choice == "scissors") and (computer_choice == "rock")):
                return("Bummer, computer wins")
        elif ((user_choice == "paper") and (computer_choice == "scissors")):
                return("Bummer, computer wins")


if __name__ == "__main__":

    print("Welcome", player_name, "to my Rock-Paper-Scissors game...")

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

    print(determine_winner(user_choice, computer_choice))


    # FINAL RESULTS

    print("Thanks for playing. Please play again!")
