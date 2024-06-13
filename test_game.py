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

    def test_return_solve_result_if_matched_number(self):
        self.game.question = "123"
        ret: GameResult = self.game.guess("123")

        self.assertIsNotNone(ret)
        self.assertTrue(ret.solved)
        self.assertEqual(3, ret.strikes)
        self.assertEqual(0, ret.balls)

    def test_return_solve_result_if_unmatched_number(self):
        self.game.question = "123"
        ret: GameResult = self.game.guess("456")

        self.assertIsNotNone(ret)
        self.assertFalse(ret.solved)
        self.assertEqual(0, ret.strikes)
        self.assertEqual(0, ret.balls)
