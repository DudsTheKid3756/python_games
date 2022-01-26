class Card:
    def __init__(self, suite, value):
        self.suite = suite
        self.value = value
        self.name = f'{value[1]} of {suite}'


suites = {
    "Hearts",
    "Diamonds",
    "Clubs",
    "Spades"
}

values = {
    (1, "Ace"),
    (2, "Two"),
    (3, "Three"),
    (4, "Four"),
    (5, "Five"),
    (6, "Six"),
    (7, "Seven"),
    (8, "Eight"),
    (9, "Nine"),
    (10, "Ten"),
    (11, "Jack"),
    (12, "Queen"),
    (13, "King")
}
