from copy import deepcopy
import random
from typing import List, Tuple


def print_rules(filename: str) -> None:
    """
    Given the name of a file containing the rules of the game, prints the rules to the console.
    """
    with open(filename) as f:
        rules = f.read()
        print(rules)


def get_player_name() -> str:
    """
    Prompts the user to enter a player name and returns it.
    """
    name = input(f"Enter your name: ")
    return name


def get_random_player(players: Tuple[str]) -> str:
    """
    Given a list of players, returns one of them at random.
    """
    return random.choice(players)


def print_board(board: List[str]) -> None:
    """Prints the current state of the board"""
    print("   |   |")
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("___|___|___")
    print("   |   |")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("___|___|___")
    print("   |   |")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print("   |   |")


def select_difficulty() -> str:
    """
    Prompts the player to select the difficulty level (easy or hard), and returns the corresponding game mode.
    """
    choice = input("Select difficulty level (easy/hard): ").strip().lower()
    while choice not in ["easy", "hard"]:
        print("Invalid choice. Please enter 'easy' or 'hard'.")
        choice = input("Select difficulty level (easy/hard): ").strip().lower()
    return choice


def get_move(player: str, board: List[str], difficulty: str = "easy") -> int:
    """Gets the index of the next user move on the board, for all users and difficulties."""
    if player == "computer":
        if difficulty == "easy":
            return get_computer_move(board)
        else:
            return get_best_move(board)
    else:
        return get_user_move(player, board)


def get_user_move(player: str, board: List[str]) -> int:
    """Gets the move from the player"""
    move = input(f"Enter your move, {player.capitalize()}: ").strip()
    while (
        not move.isdigit()
        or int(move) not in range(1, 10)
        or board[int(move) - 1] in ["X", "O"]
    ):
        print("Invalid move. Please enter a number between 1 and 9.")
        move = input(f"Enter your move, {player.capitalize()}: ").strip()
    return int(move) - 1


def get_computer_move(board: List[str]) -> int:
    """Gets random move from the computer"""
    move = random.randint(1, 9)
    print(move)
    while board[move - 1] in ["X", "O"]:
        move = random.randint(1, 9)
    return move - 1


def get_best_move(board: List[str]) -> int:
    """Returns the best move for the X player on the board."""
    # Get Best Move to win the game
    for i in range(0, 9):
        if board[i] not in ["X", "O"] and int(board[i]) == i + 1:
            board_copy_x = deepcopy(board)
            board_copy_o = deepcopy(board)
            board_copy_x[i] = "X"
            board_copy_o[i] = "O"
            if check_win(board_copy_x):
                return i
            elif check_win(board_copy_o):
                return i

    return get_computer_move(board)


def update_board(move: int, player: str, board: List[str]) -> None:
    """Updates the board with the player's move"""
    print(f"{player.capitalize()} played on field {move + 1}.")
    board[move] = "X" if player == "computer" else "O"


def switch_player(player: str, players: Tuple[str]) -> str:
    """
    Given the current player and a list of players, returns the next player in the list.
    """
    return players[0] if player == players[1] else players[1]


def game_over(board: List[str]) -> bool:
    """
    Returns True if the game is over (i.e., there is a winner or a tie), and False otherwise.
    """
    return check_win(board) or check_tie(board)


def check_win(board: List[str]) -> bool:
    def check_rows(board):
        """Checks if any row has a winning pattern."""
        return any([check_row(board, i) for i in range(3)])

    def check_row(board, row):
        """Checks if a row has a winning pattern."""
        return len(set(board[row * 3 : row * 3 + 3])) == 1 and board[row * 3] != " "

    def check_columns(board):
        """Checks if any column has a winning pattern."""
        return any([check_column(board, i) for i in range(3)])

    def check_column(board, column):
        """Checks if a column has a winning pattern."""
        return (
            len(set([board[column + i * 3] for i in range(3)])) == 1
            and board[column] != " "
        )

    def check_diagonals(board):
        """Checks if any diagonal has a winning pattern."""
        return check_left_diagonal(board) or check_right_diagonal(board)

    def check_left_diagonal(board):
        """Checks if the left diagonal has a winning pattern."""
        return len(set([board[i] for i in range(0, 9, 4)])) == 1 and board[0] != " "

    def check_right_diagonal(board):
        """Checks if the right diagonal has a winning pattern."""
        return len(set([board[i] for i in range(2, 7, 2)])) == 1 and board[2] != " "

    """Checks if a figure (X or O) has a winning pattern."""
    return check_rows(board) or check_columns(board) or check_diagonals(board)


def check_tie(board: List[str]) -> bool:
    """Checks if the game is a tie"""
    return all([cell in ["X", "O"] for cell in board])


def does_game_continue() -> bool:
    """
    Prompts the player to enter "Y" or "N" to indicate whether they want to continue playing,
    and returns True if the player enters "Y", and False if the player enters "N".
    """
    choice = input("Do you want to continue playing? (Y/N) ").strip().upper()
    while choice not in ["Y", "N"]:
        print("Invalid choice. Please enter 'Y' or 'N'.")
        choice = input("Do you want to continue playing? (Y/N) ").strip().upper()
    return False if choice == "N" else True


print(True)
