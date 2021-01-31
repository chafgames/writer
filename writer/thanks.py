from asciimatics.scene import Scene
from asciimatics.screen import Screen
from asciimatics.effects import Print
from asciimatics.event import KeyboardEvent

from asciimatics.renderers import FigletText, Fire, Figlet
from asciimatics.exceptions import NextScene


class Thanks(Scene):
    def __init__(self, screen, effects=[], duration=-1, clear=True, name='Credits'):
        super().__init__(effects, duration, clear, name)
        self._screen = screen
        self.body = "peterbrittain (github.com/peterbrittain/asciimatics) \n & Chris Black (Head Writer)"

    def reset(self, old_scene=None, screen=None):
        centre = (self._screen.width // 2, self._screen.height // 2)
        text = Figlet(font="banner", width=200).renderText("Special Thanks")
        width = max([len(x) for x in text.split("\n")])

        effects = [
            Print(self._screen,
                  Fire(20, width, text, .4, 40, self._screen.colours),
                  x=centre[0] - 40,
                  y=centre[1] - 30,
                  speed=1,
                  transparent=False),
            Print(self._screen,
                  FigletText("Special Thanks", "banner"),
                  x=centre[0] - 40,
                  y=centre[1] - 12,
                  colour=Screen.COLOUR_WHITE,
                  bg=Screen.COLOUR_WHITE,
                  speed=1),
            Print(self._screen,
                  FigletText("@peterbrittain\n(github.com/peterbrittain/asciimatics)", "thin"),
                  x=1,
                  y=centre[1] - 4,
                  colour=Screen.COLOUR_WHITE,
                  bg=Screen.COLOUR_BLACK,
                  speed=1),
            Print(self._screen,
                  FigletText("Chris Black\n(Head Writer)", "thin"),
                  x=1,
                  y=centre[1]+11,
                  colour=Screen.COLOUR_WHITE,
                  bg=Screen.COLOUR_BLACK,
                  speed=1)
        ]

        for fx in effects:
            self.add_effect(fx)

    def process_event(self, event):
        super(Thanks, self).process_event(event)
        if isinstance(event, KeyboardEvent):
            if event.key_code == 32:  # SPACE key
                raise NextScene
