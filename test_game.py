from unittest import TestCase

from game import Game


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
