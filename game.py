from game_result import GameResult


class Game:
    def __init__(self):
        self.question = ""

    def guess(self, guess_number) -> GameResult:
        self.assert_illegal_value(guess_number)
        if guess_number == self.question:
            return GameResult(True, 3, 0)

    def assert_illegal_value(self, guess_number):
        if guess_number is None:
            raise ValueError
        if len(guess_number) != 3:
            raise ValueError
        for number in guess_number:
            if not ord('0') <= ord(number) <= ord('9'):
                raise ValueError
        if self.has_duplicate_number(guess_number):
            raise ValueError

    @staticmethod
    def has_duplicate_number(guess_number):
        return len(set(guess_number)) != 3
