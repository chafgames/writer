from asciimatics.screen import Screen
from asciimatics.scene import Scene
from asciimatics.effects import Cycle, Stars, Print
from asciimatics.renderers import FigletText, Box, SpeechBubble
from time import sleep

def run(screen):
    scenes = []
    centre = (screen.width // 2, screen.height // 2)

    effects = [
        Print(screen,
              Box(screen.width, screen.height, uni=screen.unicode_aware),
              0, 0, start_frame=0),
        Stars(screen, (screen.width + screen.height) // 2, start_frame=0),
		Print(screen,
			FigletText("Hello world!", font="big"),
			x=centre[0], y=centre[1],
			clear=True,
			start_frame=0,
			stop_frame=100),
    ]
    scenes.append(Scene(effects, -1))
    screen.refresh()
    # sleep(100)

    screen.play(scenes, stop_on_resize=True)

def main():
	Screen.wrapper(run)
