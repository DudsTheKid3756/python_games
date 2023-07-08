from time import sleep
import random

from menu_displays import *
from constants import *


def shuffle(deck):
    random.shuffle(deck)
    return deck


def get_menu_input(message):
    """validates user input and returns value"""
    is_valid = False
    menu_item = 0
    while not is_valid:
        try:
            menu_item = int(input(f'''
{'~' * 40}
{message}> '''))
            is_valid = True
        except ValueError:
            print("Please enter a number from the menu!")
    return menu_item


def prompt_menu_change(input_):
    print('~' * 40)
    match input_:
        case 0:
            exit_sequence()
        case 1:
            from main.main_menu import play_games
            clear_console()
            show_main_menu()
            play_games()
        case _:
            print(not_an_option.format(input_))


def prompt_exit(exit_prompt, options=None, is_main=False, menu=default_menu):
    """asks if player wants to exit game, exits if (y)es"""
    while True:
        response = input(f'{exit_prompt}> ').lower()
        if response == 'y':
            if is_main:
                exit_sequence()
            else:
                exec(menu.format(options[0], options[1]))
        elif response == 'n':
            return False
        else:
            print(not_valid)


def clear_console():
    print('\n' * 150)


def exit_sequence():
    print('Closing program in:')
    for num in range(1, 6).__reversed__():
        print(num, flush=True)
        sleep(1)
    exit(0)
