from asciimatics.scene import Scene
from asciimatics.screen import Screen
from asciimatics.event import KeyboardEvent
from asciimatics.exceptions import StopApplication, NextScene
from asciimatics.widgets import PopUpDialog

from math import sin, cos, pi
from writer.minimap import MiniMap
from writer.raycaster import RayCaster
from writer.textframe import TextFrame
from writer.statusframe import StatusFrame
from writer.gamestate import HELP, STATE

import logging
logger = logging.getLogger(__name__)


class GameController(Scene):
    """
    Scene to control the combined Effects for the demo.

    This class handles the user input, updating the game state and updating required Effects as needed.
    Drawing of the Scene is then handled in the usual way.
    """

    def __init__(self, screen, word, map, car=False, name='GameController'):
        self.safe_to_default_unhandled_input = False
        self.delete_count = None
        # self.frame_update_count = 0
        self._screen = screen
        self._mini_map = MiniMap(screen, self._screen.height // 4)
        frame_width = screen.width // 5
        right_frame_xpos = frame_width * 4
        self.word = word
        self.map = map
        self.car = car
        self.playerx, self.playery = 1.5, 1.5
        effects = [
            RayCaster(screen),
            TextFrame(screen, height=screen.height, width=frame_width, data={},
                      x=0, y=0, name=f"frame_{name}", title='story'),
            StatusFrame(screen, height=screen.height, width=frame_width, data={},
                        x=right_frame_xpos, y=0, name='status', title='status'),
            self._mini_map,
        ]
        super(GameController, self).__init__(effects, -1, name=name)

    def reset(self):
        STATE.word = self.word
        STATE.map = self.map
        STATE.car = self.car
        STATE.x = self.playerx
        STATE.y = self.playery

    def process_event(self, event):

        # If that didn't handle it, check for a key that this demo understands.
        if isinstance(event, KeyboardEvent):
            c = event.key_code
            if c in (ord("x"), ord("X")):
                raise StopApplication("User exit")
            elif c in (ord("a"), Screen.KEY_LEFT):
                STATE.safe_update_angle(-pi / 12.25)
            elif c in (ord("d"), Screen.KEY_RIGHT):
                STATE.safe_update_angle(pi / 12.25)
            elif c in (ord("w"), Screen.KEY_UP):
                STATE.safe_update_x(cos(STATE.player_angle) / 5)
                STATE.safe_update_y(sin(STATE.player_angle) / 5)
            elif c in (ord("s"), Screen.KEY_DOWN):
                STATE.safe_update_x(-cos(STATE.player_angle) / 5)
                STATE.safe_update_y(-sin(STATE.player_angle) / 5)
            elif c in (ord("1"), ord("2")):
                STATE.mode = c - ord("0")
            elif c in (ord("m"), ord("M")):
                STATE.show_mini_map = not STATE.show_mini_map
                if STATE.show_mini_map:
                    self.add_effect(self._mini_map)
                else:
                    self.remove_effect(self._mini_map)
            elif c in (ord("h"), ord("H")):
                self.add_effect(PopUpDialog(self._screen, HELP, ["OK"]))
            elif c == ord("0"):
                raise NextScene
            else:
                # Not a recognised key - pass on to other handlers.
                return event
        else:
            # Ignore other types of events.
            # Allow standard event processing first
            if super(GameController, self).process_event(event) is None:
                return
            return event

    def register_scene(self, scene):
        # Nothing special to do.  Just need this to satisfy the ABC.
        pass

    def update(self, scene):
        # Nothing special to do.  Just need this to satisfy the ABC.
        return
