from asciimatics.screen import ManagedScreen
from asciimatics.scene import Scene
from asciimatics.effects import Cycle, Stars
from asciimatics.renderers import FigletText, Box
from time import sleep

def test():
    hello_world()

@ManagedScreen
def hello_world(screen=None):
    # screen.print_at('Hello world! 1', 0, 0)
    # screen.refresh()
    # sleep(2)
    # # screen.print_at('Hello world! 2', 0, 0)
    # # screen.refresh()
    # # sleep(2)
    # # screen.print_at('Hello world! 3', 0, 0)
    # # screen.refresh()
    # # sleep(2)
    # # screen.print_at('Hello world! 4', 0, 0)
    # # screen.refresh()
    # # sleep(2)
    # screen.paint(FigletText("ASCIIMATICS", font='big'), 0, 0)
    screen.paint(Box(3, 3), 2, 2)
    screen.refresh()
    sleep(100)