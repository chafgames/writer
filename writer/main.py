from writer.foundtext import FoundText
from writer.gamecontroller import GameController
from writer.intro2 import Intro2
from writer.title import Title
from writer.bar import Bar
from writer.car import Car
from writer.captain import Captain
from writer.ironcurtain import IronCurtain
from writer.wall import Wall
from writer.river import River
from writer.levels import LEVEL_MAPS
from writer.maze import make_maze, add_word
from writer.credits import Credits
from writer.thanks import Thanks
from writer.prompt import Prompt
from writer.image import Image
from writer.plaintext import PlainText
from writer.singleprompt import SinglePrompt
from writer import constants

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

    scenes.append(Image(screen, name='Intro', imagetext=constants.intro_text, imagefile='globe.gif'))
    # scenes.append(Intro(screen))
    scenes.append(Intro2(screen))

    scenes.append(Title(screen))
    L1 = 'TOM'
    maze = make_maze(3, 3)
    scenes.append(GameController(screen, L1, add_word(maze, word=L1), name='L1'))

    scenes.append(FoundText(screen))

    scenes.append(Bar(screen))

    scenes.append(Prompt(screen, name='bar_order', title='',
                         prompt=constants.bar_order_prompt,
                         buttons=[constants.bar_order_button_1_text,
                                  constants.bar_order_button_2_text,
                                  constants.bar_order_button_3_text],
                         responses=[constants.bar_order_button_1_resp,
                                    constants.bar_order_button_2_resp,
                                    constants.bar_order_button_3_resp],
                         closing_scenes=[constants.bar_order_button_1_jump_to,
                                         constants.bar_order_button_2_jump_to,
                                         constants.bar_order_button_3_jump_to]))
    scenes.append(Prompt(screen, name='stranger_convo', title='',
                         prompt=constants.stranger_convo_prompt,
                         buttons=[constants.stranger_convo_button_1_text,
                                  constants.stranger_convo_button_2_text,
                                  constants.stranger_convo_button_3_text],
                         responses=[constants.stranger_convo_button_1_resp,
                                    constants.stranger_convo_button_2_resp,
                                    constants.stranger_convo_button_3_resp],
                         closing_scenes=[constants.stranger_convo_button_1_jump_to,
                                         constants.stranger_convo_button_2_jump_to,
                                         constants.stranger_convo_button_3_jump_to]))

    scenes.append(Car(screen, name='car'))
    L3 = 'CAR'
    scenes.append(GameController(screen, L3, add_word(LEVEL_MAPS[L3], L3), car=True, name='L3'))
    scenes.append(Prompt(screen, name='car_boot', title='',
                         prompt=constants.car_boot_prompt,
                         buttons=[constants.car_boot_button_1_text,
                                  constants.car_boot_button_2_text,
                                  constants.car_boot_button_3_text],
                         responses=[constants.car_boot_button_1_resp,
                                    constants.car_boot_button_2_resp,
                                    constants.car_boot_button_3_resp],
                         closing_scenes=[constants.car_boot_button_1_jump_to,
                                         constants.car_boot_button_2_jump_to,
                                         constants.car_boot_button_3_jump_to]))
    scenes.append(Image(screen, name='flag', imagetext=constants.flag_text, imagefile='flag.gif', font='straight'))
    scenes.append(PlainText(screen, name='flagtext', text=constants.flag_text, font='straight'))

    scenes.append(IronCurtain(screen))
    scenes.append(SinglePrompt(screen, name='mirror', prompt=constants.mirror_prompt))

    # scenes.append(PlainText(screen, name='flagtext', text=constants.flag_text, font='straight'))
    L4 = 'CHAUFFEUR'
    maze = make_maze(6, 6)
    scenes.append(GameController(screen, L4, add_word(maze, word=L4), name='L4'))
    scenes.append(Prompt(screen, name='pig', title='',
                         prompt=constants.pig_prompt,
                         buttons=[constants.pig_button_1_text,
                                  constants.pig_button_2_text,
                                  constants.pig_button_3_text],
                         responses=[constants.pig_button_1_resp,
                                    constants.pig_button_2_resp,
                                    constants.pig_button_3_resp],
                         closing_scenes=[constants.pig_button_1_jump_to,
                                         constants.pig_button_2_jump_to,
                                         constants.pig_button_3_jump_to]))

    scenes.append(Captain(screen))
    scenes.append(Wall(screen))
    scenes.append(River(screen))
    scenes.append(Prompt(screen, name='final', title='',
                         prompt=constants.river_scene_story_text,
                         buttons=[constants.final_button_1_text,
                                  constants.final_button_2_text,
                                  constants.final_button_3_text],
                         responses=[constants.final_button_1_resp,
                                    constants.final_button_2_resp,
                                    constants.final_button_3_resp],
                         closing_scenes=[constants.final_button_1_jump_to,
                                         constants.final_button_2_jump_to,
                                         constants.final_button_3_jump_to]))

    scenes.append(Credits(screen, name=Credits))
    scenes.append(Thanks(screen))

    screen.refresh()

    screen.play(scenes, stop_on_resize=True)
