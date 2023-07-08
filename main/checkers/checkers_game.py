from util_functions import *
from main.setup.board import red_empty_spot, black_empty_spot

setup = []
for i in range(8):
    if bool(i % 2):
        setup.append(red_empty_spot)
    else:
        setup.append(black_empty_spot)
for i in range(8):
    if bool(i % 2):
        setup.append(black_empty_spot)
    else:
        setup.append(red_empty_spot)


def view_board():
    print('''
{}{}{}{}{}{}{}{}
{}{}{}{}{}{}{}{}
{}{}{}{}{}{}{}{}
{}{}{}{}{}{}{}{}
{}{}{}{}{}{}{}{}
{}{}{}{}{}{}{}{}
{}{}{}{}{}{}{}{}
{}{}{}{}{}{}{}{}
    '''.format(
            *setup * 4
        )
    )


def handle_input(input_):
    print('~' * 40)
    match input_:
        case 0:
            prompt_exit(ask_to_exit, exit_options)
        case 1:
            view_board()
        case 2:
            print('show moves')
        case 3:
            print('make move')
        case 4:
            print('show instructions')
        case _:
            print(not_an_option.format(input_))


def make_game():
    while True:
        handle_input(get_menu_input(menu_prompt))
