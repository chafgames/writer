from writer.renderers import BW
from asciimatics.scene import Scene
from asciimatics.effects import Print
from asciimatics.event import KeyboardEvent

from asciimatics.particles import Rain
from asciimatics.renderers import FigletText
from asciimatics.exceptions import NextScene

from pkg_resources import resource_string
from writer import constants


class Wall(Scene):
    def __init__(self, screen, effects=[], duration=600, clear=True, name='Wall'):
        super().__init__(effects, duration, clear, name)
        self._screen = screen
        self.car_text = resource_string('writer.art', 'wall').decode('utf-8')

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
            self.intro_text(constants.wall_scene_story_text, 40, x=12, y=35),
        ]
        for fx in effects:
            self.add_effect(fx)

    def process_event(self, event):
        super(Wall, self).process_event(event)
        if isinstance(event, KeyboardEvent):
            if event.key_code == 32:  # SPACE key
                raise NextScene
