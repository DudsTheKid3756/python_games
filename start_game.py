import logging
import traceback

import main.main_menu as main_menu
from menu_displays import *


# noinspection PyBroadException

def main():
    try:
        show_main_menu()
        main_menu.play_games()
    except Exception:
        logging.error(traceback.format_exc())
        exit(0)


if __name__ == '__main__':
    main()
