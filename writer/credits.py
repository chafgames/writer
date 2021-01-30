from asciimatics.scene import Scene
from asciimatics.screen import Screen
from asciimatics.effects import Print
from asciimatics.event import KeyboardEvent

from asciimatics.renderers import FigletText, Fire, Figlet
from asciimatics.exceptions import NextScene


class Credits(Scene):
    def __init__(self, screen, effects=[], duration=-1, clear=True, name='Credits'):
        super().__init__(effects, duration, clear, name)
        self._screen = screen

    def reset(self, old_scene=None, screen=None):
        centre = (self._screen.width // 2, self._screen.height // 2)
        text = Figlet(font="banner", width=200).renderText("ChafNut Games")
        width = max([len(x) for x in text.split("\n")])

        effects = [
            Print(self._screen,
                  Fire(20, width, text, .4, 40, self._screen.colours),
                  x=centre[0] - 40,
                  y=centre[1] - 30,
                  speed=1,
                  transparent=False),
            Print(self._screen,
                  FigletText("ChafNut Games", "banner"),
                  x=centre[0] - 40,
                  y=centre[1] - 12,
                  colour=Screen.COLOUR_WHITE,
                  bg=Screen.COLOUR_WHITE,
                  speed=1),
            Print(self._screen,
                  FigletText("Michael Robinson \n Matt Mulhern", "thin"),
                  x=centre[0] - 20,
                  y=centre[1],
                  colour=Screen.COLOUR_WHITE,
                  bg=Screen.COLOUR_BLACK,
                  speed=1)
        ]

        for fx in effects:
            self.add_effect(fx)

    def process_event(self, event):
        super(Credits, self).process_event(event)
        if isinstance(event, KeyboardEvent):
            if event.key_code == 32:  # SPACE key
                raise NextScene
