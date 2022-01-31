


#
# FYI: this is to satisfy the OPTIONAL testing challenge objectives
# ... https://github.com/prof-rossetti/intro-to-python/blob/main/exercises/rock-paper-scissors/challenges.md
#

from game import determine_winner


def test_determination_of_the_winner():

    assert determine_winner("rock", "rock") == "Tie game"
    assert determine_winner("paper", "paper") == "Tie game"
    assert determine_winner("scissors", "scissors") == "Tie game"

    assert determine_winner("paper", "rock") == "You win"
    assert determine_winner("rock", "scissors") == "You win"
    assert determine_winner("scissors", "paper") == "You win"

    assert determine_winner("rock", "paper") == "Bummer, computer wins"
    assert determine_winner("paper", "scissors") == "Bummer, computer wins"
    assert determine_winner("scissors", "rock") == "Bummer, computer wins"
