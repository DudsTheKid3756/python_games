import random

from main.setup.card_games import hands, deck
from util_functions import *
from constants import *

_hands_, player_hand, cpu_hand = [[] for _ in range(3)]
current_round = 1


def initialize():
    global _hands_, player_hand, cpu_hand
    _hands_ = hands.deal_hands(deck.create_deck(), 26)
    player_hand = [i for i in _hands_[0]]
    cpu_hand = [i for i in _hands_[1]]


def display_round_info(message):
    player_card = player_hand[0].name
    cpu_card = cpu_hand[0].name
    print(f'''
Round: {current_round}

Player card: {player_card}
CPU card: {cpu_card}

{message}
{'~' * 40}
    ''')


def handle_battle_win(winner_hand, loser_hand, cards_to_move):
    del loser_hand[0]
    del winner_hand[0]
    if len(winner_hand) > 5:
        rand_index = random.choice(range(int(len(winner_hand) / 2), int(len(winner_hand) - 1)))
        for card_ in cards_to_move:
            winner_hand.insert(rand_index, card_)
    else:
        for card_ in cards_to_move:
            winner_hand.append(card_)


def prep_war(hand):
    return [hand.pop(0) for _ in range(5)] \
        if len(hand) > 5 else [hand.pop(0) for _ in range(len(hand) - 1)] \
        if len(hand) > 1 else []


def declare_war():
    do_war = True
    war_round = 1
    war_debt = []
    war_winner = None
    while do_war:
        player_wager = prep_war(player_hand)
        cpu_wager = prep_war(cpu_hand)
        player_card = player_hand[0]
        cpu_card = cpu_hand[0]
        print(f'{"~" * 14}Declare War!{"~" * 14}')
        print(f'''
War Round: {war_round}

Player card: {player_card.name}
CPU card: {cpu_card.name}
        ''')
        war_debt = [*player_wager, *cpu_wager]
        if len(player_hand) > 1 and len(cpu_hand) > 1:
            if player_card.value[0] != cpu_card.value[0]:
                if player_card.value[0] > cpu_card.value[0]:
                    war_winner = 0
                else:
                    war_winner = 1
                war_debt.append(player_card)
                war_debt.append(cpu_card)
                do_war = False
            else:
                war_round += 1
        else:
            if len(player_hand) == 1:
                if player_card.value[0] > cpu_card.value[0]:
                    war_winner = 0
                    do_war = False
                    war_debt.append(player_card)
                    war_debt.append(cpu_card)
                else:
                    print('You lost :(')
                    exec(default_menu.format(exit_options[0], exit_options[1]))
            else:
                if cpu_card.value[0] > player_card.value[0]:
                    war_winner = 1
                    do_war = False
                    war_debt.append(player_card)
                    war_debt.append(cpu_card)
                else:
                    print('You won!!')
                    exec(default_menu.format(exit_options[0], exit_options[1]))
    print(f'''
{"You won the wager!" if war_winner == 0 else "You lost the wager :("}
{'~' * 40}
''')
    return deck.shuffle(war_debt), war_winner


def battle():
    while True:
        global current_round
        if len(player_hand) > 0 and len(cpu_hand) > 0:
            player_card = player_hand[0]
            cpu_card = cpu_hand[0]
            player_card_value = player_card.value[0]
            cpu_card_value = cpu_card.value[0]
            cards_in_battle = [player_card, cpu_card]
            if player_card_value > cpu_card_value:
                display_round_info('You won the battle!')
                handle_battle_win(player_hand, cpu_hand, cards_in_battle)
            elif player_card_value < cpu_card_value:
                display_round_info('You lost the battle!')
                handle_battle_win(cpu_hand, player_hand, cards_in_battle)
            else:
                display_round_info('WAR!!')
                war_results = declare_war()
                handle_battle_win(player_hand, cpu_hand, war_results[0]) \
                    if war_results[1] == 0 \
                    else handle_battle_win(cpu_hand, player_hand, war_results[0])
            current_round += 1
        else:
            if len(player_hand) == 0:
                print('You lost :(')
            else:
                print('You won!!')
            exec(default_menu.format(exit_options[0], exit_options[1]))


def show_instructions():
    print(f'''
War Instructions:
{'~' * 40}
Welcome to Python War!

    This is the game of war! This version of the classic war
card game was made in Python. Due to the way the game is played
originally, this version is to be 'watched' more than 'played',
for now.
    
    In this game, each hand is dealt by splitting the deck in
half. With each hand unseen, a player flips the top card over 
to be compared to their opponents top card. Which ever player 
has the highest valued card, takes the pair and puts them at 
the bottom of their hand. If the two cards have the same value
the player 'declare war'. During war, each play lays out 3 face
down cards and then one card face up to be compared. Which ever
player has the highest of the face up cards gets all 10 cards.
If the cards are the same then another war commences. The first
player to have all 52 cards wins!

    That's pretty much it! Enjoy the game and feel free to give
feedback at curlyq3756@gmail.com! Thank You!

    This version of War was created by Duds, The Kid
                Version 1.0.0 | Copyright 2021 
    ''')


def handle_input(input_):
    print('~' * 40)
    match input_:
        case 0:
            prompt_exit(ask_to_exit, exit_options)
        case 1:
            battle()
        case 2:
            show_instructions()
        case _:
            print(not_an_option.format(input_))


def make_game():
    initialize()
    while True:
        handle_input(get_menu_input(menu_prompt))
