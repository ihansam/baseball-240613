from unittest import TestCase

from game import Game
from game_result import GameResult


class TestGame(TestCase):
    def setUp(self):
        super().setUp()
        self.game = Game()

    def assert_raise_value_error_with_invalid_argument(self, guess_number):
        try:
            self.game.guess(guess_number)
            self.fail()
        except ValueError:  # seems more appropriate than TypeError
            pass

    def test_exception_when_invalid_input(self):
        self.assert_raise_value_error_with_invalid_argument(None)
        self.assert_raise_value_error_with_invalid_argument("12")
        self.assert_raise_value_error_with_invalid_argument("1234")
        self.assert_raise_value_error_with_invalid_argument("12s")
        self.assert_raise_value_error_with_invalid_argument("121")

    def assert_matched_number(self, ret, solved, strikes, balls):
        self.assertIsNotNone(ret)
        self.assertEqual(solved, ret.solved)
        self.assertEqual(strikes, ret.strikes)
        self.assertEqual(balls, ret.balls)

    def generate_question(self, answer):
        self.game.question = answer

    def test_return_solve_result_if_matched_number(self):
        self.generate_question("123")
        self.assert_matched_number(self.game.guess("123"), True, 3, 0)

    def test_return_solve_result_if_unmatched_number(self):
        self.generate_question("123")
        self.assert_matched_number(self.game.guess("456"), False, 0, 0)

    def test_return_solve_result_if_some_matched_number(self):
        self.generate_question("123")
        self.assert_matched_number(self.game.guess("120"), False, 2, 0)
        self.assert_matched_number(self.game.guess("061"), False, 0, 1)
        self.assert_matched_number(self.game.guess("136"), False, 1, 1)
