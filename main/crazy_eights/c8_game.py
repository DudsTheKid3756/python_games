import time

from main.setup.card_games import hands, deck
from util_functions import *

deck = deck.Deck()
suites = deck.suites
stock, _hands_, player_hand, cpu_hand, starter_pile = [[] for _ in range(5)]
current_suite = ""


def initialize():
    global stock, _hands_, player_hand, cpu_hand
    stock = shuffle(deck.deck)
    _hands_ = hands.deal_hands(stock)
    player_hand = [i for i in _hands_[0]]
    cpu_hand = [i for i in _hands_[1]]


def start_game():
    global current_suite
    starter_pile.append(stock[0])
    stock.pop(0)
    while starter_pile[0].value[0] == 8:
        starter_pile.insert(0, stock[0])
        stock.pop(0)
    current_suite = starter_pile[0].suite


def show_starter():
    print(f'Starter suite: [{current_suite}]') \
        if starter_pile[0].value[0] == 8 \
        else print(f'Starter: [{starter_pile[0].name}]')


def handle_low_stock():
    for count in range(1, len(starter_pile) - 1):
        stock.append(starter_pile[1])
        starter_pile.pop(1)
    shuffle(stock)


def draw_card(hand):
    if len(stock) > 0:
        if len(stock) < 2:
            handle_low_stock()
        else:
            pass
        hand.append(stock[0])
        stock.pop(0)
        return True
    else:
        print('No more cards to draw!')
        return False


def handle_play_card(hand, card_to_play):
    starter_pile.insert(0, hand[card_to_play])
    del hand[card_to_play]


def check_for_win(hand, message):
    if len(hand) == 0:
        print('~' * 40)
        print(message)
        prompt_exit(play_again, exit_options)
    else:
        pass


def player_turn():
    show_starter()
    print('~' * 40)
    card_to_play = None
    can_play_card = False
    global current_suite
    while not can_play_card:
        is_card_in_hand = False
        while not is_card_in_hand:
            try:
                card_to_play = int(input(f'''
Pick a card number to play (0 - {len(player_hand) - 1})
Draw a card and show hand (-1)
End turn without playing a card (-2)

Enter a response> '''))
                match card_to_play:
                    case -1:
                        print('~' * 40)
                        draw_card(player_hand)
                        view_hand()
                    case -2:
                        return False
                    case _:
                        if card_to_play > len(player_hand) - 1:
                            print('~' * 40)
                            print('Please pick a card that\'s in your hand!')
                        else:
                            has_answer = False
                            while not has_answer:
                                print('~' * 40)
                                response = input(f'Play {player_hand[card_to_play].name}? (Y or n)> ').lower()
                                print('~' * 40)
                                match response:
                                    case 'y':
                                        has_answer = True
                                        is_card_in_hand = True
                                    case 'n':
                                        has_answer = True
                                        pass
                                    case _:
                                        print(not_valid)
            except ValueError:
                print('~' * 40)
                print(not_numeric)
        card_to_play_value = player_hand[card_to_play].value[0]
        card_to_play_suite = player_hand[card_to_play].suite
        starter_card_value = starter_pile[0].value[0]
        starter_card_suite = starter_pile[0].suite
        if card_to_play_value == 8:
            print('~' * 20)
            suite_decided = False
            while not suite_decided:
                for suite in suites:
                    print(f'{list(suites).index(suite)}: {suite}\r')
                try:
                    response = int(input('Pick a suite to change to!> '))
                    if response > 3:
                        print('~' * 40)
                        print('Please pick a valid suite number!')
                    else:
                        suite_decided = True
                        current_suite = list(suites)[response]
                        handle_play_card(player_hand, card_to_play)
                        can_play_card = True
                        break
                except ValueError:
                    print('~' * 40)
                    print(not_numeric)
        elif starter_card_value == 8:
            if card_to_play_suite == current_suite:
                handle_play_card(player_hand, card_to_play)
                can_play_card = True
            else:
                print(f'Suite does not match! Pick a card with the suite: {current_suite}')
        elif card_to_play_value == starter_card_value or card_to_play_suite == starter_card_suite:
            handle_play_card(player_hand, card_to_play)
            can_play_card = True
        else:
            print('~' * 40)
            print('That card does not match the starter! Pick another one!')
    check_for_win(player_hand, 'You won!!!')


def cpu_turn():
    print('My turn!', flush=True)
    sleep(.5)
    for _ in range(4):
        print('.', flush=True)
        sleep(.5)
    stop_play = False
    card_was_played = False
    global current_suite
    while not stop_play:
        possible_card_plays = [
            card_ for card_ in cpu_hand
            if (starter_pile[0].value[0] == 8
                and card_.suite == current_suite)
            or (card_.suite == starter_pile[0].suite
                or card_.value[0] == starter_pile[0].value[0])
        ]
        if len(possible_card_plays) > 0:
            play_card = random.choice(range(0, 2))
            turn_complete = False
            random_card = random.choice(possible_card_plays)
            card_to_play = cpu_hand.index(random_card)
            while not turn_complete:
                if play_card == 0:
                    if random_card.value[0] == 8:
                        current_suite = random.choice(list(suites))
                        print(f'I played an 8! I change the suite to {current_suite}')
                    else:
                        print(f'I played a {cpu_hand[card_to_play].name}!')
                    handle_play_card(cpu_hand, card_to_play)
                    card_was_played = True
                    turn_complete = True
                    stop_play = True
                else:
                    draw_card(cpu_hand)
                    turn_complete = True
                    stop_play = random.choice((True, False))
        else:
            draw_card(cpu_hand)
            stop_play = random.choice((True, False))
    check_for_win(cpu_hand, 'You lost!! :(')
    print('I\'m not playing a card this turn.') if card_was_played is False else None
    print('Your turn!')


def view_hand():
    for card_ in player_hand:
        print(f'[{player_hand.index(card_)}: {card_.name}]\r')


def show_instructions():
    print(f'''
Python Crazy 8's Instructions:
{'~' * 40}
Welcome to Python Crazy 8's!

    This is a basic game of Crazy 8's played against a computer!
The player (that's you) and the cpu are both dealt 5 cards from
the deck to start. A single card from the deck is placed face up
as the starter. The player goes first and can select a number from
the starter menu to either view their hand (1), play a card (2),
draw a card (3), or exit the game (0)
if they so desire.

    The player starts by playing a card that matches the starter
in either suite or number value, for example: if Four (4) of Clubs
is the starter, any Four (4) or Clubs card can be played. To see 
specific card values, select (4) from the start menu. After that 
each player takes turns playing cards that match the previous card
played. As a general rule, Eights are wild cards and can be played
at any time. If an Eight is played the player must specify which
suite they want the wild card to represent. The game ends when a
player or the computer has run out of cards and is declared the
winner!

    That's pretty much it! Enjoy the game and feel free to give
feedback at curlyq3756@gmail.com! Thank You!

    This version of Crazy 8's was created by Duds, The Kid
                Version 1.0.0 | Copyright 2021
    ''')


def handle_input(input_):
    print('~' * 40)
    match input_:
        case 0:
            prompt_exit(ask_to_exit, exit_options)
        case 1:
            view_hand()
        case 2:
            show_starter()
        case 3:
            player_turn()
            cpu_turn()
        case 4:
            if draw_card(player_hand) is False:
                print('Skipping your turn!')
                cpu_turn()
            else:
                view_hand()
                pass
        case 5:
            cpu_turn()
        case 6:
            show_instructions()
        case _:
            print(not_an_option.format(input_))


def make_game():
    initialize()
    start_game()
    while True:
        handle_input(get_menu_input(menu_prompt))
