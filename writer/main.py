from writer import writer2

from asciimatics.screen import Screen
from asciimatics.exceptions import ResizeScreenError

import sys


def client_entrypoint():
    game_state = writer2.GameState()
    while True:
        try:
            Screen.wrapper(run, catch_interrupt=False, arguments=[game_state])
            sys.exit(0)
        except ResizeScreenError:
            pass


def run(screen, game_state):
    screen.play([writer2.GameController(screen, game_state)], stop_on_resize=True)