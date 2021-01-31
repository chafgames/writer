from writer.foundtext import FoundText
from writer.gamecontroller import GameController
from writer.intro import Intro
from writer.intro2 import Intro2
from writer.title import Title
from writer.bar import Bar
from writer.levels import LEVEL_MAPS
from writer.maze import make_maze, add_word
from writer.credits import Credits
from writer.thanks import Thanks

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
    scenes.append(Intro2(screen))
    scenes.append(Title(screen))
    scenes.append(Bar(screen))

    # scenes.append(Prompt(screen, name='myTestPrompt', title='my test prompt',
    #                      prompt='What is the flight speed of an unladen sparrow?',
    #                      buttons=['African or European?', 'Erm... Shrubbary?', 'Niiii!'],
    #                      responses=['African?', 'Shrubbary', 'Ni.'],
    #                      closing_scenes=['Intro2', 'L2', 'Credits']))
    L1 = 'TOM'
    maze = make_maze(3, 3)
    scenes.append(GameController(screen, L1, add_word(maze, word=L1), name='L1'))
    scenes.append(FoundText(screen))

    L2 = 'ALIVE'
    scenes.append(GameController(screen, L2, LEVEL_MAPS[L2], name='L2'))

    L3 = 'CAR'
    scenes.append(GameController(screen, L3, LEVEL_MAPS[L3], car=True, name='L3'))

    scenes.append(Credits(screen))
    scenes.append(Thanks(screen))

    screen.refresh()

    screen.play(scenes, stop_on_resize=True)
