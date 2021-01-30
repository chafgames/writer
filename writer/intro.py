from writer.renderers import Dull
from asciimatics.scene import Scene
from asciimatics.effects import Print
from asciimatics.particles import Rain
from asciimatics.renderers import FigletText, Rainbow


class Intro(Scene):
    def __init__(self, screen, effects=[], duration=300, clear=True, name='Intro'):
        super().__init__(effects, duration, clear, name)
        self._screen = screen


    def reset(self, old_scene=None, screen=None):
        centre = (self._screen.width // 2, self._screen.height // 2)
        effects = [
            # Stars(screen, (screen.width + screen.height) // 2, start_frame=0),
            Rain(screen, self.duration),
            Print(screen,
                Dull(screen, FigletText("""“But the biggest thing that has happened in the world in my life, in our lives, is this: 
                By the grace of God, America won the Cold War.”""",
                        font='smslant', width=150)),
                x=centre[0]-100, y=centre[1]-20,
                clear=True,
                start_frame=0,
                stop_frame=200),
            Print(screen,
                Rainbow(screen, FigletText("Press <SPACE> to start")),
                x=centre[0]-100, y=centre[1]-20,
                clear=True,
                start_frame=200,
                stop_frame=2000),
        ]
        for fx in effects:
            self.add_effect(fx)
