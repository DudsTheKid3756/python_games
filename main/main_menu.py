from main.crazy_eights import c8_game
from main.go_fish import gf_game
from main.war import war_game
from util_functions import *
from constants import *


def play_go_fish():
    show_go_fish_menu()
    gf_game.make_game()


def play_crazy_eights():
    show_crazy_8_menu()
    c8_game.make_game()


def play_war():
    show_war_menu()
    war_game.make_game()


def show_about():
    print(f'''
About Python Games:
{'~' * 40}
    Hey! This app was created by me! Tyler
Dudley a.k.a. Duds, The Kid! I wanted to try
this out as a way to practice Python basics.
I started off with the Go Fish! game and got
a bit carried away, but I feel like it turned
out pretty good and it was a lot of fun to
make! More games might be added later and 
potentially implementation of a more user friendly
interface. 
    
    Anyway, not much else to it. Enjoy
and feel free to send feedback!
''')


def handle_input(input_):
    print('~' * 40)
    match input_:
        case 0:
            prompt_exit(ask_to_exit, is_main=True)
        case 1:
            play_go_fish()
        case 2:
            play_crazy_eights()
        case 3:
            play_war()
        case 4:
            show_about()
        case _:
            print(not_an_option.format(input_))


def play_games():
    while True:
        handle_input(get_menu_input(menu_prompt))
