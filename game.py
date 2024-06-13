class Game:
    def guess(self, guess_number):
        if guess_number is None:
            raise ValueError

        if len(guess_number) != 3:
            raise ValueError
