import os


class Deck:
    lines = []
    suites = []

    class Card:
        def __init__(self, suite, value):
            self.suite = suite
            self.value = value
            self.name = f'{value[1]} of {suite}'

    def __init__(self):
        script_dir = os.path.dirname(__file__)
        rel_path = "strings.txt"
        abs_file_path = os.path.join(script_dir, rel_path)
        with open(abs_file_path, 'r') as f:
            lines = f.readlines()

        self.suites = [lines[i].strip() for i in range(1, 5)]
        words = [lines[i].strip() for i in range(7, 20)]
        values = [(words.index(word) + 1, word) for word in words]
        self.deck = [self.Card(suite, value) for suite in self.suites for value in values]
