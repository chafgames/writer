# noqa: W605
from writer.renderers import Dull, Jenny
from asciimatics.scene import Scene
from asciimatics.effects import Print
from asciimatics.event import KeyboardEvent

from asciimatics.renderers import FigletText
from asciimatics.exceptions import NextScene


class Bar(Scene):
    def __init__(self, screen, effects=[], duration=300, clear=True, name='Titles'):
        super().__init__(effects, duration, clear, name)
        self._screen = screen
        self.title_text1 = """
                              There’s a cedarwood top to the bar, a cold lacquer at odds with the warmth of the landlord.
                                 Jenny’s tapping nervously on a coaster when a man slides into the seat beside her.
                                   He’s looking at the barman, waiting for something. He’s waiting for a drink…
                                           if only Jenny could remember what she was supposed to order…


                                                             ,-----.
                                                            (  Yes? )
                                                             `---y--
                                                                /       _     ,------------.
                                                              ,~,     `{,c. -( Miss Sinton? )
                                                            Y (((   __,-==`-. `-------------
                                                            /_)))) _[//\   |->______
                                                              )\(/[_____|__\________
                                                             /   )  |   | _)) [_]
                                                            /___(   |   | | \  |
                                                           /)  |)   |   | |\ \ |
                                                         _,p  _,p   |  ,|_| \_\L_

"""
        self.title_text2 = "Press SPACE to continue"

    def intro_text(self, text, start=0):
        return Print(self._screen,
                     Jenny(self._screen, FigletText(text, width=self._screen.width, font='term')),
                     x=0, y=16,
                     clear=True,
                     start_frame=start,
                     stop_frame=start + self.duration // 2,
                     bg=0)

    def reset(self, old_scene=None, screen=None):
        effects = [
            self.intro_text(self.title_text1, 0),
            Print(self._screen,
                  Dull(self._screen, FigletText(self.title_text2, width=self._screen.width, font='term')),
                  x=self._screen.width // 2 - 10, y=36,
                  clear=True,
                  start_frame=0,
                  stop_frame=self.duration,
                  bg=0),
        ]
        for fx in effects:
            self.add_effect(fx)

    def process_event(self, event):
        super(Bar, self).process_event(event)
        if isinstance(event, KeyboardEvent):
            if event.key_code == 32:  # SPACE key
                raise NextScene
