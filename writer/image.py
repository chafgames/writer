from writer.renderers import Dull
from asciimatics.scene import Scene
from asciimatics.effects import Print
from asciimatics.event import KeyboardEvent

from asciimatics.renderers import FigletText, ColourImageFile
from asciimatics.exceptions import NextScene
from asciimatics.screen import Screen

import pkg_resources


class Image(Scene):
    def __init__(self, screen, effects=[], duration=-1, clear=True, name='Image',
                 imagefile='globe.gif', imagetext='FOOBAR'):
        super().__init__(effects, duration, clear, name)
        self._screen = screen
        self._imagefile = imagefile
        self._imagetext = imagetext

    def reset(self, old_scene=None, screen=None):
        image_filename = pkg_resources.resource_filename(pkg_resources.Requirement.parse('writer'), f"writer/art/{self._imagefile}")
        effects = [
            Print(self._screen, ColourImageFile(self._screen, image_filename, self._screen.height, bg=Screen.COLOUR_BLACK,
                  fill_background=False, uni=False, dither=False),
                  0,
                  stop_frame=100),

            Print(self._screen,
                  Dull(self._screen, FigletText(self._imagetext, font='thin', width=self._screen.width)),
                  x=2, y=13,
                  clear=True,
                  start_frame=0,
                  stop_frame=200)
                  ]
        for fx in effects:
            self.add_effect(fx)

    def process_event(self, event):
        super(Image, self).process_event(event)
        if isinstance(event, KeyboardEvent):
            if event.key_code == 32:  # SPACE key
                raise NextScene
