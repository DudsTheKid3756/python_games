import logging
import traceback

from main_menu import play_games
from menu_displays import *

# noinspection PyBroadException
try:
    show_main_menu()
    play_games()
except Exception as e:
    logging.error(traceback.format_exc())
    exit(0)
