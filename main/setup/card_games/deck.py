import random

from main.setup.card_games import card

values = card.values
suites = card.suites
Card = card.Card


def shuffle(deck):
    """shuffles deck"""
    random.shuffle(deck)
    return deck


def create_deck():
    """creates deck of shuffled cards"""
    deck = [Card(suite, value) for suite in suites for value in values]
    return shuffle(deck)
