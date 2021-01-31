from writer.renderers import BW
from asciimatics.scene import Scene
from asciimatics.effects import Print, Snow
from asciimatics.event import KeyboardEvent

from asciimatics.renderers import FigletText
from asciimatics.exceptions import NextScene


class IronCurtain(Scene):
    def __init__(self, screen, effects=[], duration=600, clear=True, name='Iron curtain'):
        super().__init__(effects, duration, clear, name)
        self._screen = screen
        self.title_text1 = """
                        ________________   __________________
                    .-/|                \ /                |\-.
                    ||||                 |                 ||||
                    ||||                 |      ~~*~~      ||||
                    ||||   --==*==--     |                 ||||
                    ||||                 |    Chapter 2    ||||
                    ||||      The        |                 ||||
                    ||||     Writer      |    --==*==--    ||||
                    ||||                 |                 ||||
                    ||||                 |    The East     ||||
                    ||||                 |                 ||||
                    ||||                 |                 ||||
                    ||||________________ | ________________||||
                    ||/=================\|/=================\||
                    `------------------~___~-----------------''
"""
        self.title_text1 = """
                                _________   _________
                           ____/       12\ /      13 \____
                         /|               |               |\\
                        |||               |               |||
                        |||               |    ~~**~~     |||
                        |||  --==**==--   |               |||
                        |||               |   Chapter 2   |||
                        |||     The       |               |||
                        |||    Writer     |  --==**==--   |||
                        |||               |               |||
                        |||               |   The East    |||
                        |||               |               |||
                        |||               |               |||
                        |||_____________  |  _____________|||
                        L/_____/--------\\\\_//W-------\\_____\\J
"""
        self.title_text2 = """
                                _________   _________
                           ____/       14\ /      15 \____
                         /| Three months  | narrowing her |\\
                        ||| behing the    | to a fine     |||
                        ||| Iron Curtain  | point. She    |||
                        ||| have hardened | feels like a  |||
                        ||| Jennys body   | robot, like a |||
                        ||| along with    | woman from    |||
                        ||| her mind.     | Flatworld,    |||
                        ||| Shes all      | a single line |||
                        ||| angles now,   | that cant     |||
                        ||| the constant  | think for fear|||
                        ||| rationing     | of spilling   |||
                        |||_____________  |  _____________|||
                        L/_____/--------\\\\_//W-------\\_____\\J
"""

        self.title_text3 = """
                                _________   _________
                           ____/       16\ /      17 \____
                         /| every thing   | shes coiming; |\\
                        ||| like sewage   | its  her job. |||
                        ||| from a burst  | A few gentle  |||
                        ||| pipe. The     | words, some   |||
                        ||| Officer shes  | well placed   |||
                        ||| meeting       | flattery, then|||
                        ||| tonight has   | she ll slip   |||
                        ||| called to     | away with next|||
                        ||| make sure she | weeks guard   |||
                        ||| is coming.    | rotation and  |||
                        ||| Of course     | another       |||
                        |||_____________  |  _____________|||
                        L/_____/--------\\\\_//W-------\\_____\\J
"""

        self.title_text4 = """
                                _________   _________
                           ____/       18\ /      19 \____
                         /| hundred souls | tonight.      |\\
                        ||| will brave    |               |||
                        ||| the wires and |               |||
                        ||| the guns      |               |||
                        ||| separating    |               |||
                        ||| East from West|               |||
                        ||| And they ll   |               |||
                        ||| live and die  |               |||
                        ||| on the truth  |               |||
                        ||| - or lies -   |               |||
                        ||| she finds     |               |||
                        |||_____________  |  _____________|||
                        L/_____/--------\\\\_//W-------\\_____\\J
"""

    def intro_text(self, text, start=0):
        return Print(self._screen,
                     BW(self._screen, FigletText(text, width=self._screen.width, font='term')),
                     x=44, y=16,
                     clear=True,
                     start_frame=start,
                     stop_frame=start + 200,
                     bg=0)

    def reset(self, old_scene=None, screen=None):
        effects = [
            Snow(self._screen),
            self.intro_text(self.title_text1, 0),
            self.intro_text(self.title_text2, 100),
            self.intro_text(self.title_text3, 300),
            self.intro_text(self.title_text2, 500),
        ]
        for fx in effects:
            self.add_effect(fx)

    def process_event(self, event):
        super(IronCurtain, self).process_event(event)
        if isinstance(event, KeyboardEvent):
            if event.key_code == 32:  # SPACE key
                raise NextScene
