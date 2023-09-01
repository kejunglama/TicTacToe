import unittest
from unittest.mock import patch
from tic_tac_toe import *


class TestTicTacToe(unittest.TestCase):
    # Get random player
    def test_get_random_player_returns_player_in_list(self):
        players = ["Alice", "Bob"]
        player = get_random_player(players)
        self.assertIn(player, players)

    def test_get_random_player_returns_random_player(self):
        players = ["Alice", "Bob"]
        players = set([get_random_player(players) for i in range(100)])
        self.assertEqual(len(players), 2)

    # Select difficulty
    @patch("builtins.input", side_effect=["easy"])
    def test_select_difficulty_easy(self, mock_input):
        self.assertEqual(select_difficulty(), "easy")

    @patch("builtins.input", side_effect=["hard"])
    def test_select_difficulty_hard(self, mock_input):
        self.assertEqual(select_difficulty(), "hard")

    @patch("builtins.input", side_effect=["invalid", "hard"])
    def test_select_difficulty_invalid_then_hard(self, mock_input):
        self.assertEqual(select_difficulty(), "hard")

    @patch("builtins.input", side_effect=["a", "rgd", "i2345", "invalid", "hard"])
    def test_select_difficulty_invalid_then_hard(self, mock_input):
        self.assertEqual(select_difficulty(), "hard")

    # get move computer
    def test_get_computer_move_global_range(self):
        board = ["1", "2", "4", "4", "5", "6", "7", "8", "9"]
        move = get_computer_move(board)
        self.assertIn(move, range(9))

    def test_get_computer_move_valid_range(self):
        board = ["1", "X", "X", "O", "O", "X", "O", "8", "9"]
        move = get_computer_move(board)
        self.assertIn(move, [0, 7, 8])
        board = ["1", "2", "X", "O", "5", "6", "O", "8", "9"]
        move = get_computer_move(board)
        self.assertIn(move, [0, 1, 4, 5, 7, 8])

    # get move user
    def test_get_user_move_valid(self):
        with patch("builtins.input", return_value="5"):
            board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
            self.assertEqual(get_user_move("bob", board), 4)
        with patch("builtins.input", return_value="9"):
            board = ["1", "X", "3", "4", "5", "6", "O", "8", "9"]
            self.assertEqual(get_user_move("bob", board), 8)

    def test_get_user_move_already_taken(self):
        with patch("builtins.input", side_effect=["2", "1"]):
            board = ["1", "X", "3", "4", "5", "6", "7", "8", "9"]
            self.assertEqual(get_user_move("bob", board), 0)
        with patch("builtins.input", side_effect=["2", "3", "4", "5", "6", "7", "8"]):
            board = ["1", "X", "X", "O", "O", "X", "O", "8", "9"]
            self.assertEqual(get_user_move("bob", board), 7)

    def test_get_user_move_out_of_range(self):
        with patch("builtins.input", side_effect=["0", "10", "9"]):
            board = ["O", "X", "3", "4", "5", "6", "7", "8", "9"]
            self.assertEqual(get_user_move("bob", board), 8)
        with patch("builtins.input", side_effect=["234567890", "-1", "7"]):
            board = ["O", "X", "3", "O", "X", "6", "7", "8", "9"]
            self.assertEqual(get_user_move("bob", board), 6)

    def test_get_user_move_non_numeric(self):
        with patch(
            "builtins.input", side_effect=["abc", "a234", "2Zaez", "hello", "3"]
        ):
            board = ["O", "X", "3", "4", "O", "X", "7", "8", "X"]
            self.assertEqual(get_user_move("bob", board), 2)

    # get move general
    def test_get_move_computer_easy(self):
        board = ["X", "2", "O", "4", "X", "6", "O", "8", "9"]
        self.assertIn(get_move("computer", board, "easy"), [1, 3, 5, 7, 8])

    def test_get_move_computer_hard(self):
        board = ["X", "2", "O", "4", "X", "6", "O", "8", "9"]
        self.assertEqual(get_move("computer", board, "hard"), 8)

    def test_get_move_user(self):
        with unittest.mock.patch("builtins.input", return_value="4"):
            board = ["X", "2", "O", "3", "4", "5", "6", "8", "9"]
            self.assertEqual(get_move("bob", board), 3)

    # Best move tests
    def test_get_best_move_block_win_1(self):
        board = ["1", "X", "3", "4", "O", "O", "7", "X", "9"]
        best_move = get_best_move(board)
        self.assertEqual(best_move, 3)

    def test_get_best_move_block_win_2(self):
        board = ["O", "X", "3", "4", "O", "6", "7", "X", "9"]
        best_move = get_best_move(board)
        self.assertEqual(best_move, 8)

    def test_get_best_move_can_win_1(self):
        board = ["O", "X", "O", "4", "5", "6", "7", "X", "9"]
        best_move = get_best_move(board)
        self.assertEqual(best_move, 4)

    def test_get_best_move_can_win_2(self):
        board = ["X", "X", "O", "O", "X", "6", "7", "O", "9"]
        best_move = get_best_move(board)
        self.assertEqual(best_move, 8)

    # update board
    def test_update_board_with_player_O(self):
        board = ["X", "X", "O", "O", "X", "6", "7", "O", "9"]
        move = 8
        player = "bob"
        update_board(move, player, board)
        self.assertEqual(board, ["X", "X", "O", "O", "X", "6", "7", "O", "O"])

    def test_update_board_with_player_X(self):
        board = ["X", "X", "O", "O", "X", "6", "7", "O", "9"]
        move = 5
        player = "computer"
        update_board(move, player, board)
        self.assertEqual(board, ["X", "X", "O", "O", "X", "X", "7", "O", "9"])

    # switch players
    def test_switch_player(self):
        players = ("computer", "player2")
        next_player = switch_player("computer", players)
        self.assertEqual(next_player, "player2")
        next_player = switch_player("player2", players)
        self.assertEqual(next_player, "computer")

    # Vertical wins
    def test_check_win_vertical_left_O(self):
        board = ["O", "2", "X", "O", "X", "6", "O", "8", "X"]
        result = check_win(board)
        self.assertTrue(result)

    def test_check_win_vertical_middle_O(self):
        board = ["X", "O", "X", "4", "O", "6", "7", "O", "X"]
        result = check_win(board)
        self.assertTrue(result)

    def test_check_win_vertical_right_O(self):
        board = ["X", "X", "O", "4", "5", "O", "7", "X", "O"]
        result = check_win(board)
        self.assertTrue(result)

    def test_check_win_vertical_left_X(self):
        board = ["X", "2", "O", "X", "O", "6", "X", "O", "9"]
        result = check_win(board)
        self.assertTrue(result)

    def test_check_win_vertical_middle_X(self):
        board = ["1", "X", "O", "4", "X", "6", "O", "X", "O"]
        result = check_win(board)
        self.assertTrue(result)

    def test_check_win_vertical_right_X(self):
        board = ["1", "2", "X", "4", "O", "X", "O", "O", "X"]
        result = check_win(board)
        self.assertTrue(result)

    # Horizontal wins
    def test_check_win_horizontal_top_X(self):
        board = ["X", "X", "X", "4", "O", "O", "7", "O", "9"]
        result = check_win(board)
        self.assertTrue(result)

    def test_check_win_horizontal_middle_X(self):
        board = ["1", "O", "O", "X", "X", "X", "O", "8", "9"]
        result = check_win(board)
        self.assertTrue(result)

    def test_check_win_horizontal_bottom_X(self):
        board = ["O", "2", "3", "O", "O", "X", "X", "X", "X"]
        result = check_win(board)
        self.assertTrue(result)

    def test_check_win_horizontal_top_O(self):
        board = ["O", "O", "O", "4", "X", "X", "X", "O", "X"]
        result = check_win(board)
        self.assertTrue(result)

    def test_check_win_horizontal_middle_O(self):
        board = ["1", "X", "X", "O", "O", "O", "O", "X", "9"]
        result = check_win(board)
        self.assertTrue(result)

    def test_check_win_horizontal_bottom_O(self):
        board = ["O", "X", "X", "X", "5", "X", "O", "O", "O"]
        result = check_win(board)
        self.assertTrue(result)

    # Diagonal wins
    def test_check_win_diagonal_left_O(self):
        board = ["O", "O", "X", "X", "O", "X", "O", "X", "O"]
        result = check_win(board)
        self.assertTrue(result)

    def test_check_win_diagonal_right_O(self):
        board = ["O", "2", "O", "X", "O", "6", "O", "X", "X"]
        result = check_win(board)
        self.assertTrue(result)

    def test_check_win_diagonal_right_X(self):
        board = ["O", "O", "X", "X", "X", "O", "X", "8", "O"]
        result = check_win(board)
        self.assertTrue(result)

    def test_check_win_diagonal_left_X(self):
        board = ["X", "O", "O", "O", "X", "X", "O", "8", "X"]
        result = check_win(board)
        self.assertTrue(result)

    # No wins
    def test_check_no_win_1(self):
        board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        result = check_win(board)
        self.assertFalse(result)

    def test_check_no_win_2(self):
        board = ["1", "2", "3", "4", "X", "6", "7", "8", "9"]
        result = check_win(board)
        self.assertFalse(result)

    def test_check_no_win_3(self):
        board = ["1", "X", "3", "4", "5", "O", "7", "8", "9"]
        result = check_win(board)
        self.assertFalse(result)

    def test_check_no_win_4(self):
        board = ["1", "X", "3", "4", "5", "O", "7", "O", "9"]
        result = check_win(board)
        self.assertFalse(result)

    def test_check_no_win_5(self):
        board = ["O", "X", "3", "4", "O", "O", "7", "X", "9"]
        result = check_win(board)
        self.assertFalse(result)

    # Check tie
    def test_check_tie(self):
        board = ["X", "O", "X", "O", "X", "O", "O", "X", "O"]
        result = check_tie(board)
        self.assertTrue(result)

    def test_check_not_tie(self):
        board = ["1", "O", "X", "O", "X", "O", "O", "X", "O"]
        result = check_tie(board)
        self.assertFalse(result)

    # check game over
    def test_game_over_tie(self):
        board = ["X", "O", "X", "O", "X", "O", "O", "X", "O"]
        result = game_over(board)
        self.assertTrue(result)

    def test_game_over_win(self):
        board = ["X", "O", "X", "O", "X", "O", "O", "8", "X"]
        result = game_over(board)
        self.assertTrue(result)

    def test_game_over_no_win(self):
        board = ["X", "O", "X", "O", "5", "O", "O", "X", "9"]
        result = game_over(board)
        self.assertFalse(result)


if __name__ == "__main__":
    unittest.main()
