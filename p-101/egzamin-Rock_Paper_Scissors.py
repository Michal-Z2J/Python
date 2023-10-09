# Egzamin p-101
# Rock paper scissors

import random

def game_result(player, computer):
    if player == computer:
        print(f"Computer chose {computer}. It's a draw.")
    elif player == "rock" and computer == "scissors":
        print(f"Computer chose {computer}. Congratulations, you win!")
    elif player == "paper" and computer == "rock":
        print(f"Computer chose {computer}. Congratulations, you win!")
    elif player == "scissors" and computer == "paper":
        print(f"Computer chose {computer}. Congratulations, you win!")
    else:
        print(f"Computer chose {computer} and you lose, try again!")

moves = ["rock", "paper", "scissors"]
print("Welcome to Rock, Paper, Scissors game!")

while True:
    player_move = input("Choose your move (enter 'q' to quit): ").lower()
    computer_move = random.choice(moves)

    if player_move in moves:
        game_result(player_move, computer_move)
    elif player_move == "q":
        print("Closing program.")
        break
    else:
        print("Wrong input, try again.")