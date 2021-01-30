from writer import matics
from writer import writer2
from writer.textframe import TextFrame

from asciimatics.screen import Screen
from asciimatics.exceptions import ResizeScreenError
# from asciimatics.particles import Rain
# from asciimatics.effects import Clock
from asciimatics.scene import Scene

import sys


def matics_entrypoint():
    matics.main()


def client_entrypoint():
    last_scene = None
    while True:
        try:
            Screen.wrapper(run_client, catch_interrupt=False, arguments=[last_scene])
            sys.exit(0)
        except ResizeScreenError as e:
            last_scene = e.scene


def run_client(screen, scene):
    scenes = []
    centre = (screen.width // 2, screen.height // 2)
    cx, cy = centre
    frame_width = int(screen.width / 5)
    right_frame_xpos = frame_width * 4

    effects = [
        writer2.GameController(screen, writer2.GameState()),
        TextFrame(screen, height=screen.height, width=frame_width, data={'text': 'This is the left frame'},
                  x=0, y=0, name='LEFT', title='LEFT_FRAME'),
        TextFrame(screen, height=screen.height, width=frame_width, data={'text': 'This is the right frame'},
                  x=right_frame_xpos, y=0, name='RIGHT', title='RIGHT_FRAME'),
    ]
    scenes.append(Scene(effects, -1))
    # scenes.append(writer2.GameController(screen, writer2.GameState()))

    screen.play(scenes, stop_on_resize=True, start_scene=scene)
