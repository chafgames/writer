from writer.gamestate import GameState
from writer.gamecontroller import GameController

from asciimatics.screen import Screen
from asciimatics.exceptions import ResizeScreenError

import sys


def client_entrypoint():
    game_state = GameState()
    while True:
        try:
            Screen.wrapper(run, catch_interrupt=False, arguments=[game_state])
            sys.exit(0)
        except ResizeScreenError:
            pass


def run(screen, game_state):
    screen.play([GameController(screen, game_state)], stop_on_resize=True)
