from writer.renderers import Dull, BW
from writer.constants import car_scene_story_text
from asciimatics.scene import Scene
from asciimatics.effects import Print
from asciimatics.event import KeyboardEvent

from asciimatics.particles import Rain
from asciimatics.renderers import FigletText
from asciimatics.exceptions import NextScene

from pkg_resources import resource_string
from writer import constants

class Car(Scene):
    def __init__(self, screen, effects=[], duration=400, clear=True, name='Car'):
        super().__init__(effects, duration, clear, name)
        self._screen = screen
        self.car_text = resource_string('writer.art', 'car_road').decode('utf-8')


    def intro_text(self, text, start, x, y):
        return Print(self._screen,
                     BW(self._screen, FigletText(text, width=self._screen.width, font='term')),
                     x=x, y=y,
                     clear=True,
                     start_frame=start,
                     stop_frame=self.duration,
                     bg=0)

    def reset(self, old_scene=None, screen=None):
        effects = [
            Rain(self._screen, self.duration),
            self.intro_text(self.car_text, 0, x=22, y=10),
            self.intro_text(constants.car_scene_story_text, 100, x=2, y=45),
        ]
        for fx in effects:
            self.add_effect(fx)

    def process_event(self, event):
        super(Car, self).process_event(event)
        if isinstance(event, KeyboardEvent):
            if event.key_code == 32:  # SPACE key
                raise NextScene
