from writer.renderers import Dull
from asciimatics.scene import Scene
from asciimatics.effects import Print
from asciimatics.particles import Rain
from asciimatics.renderers import FigletText, Rainbow


class Intro(Scene):
    def __init__(self, screen, effects=[], duration=300, clear=True, name='Intro'):
        super().__init__(effects, duration, clear, name)
        self._screen = screen
        self.story_text = """
        Jenny Sinton has fallen into a coma and doesn’t know how to get out.
Jenny’s writing has kept her sane since the Cold War ended. Left by the UK government to cope with the trauma of being an ex-spy. She has alienated her family in service to her country, and now that her country has abandoned her, she’s trying to find her way back to normal life.
When she’s hears the news she’s been waiting for, she falls into a coma, and words are the only thing that can bring her back to reality."""



    def reset(self, old_scene=None, screen=None):
        centre = (self._screen.width // 2, self._screen.height // 2)
        effects = [
            # Stars(screen, (screen.width + screen.height) // 2, start_frame=0),
            Rain(screen, self.duration),
            Print(screen,
                Dull(screen, FigletText("""“But the biggest thing that has happened in the world in my life, in our lives, is this: 
                By the grace of God, America won the Cold War.”""",
                        font='thin', width=self._screen.width)),
                x=2, y=16, 
                clear=True,
                start_frame=0,
                stop_frame=200),
            Print(screen,
                Rainbow(screen, FigletText(self.story_text)),
                x=2, y=1,
                clear=True,
                start_frame=200,
                stop_frame=2000),
        ]
        for fx in effects:
            self.add_effect(fx)
