import getpass

from main.setup.card_games import hands, deck
from util_functions import *
from constants import *

_deck_, _hands_, player_hand, cpu_hand, player_matches, cpu_matches = [[] for _ in range(6)]


def initialize():
    global _deck_, _hands_, player_hand, cpu_hand
    _deck_ = shuffle(deck.Deck().deck)
    _hands_ = hands.deal_hands(_deck_)
    player_hand = [i for i in _hands_[0]]
    cpu_hand = [i for i in _hands_[1]]


def view_hand():
    """shows current cards in player's hand"""
    for card_ in player_hand:
        print(f'[{card_.name}]\r')


def check_matches(hand, pile_for_matches):
    """searches through cards in hand for matches"""
    matches_ = []
    card_values_to_check = []
    hand_to_check = hand.copy()
    for card_ in hand_to_check:
        value = card_.value[0]
        if value not in card_values_to_check:
            card_values_to_check.append(value)
        else:
            for checked_card in hand_to_check:
                if checked_card.value[0] == value:
                    matches_.append(checked_card.name)
                    try:
                        del hand[hand.index(checked_card)]
                    except ValueError:
                        break
                else:
                    continue
    for match in matches_:
        pile_for_matches.append(match)


def view_matches():
    """shows player's matches"""
    if len(player_matches) != 0:
        values_ = set(item.split()[0] for item in player_matches)
        grouped_matches = [[item for item in player_matches if item.split()[0] == value]
                           for value in values_]
        for match in grouped_matches:
            print(f'[{match}]\r')
    else:
        print('No matches yet!')


def admin_access():
    """
    allows sight of the deck, both player's hands,
    and both player's matches, protected by password
    """
    # TODO: format with separate menu to select from
    password = getpass.getpass(prompt='Input admin password: ', stream=None)
    if password == 'TDuds3756$':
        print('~' * 40)
        print('Deck: ')
        print('~' * 10)
        for card_ in _deck_:
            print(card_.name)
        print('~' * 40)
        print(f'Player matches: {player_matches}')
        print('~' * 40)
        print(f'CPU matches: {cpu_matches}')
        print('~' * 40)
        print('Player hand: ')
        print('~' * 10)
        for player_ in player_hand:
            print(f'{player_.name}\r')
        print('~' * 40)
        print('CPU hand: ')
        print('~' * 10)
        for cpu_ in cpu_hand:
            print(f'{cpu_.name}\r')
    else:
        print('Password incorrect!')
        exit(0)


def pick_winner():
    """finds which player has more matches"""
    if len(player_matches) > len(cpu_matches):
        print('~' * 40)
        print('You won!!!')
    elif len(cpu_matches) > len(player_matches):
        print('~' * 40)
        print('You lost! :(')
    else:
        print('~' * 40)
        print('There was a tie. No winner. Play again!')
    prompt_exit(play_again, exit_options)


def handle_empty_hand(hand, opponent_hand):
    """
    line 120-124: calls go fish function if player has no cards after turn
    line 126-127: calls pick winner function if deck and both player hands are empty
    """
    if len(hand) == 0:
        go_fish(hand)

    if len(opponent_hand) == 0:
        go_fish(opponent_hand)

    if len(_deck_) == 0 and len(hand) == 0 and len(opponent_hand) == 0:
        pick_winner()


def go_fish(hand):
    """adds single card to hand if possible"""
    if len(_deck_) > 0:
        hand.append(_deck_[0])
        _deck_.pop(0)
    else:
        pass


def handle_card_call(
        hand,
        opponent_hand,
        card_call,
        success_message,
        fail_message
):
    """
    determines if called card matches cards in hand,
    moves card to correct hand if match
    """
    matched = False
    card_to_use = None
    for card in hand:
        card_num_value = card.value[0]
        if card_call == card_num_value:
            matched = True
            card_to_use = card
            break
        else:
            continue
    if matched:
        opponent_hand.append(card_to_use)
        del hand[hand.index(card_to_use)]
        print(success_message)
    else:
        go_fish(opponent_hand)
        print(fail_message)


def call_card():
    """
    player's turn, 'asks' cpu if it has a card,
    handles match success or fail
    """
    handle_empty_hand(player_hand, cpu_hand)
    value_exists = False
    card_call = None
    while not value_exists:
        try:
            card_call = int(input('Enter card value to match> '))
            checked = False
            for player_card in player_hand:
                player_card_num_value = player_card.value[0]
                if card_call == player_card_num_value:
                    checked = True
                    break
                else:
                    continue
            if checked:
                value_exists = True
            else:
                if card_call == 0:
                    prompt_exit(ask_to_exit, exit_options)
                else:
                    print('~' * 40)
                    print('Please enter a value that matches one in your hand!')
                    has_answer = False
                    while not has_answer:
                        print('~' * 40)
                        response = input('View hand? (Y or n)> ').lower()
                        print('~' * 40)
                        match response:
                            case 'y':
                                view_hand()
                                print('~' * 40)
                                has_answer = True
                            case 'n':
                                has_answer = True
                                pass
                            case _:
                                print(not_valid)
        except ValueError:
            print('~' * 40)
            print(not_numeric)
    print('~' * 40)
    handle_card_call(
        cpu_hand,
        player_hand,
        card_call,
        'You got a match!',
        'Go Fish!'
    )
    check_matches(cpu_hand, cpu_matches)
    check_matches(player_hand, player_matches)


def cpu_turn():
    """
    computer's turn, randomly selects card to 'call',
    handles match success or fail
    """
    handle_empty_hand(cpu_hand, player_hand)
    random_card = random.choice(cpu_hand)
    card_call = random_card.value[0]
    print(f'Do you have any {random_card.value[1]}s?')
    sleep(.5)
    print('.')
    sleep(.5)
    print('.')
    sleep(.5)
    print('.')
    sleep(.5)
    print('.')
    sleep(.5)
    handle_card_call(
        player_hand,
        cpu_hand,
        card_call,
        'I got a match!',
        'No match... It\'s your turn!'
    )
    check_matches(cpu_hand, cpu_matches)
    check_matches(player_hand, player_matches)


def view_instructions():
    print(f'''
Python Go Fish Instructions:
{'~' * 40}
Welcome to Python Go Fish!

    This is a basic game of Go Fish played against a computer!
The player (that's you!) and the cpu are both dealt 5 cards from 
the deck to start. The player goes first and can select
a number from the start menu to either view their hand (1), 
ask the cpu for a card (2), view their matches (3), or exit the game
if they so desire (0).

    At the start of the game, any matches found
in either hand right off the bat will be added to either player's
match pile (so you may not have 5 cards when you view your hand 
initially). If at any point any runs out of cards, a single card
will be drawn from the deck at the end of the turn. Each player
will take turns asking each other for cards that match ones in
their respected hands until no cards are left in the deck and
no cards are left in hand. To get a match, the card called
must match only in number value, for example: Four (4) of Clubs
matches with Four (4) of Diamonds: both are valued at 4!

    That's pretty much it! Enjoy the game and feel free to give
feedback at curlyq3756@gmail.com! Thank You!

    This version of Go Fish was created by Duds, The Kid
                Version 1.0.0 | Copyright 2021
    ''')


def handle_input(input_):
    """handles menu input"""
    print('~' * 40)
    match input_:
        case 0:
            prompt_exit(ask_to_exit, exit_options)
        case 1:
            view_hand()
        case 2:
            call_card()
            cpu_turn()
        case 3:
            check_matches(player_hand, player_matches)
            view_matches()
        case 4:
            view_instructions()
        case 3756:
            admin_access()
        case _:
            print(not_an_option.format(input_))


def make_game():
    """checks hands for match first and executes start of game"""
    initialize()
    check_matches(player_hand, player_matches)
    check_matches(cpu_hand, cpu_matches)
    while True:
        handle_empty_hand(player_hand, cpu_hand)
        handle_input(get_menu_input(menu_prompt))
