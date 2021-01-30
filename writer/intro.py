from asciimatics.screen import Screen
from writer.renderers import Dull
from asciimatics.scene import Scene
from asciimatics.effects import Print, Scroll
from asciimatics.event import KeyboardEvent

from asciimatics.particles import Rain
from asciimatics.renderers import FigletText, Rainbow
from asciimatics.exceptions import NextScene

class Intro(Scene):
    def __init__(self, screen, effects=[], duration=250, clear=True, name='Intro'):
        super().__init__(effects, duration, clear, name)
        self._screen = screen

    def reset(self, old_scene=None, screen=None):
        centre = (self._screen.width // 2, self._screen.height // 2)
        effects = [
            # Stars(screen, (screen.width + screen.height) // 2, start_frame=0),
            Rain(screen, self.duration),
            Print(screen,
                Dull(screen, FigletText("""but the biggest thing that has happened in the world in my life, in our lives, is this: 
 by the grace of God, America won the Cold War.
        President George H.W. Bush""",
                        font='thin', width=self._screen.width)),
                x=2, y=13, 
                clear=True,
                start_frame=0,
                stop_frame=200),
        ]
        for fx in effects:
            self.add_effect(fx)


    def process_event(self, event):
        super(Intro, self).process_event(event)
        if isinstance(event, KeyboardEvent):
            if event.key_code == 32:  # SPACE key
                raise NextScene
