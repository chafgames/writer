from time import sleep
import curses
import curses.panel

from writer import config


def make_panel(height, width, y, x, str):
    """
    panel stuff nicked from:
    https://stackoverflow.com/questions/21172087/i-need-an-example-of-overlapping-curses-windows-using-panels-in-python
    """
    win = curses.newwin(height, width, y, x)
    win.erase()
    win.box()
    win.addstr(2, 2, str)

    panel = curses.panel.new_panel(win)
    return win, panel


def test(stdscr):
    conf = config.new_config()
    try:
        curses.curs_set(0)
    except Exception:
        pass
    stdscr.box()
    win_height, win_width = stdscr.getmaxyx()
    stdscr.addstr(win_height-1, 2, f"INFO {win_height}x{win_width}")
    game_win, game_panel = make_panel(conf.game_height, conf.game_width, 1, 2, "GAME GOES HERE")
    curses.panel.update_panels()
    stdscr.refresh()

    sleep(1000)
