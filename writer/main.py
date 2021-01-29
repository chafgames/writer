from curses import wrapper
from writer import panels
from writer import asciimatics
def panels_entrypoint():
    wrapper(panels.test)
def ascii_entrypoint():
    asciimatics.test()
