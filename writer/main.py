from writer.gamecontroller import GameController
from writer.intro import Intro

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
    scenes.append(Intro(screen))
    scenes.append(GameController(screen))

    screen.refresh()

    screen.play(scenes, stop_on_resize=True)
