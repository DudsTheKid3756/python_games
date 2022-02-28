import random

from main.setup.card_games import card

with open("strings.txt") as f:
    lines = f.readlines()

suites = [lines[i].strip() for i in range(1, 5)]
words = [lines[i].strip() for i in range(7, 20)]
values = [(words.index(word) + 1, word) for word in words]
Card = card.Card


def shuffle(deck):
    """shuffles deck"""
    random.shuffle(deck)
    return deck


def create_deck():
    """creates deck of shuffled cards"""
    deck = [Card(suite, value) for suite in suites for value in values]
    return shuffle(deck)
