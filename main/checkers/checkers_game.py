from main.setup.board import *
from util_functions import *

mk_cpu = make_cpu_side()
mk_plr = make_player_side()

cpu_side = [
    (x.color % (bg(0), attr(0)) if x.__class__ == Piece else x)
    for i in mk_cpu for x in i
]
player_side = [
    (x.color % (bg(0), attr(0)) if x.__class__ == Piece else x)
    for i in mk_plr for x in i
]

# cpu_side = [
#     x.color if x.__class__ == Piece else x for i in mk_cpu for x in i
# ]
#
# player_side = [
#     x.color if x.__class__ == Piece else x for i in mk_plr for x in i
# ]


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
            *cpu_side,
            *player_side
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
