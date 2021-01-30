from writer.renderers import Dull
from asciimatics.scene import Scene
from asciimatics.effects import Print
from asciimatics.event import KeyboardEvent

from asciimatics.particles import Rain
from asciimatics.renderers import FigletText
from asciimatics.exceptions import NextScene


class Intro2(Scene):
    def __init__(self, screen, effects=[], duration=400, clear=True, name='Intro'):
        super().__init__(effects, duration, clear, name)
        self._screen = screen
        self.story_text1 = "Jenny Sinton has fallen into a deep coma and doesn’t know how to find her way out..."
        self.story_text2 = "Jenny’s writing has kept her sane since the Cold War ended. Left by the UK government to cope with the trauma of being an ex-spy."  # noqa: E501
        self.story_text3 = "She has alienated her family in service to her country, and now that her country has abandoned her, she’s trying to find her way back to normal life."  # noqa: E501
        self.story_text4 = "When she’s hears the news she’s been waiting for, she falls into a coma, and words are the only thing that can bring her back to reality."  # noqa: E501

    def intro_text(self, text, start):
        return Print(self._screen,
                     Dull(self._screen, FigletText(text, width=self._screen.width, font='thin')),
                     x=2, y=16,
                     clear=True,
                     start_frame=start,
                     stop_frame=start + 100,
                     bg=0)

    def reset(self, old_scene=None, screen=None):
        effects = [
            Rain(self._screen, self.duration),
            self.intro_text(self.story_text1, 0),
            self.intro_text(self.story_text2, 100),
            self.intro_text(self.story_text3, 200),
            self.intro_text(self.story_text4, 300),
        ]
        for fx in effects:
            self.add_effect(fx)

    def process_event(self, event):
        super(Intro2, self).process_event(event)
        if isinstance(event, KeyboardEvent):
            if event.key_code == 32:  # SPACE key
                raise NextScene
