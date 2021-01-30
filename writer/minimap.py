from asciimatics.screen import Screen
from asciimatics.effects import Effect
from math import pi

from writer.gamestate import STATE


class MiniMap(Effect):
    """
    Class to draw a small map based on the one stored in the GameState.
    """

    # Translation from angle to map directions.
    _DIRECTIONS = [
        (0, pi / 4, ">"),
        (pi / 4, 3 * pi / 4, "v"),
        (3 * pi / 4, 5 * pi / 4, "<"),
        (5 * pi / 4, 7 * pi / 4, "^")
    ]

    def __init__(self, screen, size=5):
        super(MiniMap, self).__init__(screen)
        self._size = size
        self._x = self._screen.width - 2 * (self._size + 1)
        self._y = self._screen.height - (self._size + 1)

    def _update(self, _):
        # Draw the miniature map.
        for mx in range(self._size * 2):
            for my in range(self._size):
                px = STATE.map_x + mx - self._size // 2
                py = STATE.map_y + my - self._size // 2
                if (0 <= py < len(STATE.map) and
                        0 <= px < len(STATE.map[0]) and STATE.map[py][px] != " "):
                    bg_colour = Screen.COLOUR_RED
                    fg_colour = Screen.COLOUR_WHITE
                    pixel = STATE.map[py][px] if STATE.map[py][px] != 'X' else " "
                else:
                    bg_colour = Screen.COLOUR_BLACK
                    fg_colour = Screen.COLOUR_BLACK
                    pixel = " "
                self._screen.print_at(pixel, self._x + mx, self._y + my, fg_colour, bg=bg_colour)

        # Draw the player
        text = ">"
        for a, b, direction in self._DIRECTIONS:
            if a < STATE.player_angle <= b:
                text = direction
                break
        self._screen.print_at(
            text, self._x + self._size // 2, self._y + self._size // 2, Screen.COLOUR_GREEN)

    @property
    def frame_update_count(self):
        # No animation required.
        return 0

    @property
    def stop_frame(self):
        # No specific end point for this Effect.  Carry on running forever.
        return 0

    def reset(self):
        # Nothing special to do.  Just need this to satisfy the ABC.
        pass

    def regiser_scene(self, scene):
        # Nothing special to do.  Just need this to satisfy the ABC.
        pass
