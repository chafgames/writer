from asciimatics.scene import Scene
from asciimatics.effects import Print
from asciimatics.event import KeyboardEvent

from asciimatics.particles import DropScreen
from asciimatics.renderers import FigletText, Rainbow, Plasma
from asciimatics.exceptions import NextScene


class FoundText(Scene):
    def __init__(self, screen, effects=[], duration=250, clear=True, name='Found!'):
        super().__init__(effects, duration, clear, name)
        self._screen = screen

    def reset(self, old_scene=None, screen=None):
        effects = [
            # Stars(screen, (screen.width + screen.height) // 2, start_frame=0),
            Print(self._screen,
                  Plasma(self._screen.height, self._screen.width, self._screen.colours),
                  x=0, y=0,
                  speed=10,
                  start_frame=0,
                  stop_frame=110,
                  transparent=False),
            Print(self._screen,
                  # Rainbow(self._screen, FigletText( "You found something, the memories are coming back.", font='thin', width=self._screen.width)),  # noqa: E501
                  FigletText("You found something, the memories are coming back.", font='thin', width=self._screen.width),
                  x=2, y=16,
                  clear=False,
                  transparent=True,
                  start_frame=0,
                  stop_frame=110),
            DropScreen(self._screen, 100, start_frame=100),
            Print(self._screen,
                  Rainbow(self._screen, FigletText("Tom is alive...", font='standard', width=self._screen.width)),
                  x=20, y=16,
                  clear=True,
                  start_frame=150,
                  stop_frame=self.duration),

        ]
        for fx in effects:
            self.add_effect(fx)

    def process_event(self, event):
        super(FoundText, self).process_event(event)
        if isinstance(event, KeyboardEvent):
            if event.key_code == 32:  # SPACE key
                raise NextScene
