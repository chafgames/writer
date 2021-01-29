from curses import wrapper
from writer import panels
def entrypoint():
    wrapper(panels.test)
