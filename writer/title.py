from writer.renderers import Dull
from asciimatics.scene import Scene
from asciimatics.effects import Print
from asciimatics.event import KeyboardEvent

from asciimatics.particles import Rain
from asciimatics.renderers import FigletText
from asciimatics.exceptions import NextScene


class Title(Scene):
    def __init__(self, screen, effects=[], duration=300, clear=True, name='Titles'):
        super().__init__(effects, duration, clear, name)
        self._screen = screen
        self.title_text1 = """
    __________________   __________________
.-/|                  \ /                  |\-.
||||                   |                   ||||
||||                   |       ~~*~~       ||||
||||    --==*==--      |                   ||||
||||                   |     Chapter 1     ||||
||||       The         |                   ||||
||||      Writer       |     --==*==--     ||||
||||                   |                   ||||
||||                   |     Discovery     ||||
||||                   |                   ||||
||||                   |                   ||||
||||__________________ | __________________||||
||/===================\|/===================\||
`--------------------~___~-------------------''
"""
        self.title_text2 = "Press SPACE to start"

        self.title_text3 = """
        _________   _________
   ____/      452\ /     453 \____
 /| You know that |  ------------ |\\
||| something is  | ------------- |||
||| missing.      | ------------- |||
||| A thing that  | ------------- |||
||| once meant    | ------------- |||
||| everything to | ------------- |||
||| you. Maybe if | ----------    |||
||| it's found,   |  ------------ |||
||| you'll no     | ------------- |||
||| longer be     | ------ -----  |||
||| lost.         | ------------- |||
|||_____________  |  _____________|||
L/_____/--------\\\\_//W-------\\_____\\J
"""

    def intro_text(self, text, start=0):
        return Print(self._screen,
                     Dull(self._screen, FigletText(text, width=self._screen.width, font='term')),
                     x=44, y=16,
                     clear=True,
                     start_frame=start,
                     stop_frame=start + self.duration // 2,
                     bg=0)

    def reset(self, old_scene=None, screen=None):
        effects = [
            Rain(self._screen, self.duration),
            self.intro_text(self.title_text1, 0),
            Print(self._screen,
                  Dull(self._screen, FigletText(self.title_text2, width=self._screen.width, font='term')),
                  x=self._screen.width // 2 - 10, y=36,
                  clear=True,
                  start_frame=0,
                  stop_frame=self.duration,
                  bg=0),
            self.intro_text(self.title_text3, self.duration // 2),
        ]
        for fx in effects:
            self.add_effect(fx)

    def process_event(self, event):
        super(Title, self).process_event(event)
        if isinstance(event, KeyboardEvent):
            if event.key_code == 32:  # SPACE key
                raise NextScene
