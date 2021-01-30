from asciimatics.scene import Scene
from asciimatics.effects import Stars, Print
from asciimatics.renderers import FigletText, Rainbow


class Intro(Scene):
    def __init__(self, screen):
        super().__init__(effects=[], duration=300, clear=True, name='Intro')
        self._screen = screen


    def reset(self, old_scene=None, screen=None):
        centre = (self._screen.width // 2, self._screen.height // 2)
        effects = [
            Stars(screen, (screen.width + screen.height) // 2, start_frame=0),
            Print(screen,
                FigletText("""I’m afraid sometimes you’ll play lonely games too, games you can’t win because
                you’ll play against you."""),
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
