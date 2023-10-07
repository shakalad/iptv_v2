

class NotEnoughMoneyException(Exception):
    def __init__(self, message="Not Enough Money on Admin Account!"):
        self.message = message
        super().__init__(self.message)
