from writer.gamecontroller import GameController
from writer.intro import Intro
from writer.levels import LEVEL_MAPS
from writer.maze import make_maze, add_word

from asciimatics.screen import Screen
from asciimatics.exceptions import ResizeScreenError

import sys

import logging
logging.basicConfig(filename='writer.log', encoding='utf-8', level=logging.DEBUG)
logger = logging.getLogger(__name__)


def client_entrypoint():
    while True:
        try:
            Screen.wrapper(run, catch_interrupt=False, arguments=[])
            sys.exit(0)
        except ResizeScreenError:
            pass


def run(screen):
    scenes = []
    screen.height = 48
    screen.width = 160
    scenes.append(Intro(screen))

    L1 = 'TOM'
    maze = make_maze(4, 4)
    scenes.append(GameController(screen, L1, add_word(maze, word=L1)))
    # scenes.append(GameController(screen, L1, LEVEL_MAPS[L1]))

    L2 = 'ALIVE'
    scenes.append(GameController(screen, L2, LEVEL_MAPS[L2]))

    screen.refresh()

    screen.play(scenes, stop_on_resize=True)
