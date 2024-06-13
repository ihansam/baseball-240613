class GameResult:
    def __init__(self, solved, strikes, balls):
        self.__balls = balls
        self.__strikes = strikes
        self.__solved = solved

    @property
    def solved(self):
        return self.__solved

    @property
    def strikes(self):
        return self.__strikes

    @property
    def balls(self):
        return self.__balls
