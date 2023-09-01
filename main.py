from tic_tac_toe import *

# initialize variables
continue_playing = True
print_rules("rules.txt")
board = [str(i + 1) for i in range(9)]  # TO DO change to str
player = get_player_name()
players = ("computer", player)
current_player = get_random_player(players)
print_board(board)

# runs the game as long as the user does not quit
while continue_playing:
    difficulty = select_difficulty()

    board = [i + 1 for i in range(9)]  # reset board values
    print_board(board)

    # core game loop
    while not game_over(board):
        print(f"It's {current_player.capitalize()}'s turn.")
        move = get_move(current_player, board, difficulty)
        update_board(move, current_player, board)
        print_board(board)
        current_player = switch_player(current_player, players)

    # when game is over
    if check_tie(board):
        print("It's a tie!")
    else:
        current_player = switch_player(
            current_player, players
        )  # chnaged to current_player
        print(f"Player {current_player.capitalize()} wins!")

    continue_playing = does_game_continue()

print("Bye bye !")
