class Card:
    def __init__(self, suite, value):
        self.suite = suite
        self.value = value
        self.name = f'{value[1]} of {suite}'
