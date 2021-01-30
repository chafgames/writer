from asciimatics.scene import Scene
from asciimatics.screen import Screen
from asciimatics.event import KeyboardEvent

from math import sin, cos, pi, copysign, floor

from writer.minimap import MiniMap
from writer.raycaster import RayCaster
from writer.textframe import TextFrame

class GameController(Scene):
    """
    Scene to control the combined Effects for the demo.

    This class handles the user input, updating the game state and updating required Effects as needed.
    Drawing of the Scene is then handled in the usual way.
    """

    def __init__(self, screen, game_state):
        self.safe_to_default_unhandled_input = False
        self.delete_count = None
        # self.frame_update_count = 0
        self._screen = screen
        self._state = game_state
        self._mini_map = MiniMap(screen, self._state, self._screen.height // 4)
        frame_width = screen.width // 5
        right_frame_xpos = frame_width * 4
        effects = [
            RayCaster(screen, self._state),
            TextFrame(screen, height=screen.height, width=frame_width, data={'text': 'This is the left frame'},
                    x=0, y=0, name='LEFT', title='LEFT_FRAME'),
            TextFrame(screen, height=screen.height, width=frame_width, data={'text': 'This is the right frame'},
                    x=right_frame_xpos, y=0, name='RIGHT', title='RIGHT_FRAME'),
            self._mini_map,
        ]
        super(GameController, self).__init__(effects, -1)

    def process_event(self, event):
        # Allow standard event processing first
        # if super(GameController, self).process_event(event) is None:
        #     return

        # If that didn't handle it, check for a key that this demo understands.
        if isinstance(event, KeyboardEvent):
            c = event.key_code
            if c in (ord("x"), ord("X")):
                raise StopApplication("User exit")
            elif c in (ord("a"), Screen.KEY_LEFT):
                self._state.safe_update_angle(-pi / 22.5)
            elif c in (ord("d"), Screen.KEY_RIGHT):
                self._state.safe_update_angle(pi / 22.5)
            elif c in (ord("w"), Screen.KEY_UP):
                self._state.safe_update_x(cos(self._state.player_angle) / 5)
                self._state.safe_update_y(sin(self._state.player_angle) / 5)
            elif c in (ord("s"), Screen.KEY_DOWN):
                self._state.safe_update_x(-cos(self._state.player_angle) / 5)
                self._state.safe_update_y(-sin(self._state.player_angle) / 5)
            elif c in (ord("1"), ord("2")):
                self._state.mode = c - ord("0")
            elif c in (ord("m"), ord("M")):
                self._state.show_mini_map = not self._state.show_mini_map
                if self._state.show_mini_map:
                    self.add_effect(self._mini_map)
                else:
                    self.remove_effect(self._mini_map)
            elif c in (ord("h"), ord("H")):
                self.add_effect(PopUpDialog(self._screen, HELP, ["OK"]))
            else:
                # Not a recognised key - pass on to other handlers.
                return event
        else:
            # Ignore other types of events.
            return event

    def register_scene(self, scene):
        # Nothing special to do.  Just need this to satisfy the ABC.
        pass

    def update(self, scene):
        # Nothing special to do.  Just need this to satisfy the ABC.
        return