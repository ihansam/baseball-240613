class Game:
    def guess(self, guess_number):
        if guess_number is None:
            raise ValueError

        if len(guess_number) != 3:
            raise ValueError

        for number in guess_number:
            if not ord('0') <= ord(number) <= ord('9'):
                raise ValueError

        if len(set(guess_number)) != 3:
            raise ValueError
