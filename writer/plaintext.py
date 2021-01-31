from writer.renderers import BW
from asciimatics.scene import Scene
from asciimatics.effects import Print
from asciimatics.event import KeyboardEvent

from asciimatics.renderers import FigletText, ColourImageFile
from asciimatics.exceptions import NextScene
from asciimatics.screen import Screen

import pkg_resources


class PlainText(Scene):
    def __init__(self, screen, effects=[], duration=-1, clear=True, name='Image',
                 font='thin', text='text'):
        super().__init__(effects, duration, clear, name)
        self._screen = screen
        self._font = font
        self._text = text

    def reset(self, old_scene=None, screen=None):
        effects = [
            Print(self._screen,
                  BW(self._screen, FigletText(self._text, font=self._font, width=self._screen.width-14)),
                  x=4, y=8,
                  clear=True,
                  start_frame=0,
                  stop_frame=200)
                  ]
        for fx in effects:
            self.add_effect(fx)

    def process_event(self, event):
        super(PlainText, self).process_event(event)
        if isinstance(event, KeyboardEvent):
            if event.key_code == 32:  # SPACE key
                raise NextScene
