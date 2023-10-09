# Egzamin p-101
# Tic Tac Toe

import random
winning_combinations = ['123', '456', '789', '147', '258', '369', '159', '357']
board_numbers = [num for num in range(1,10)]
numbers = [str(numbers) for numbers in range(1,10)]
player_x_numbers = []
player_o_numbers = []
def print_board():
    print(f'''
    {board_numbers[0]} | {board_numbers[1]} | {board_numbers[2]}
    - - - - -
    {board_numbers[3]} | {board_numbers[4]} | {board_numbers[5]}
    - - - - -
    {board_numbers[6]} | {board_numbers[7]} | {board_numbers[8]}
    ''')    
def check_winner(player, player_numbers):
    for combination in winning_combinations:
        if set([num for num in combination]).issubset(set(player_numbers)):
            print(f"Player {player} wins!")
            return True
    if set(board_numbers) == set(['X', 'O']):
        print("It's a draw")
        return True
def game_options(prompt, option1, option2):
    while True:
        user_input = input(prompt).upper()
        if user_input in [option1, option2]:
            break
        else:
            print("Wrong input, try again.")
    return user_input
def player_field_numbers(player, move):
    if player == 'X':
        player_x_numbers.append(str(move))
        return player_x_numbers
    else:
        player_o_numbers.append(str(move))
        return player_o_numbers
def make_move(player):
    while True:
        move = input(f"Player {player} choose board number (1-9): ")
        if move in numbers and (board_numbers[int(move)-1] not in ['X', 'O']):
            board_numbers[int(move)-1] = player
            player_numbers = player_field_numbers(player, move)
            break
        else:
            print("Wrong input or field already occupied. Try again!")
    print(f"Player {player} chose {move}")
    print_board()
    if check_winner(player, player_numbers) == True:
        return True
def computer_move(computer):
    move = str(random.choice(board_numbers))
    while move in ['X', 'O']:
        move = str(random.choice(board_numbers))
    board_numbers[int(move)-1] = computer
    player_numbers = player_field_numbers(computer, move)
    print(f"Computer chose {move}.")
    print_board()
    if check_winner(computer, player_numbers) == True:
        return True
print("Welcome to Tic Tac Toe game.")
game_type = game_options("Which game would you like to play? Enter '1' for player vs player or '2' for player vs computer: ", '1', '2')
player_one = game_options("Player please choose 'X' or 'O' to play: ", 'X', 'O')
if player_one == 'X':
    player_two = 'O'
else:
    player_two = 'X'
print_board()
while True:
    if make_move(player_one) == True:
        break
    if game_type == '2':
        if computer_move(player_two) == True:
            break
    else:
        if make_move(player_two) == True:
            break