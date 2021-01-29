from asciimatics.screen import Screen
from asciimatics.scene import Scene
from asciimatics.effects import Cycle, Stars, Print
from asciimatics.renderers import FigletText, Box, Rainbow
from time import sleep

def run(screen):
    scenes = []
    centre = (screen.width // 2, screen.height // 2)

    # Intro
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

    scenes.append(Scene(effects, -1))

    # Scene 1, start the game
    side_panel = [
        Print(screen,
              Box(screen.width // 5, screen.height, uni=screen.unicode_aware),
              0, 0, start_frame=0),
		Print(screen,
			FigletText("Side", font="big"),
			x=0, y=1,
			clear=True,
			start_frame=0,
			stop_frame=100),
    ]

    effects = [
        Print(screen,
              Box((screen.width // 5) * 4, screen.height, uni=screen.unicode_aware),
              0, screen.width // 5, start_frame=0),
    ]

    final = side_panel + effects
    scenes.append(Scene(final, -1))
    screen.refresh()
    # sleep(100)

    screen.play(scenes, stop_on_resize=True)

def main():
	Screen.wrapper(run)
