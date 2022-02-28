class Card:
    def __init__(self, suite, value):
        self.suite = suite
        self.value = value
        self.name = f'{value[1]} of {suite}'


with open("strings.txt") as f:
    lines = f.readlines()

suites = [lines[i].strip() for i in range(1, 5)]
words = [lines[i].strip() for i in range(7, 20)]
values = [(words.index(word) + 1, word) for word in words]
