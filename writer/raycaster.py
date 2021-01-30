from asciimatics.screen import Screen
from asciimatics.effects import Effect
from math import sin, cos, pi, copysign
from random import choice

from writer.gamestate import STATE


class RayCaster(Effect):
    """
    Raycaster effect - will draw a 3D rendition of the map stored in the GameState.

    This class follows the logic from https://lodev.org/cgtutor/raycasting.html.
    """

    # Textures to emulate h distance.
    _TEXTURES = "@&#$AHhwai;:. "
    _A_TEXTURES = "@Aa:.         "
    _B_TEXTURES = "ßBb:.         "
    _C_TEXTURES = "©Cc:.         "
    _D_TEXTURES = "ÐDd:.         "
    _E_TEXTURES = "€Ee;.         "
    _F_TEXTURES = "FFf:.         "
    _G_TEXTURES = "9Gg:.         "
    _H_TEXTURES = "#Hh:.         "
    _I_TEXTURES = "I!i:.         "
    _J_TEXTURES = "J¿j:.         "
    _K_TEXTURES = "KKk:.         "
    _L_TEXTURES = "LLl:.         "
    _M_TEXTURES = "MMm:.         "
    _N_TEXTURES = "NNn:.         "
    _O_TEXTURES = "0Oo:.         "
    _P_TEXTURES = "¶Pp:.         "
    _Q_TEXTURES = "ÓQq:.         "
    _R_TEXTURES = "®Rr:.         "
    _S_TEXTURES = "$Ss:.         "
    _T_TEXTURES = "Tt±:.         "
    _U_TEXTURES = "Uüu:.         "
    _V_TEXTURES = "VVv:.         "
    _W_TEXTURES = "WWw:.         "
    _X_TEXTURES = "Xx×:.         "
    _Y_TEXTURES = "¥Yy:.         "
    _Z_TEXTURES = "§Zz:.         "

    # Controls for rendering - this is the relative size of the camera plane to the viewing vector.
    FOV = 0.66

    def __init__(self, screen):
        super(RayCaster, self).__init__(screen)
        self._block_size = screen.height // 3
        if screen.colours >= 256:
            self._colours = [x for x in zip(range(255, 232, -1), [0] * 24, range(255, 232, -1))]
        else:
            self._colours = [(Screen.COLOUR_WHITE, Screen.A_BOLD, 0) for _ in range(6)]
            self._colours.extend([(Screen.COLOUR_WHITE, Screen.A_NORMAL, 0) for _ in range(9)])
            self._colours.extend([(Screen.COLOUR_BLACK, Screen.A_BOLD, 0) for _ in range(9)])
            self._colours.append((Screen.COLOUR_BLACK, Screen.A_NORMAL, 0))

        # self._letter_colours = [(Screen.COLOUR_RED, Screen.A_BOLD, 0) for _ in range(6)]
        # self._letter_colours.extend([(Screen.COLOUR_BLUE, Screen.A_NORMAL, 0) for _ in range(9)])
        # self._letter_colours.extend([(Screen.COLOUR_GREEN, Screen.A_BOLD, 0) for _ in range(9)])
        # self._letter_colours.append((Screen.COLOUR_YELLOW, Screen.A_NORMAL, 0))

    def _update(self, _):
        # First draw the background - which is theoretically the floor and ceiling.
        self._screen.clear_buffer(Screen.COLOUR_BLACK, Screen.A_NORMAL, Screen.COLOUR_BLACK)

        # Now do the ray casting across the visible canvas.
        # Compensate for aspect ratio by treating 2 cells as a single pixel.
        last_side = None
        for sx in range(0, self._screen.width, 2):
            # Calculate the ray for this vertical slice.
            camera_x = cos(STATE.player_angle + pi / 2) * self.FOV
            camera_y = sin(STATE.player_angle + pi / 2) * self.FOV
            camera_segment = 2 * sx / self._screen.width - 1
            ray_x = cos(STATE.player_angle) + camera_x * camera_segment
            ray_y = sin(STATE.player_angle) + camera_y * camera_segment

            # Representation of the ray within our map
            map_x = STATE.map_x
            map_y = STATE.map_y
            hit = False
            hit_side = False
            hit_letter = False
            hit_letter_side = False

            # Logical length along the ray from one x or y-side to next x or y-side
            try:
                ratio_to_x = abs(1 / ray_x)
            except ZeroDivisionError:
                ratio_to_x = 999999
            try:
                ratio_to_y = abs(1 / ray_y)
            except ZeroDivisionError:
                ratio_to_y = 999999

            # Calculate block step direction and initial partial step to the next side (on same
            # logical scale as the previous ratios).
            step_x = int(copysign(1, ray_x))
            step_y = int(copysign(1, ray_y))
            side_x = (STATE.x - map_x) if ray_x < 0 else (map_x + 1.0 - STATE.x)
            side_x *= ratio_to_x
            side_y = (STATE.y - map_y) if ray_y < 0 else (map_y + 1.0 - STATE.y)
            side_y *= ratio_to_y

            # Give up if we'll never intersect the map
            while (((step_x < 0 and map_x >= 0) or (step_x > 0 and map_x < len(STATE.map[0]))) and
                   ((step_y < 0 and map_y >= 0) or (step_y > 0 and map_y < len(STATE.map)))):
                # Move along the ray to the next nearest side (measured in distance along the ray).
                if side_x < side_y:
                    side_x += ratio_to_x
                    map_x += step_x
                    hit_side = False
                    hit_letter_side = False
                else:
                    side_y += ratio_to_y
                    map_y += step_y
                    hit_side = True
                    hit_letter_side = True

                # Check whether the ray has now hit a wall.
                if 0 <= map_x < len(STATE.map[0]) and 0 <= map_y < len(STATE.map):
                    if STATE.map[map_y][map_x] == "X":
                        hit = True
                        break

                # Check whether the ray has now hit a letter.
                if 0 <= map_x < len(STATE.map[0]) and 0 <= map_y < len(STATE.map):
                    if STATE.map[map_y][map_x] == "A":
                        hit_letter = True
                        break

            # Draw wall if needed.
            if hit:
                # Figure out textures and colours to use based on the distance to the wall.
                if hit_side:
                    dist = (map_y - STATE.y + (1 - step_y) / 2) / ray_y
                else:
                    dist = (map_x - STATE.x + (1 - step_x) / 2) / ray_x
                wall = min(self._screen.height, int(self._screen.height / dist))
                colour, attr, bg = self._colours[min(len(self._colours) - 1, int(3 * dist))]
                text = self._TEXTURES[min(len(self._TEXTURES) - 1, int(2 * dist))]

                # Now draw the wall segment
                for sy in range(wall):
                    self._screen.print_at(
                        text * 2, sx, (self._screen.height - wall) // 2 + sy,
                        colour, attr, bg=0 if STATE.mode == 1 else bg)

                # Draw a line when we change surfaces to help make it easier to see the 3d effect
                if hit_side != last_side:
                    last_side = hit_side
                    for sy in range(wall):
                        self._screen.print_at("|", sx, (self._screen.height - wall) // 2 + sy, 0, bg=0)

            # Draw letter if needed.
            if hit_letter:
                # Figure out textures and colours to use based on the distance to the wall.
                if hit_letter_side:
                    dist = (map_y - STATE.y + (1 - step_y) / 2) / ray_y
                else:
                    dist = (map_x - STATE.x + (1 - step_x) / 2) / ray_x
                letter = min(self._screen.height, int(self._screen.height / dist))
                redList = [9, 52, 88, 124, 126, 131, 160, 167, 196, 202, 203, 204, 211]
                colour, attr, bg = (choice(redList), 0, 0)
                text = self._A_TEXTURES[min(len(self._TEXTURES) - 1, int(2 * dist))]

                # Now draw the wall segment
                for sy in range(letter):
                    self._screen.print_at(
                        text * 2, sx, (self._screen.height - letter) // 2 + sy,
                        colour, attr, bg=0 if STATE.mode == 1 else bg)

                # Draw a line when we change surfaces to help make it easier to see the 3d effect
                if hit_letter_side != last_side:
                    last_side = hit_side
                    for sy in range(letter):
                        self._screen.print_at("|", sx, (self._screen.height - letter) // 2 + sy, 0, bg=0)

    @property
    def frame_update_count(self):
        # No animation required.
        return 0

    def regiser_scene(self, scene):
        # Nothing special to do.  Just need this to satisfy the ABC.
        pass

    @property
    def stop_frame(self):
        # No specific end point for this Effect.  Carry on running forever.
        return 0

    def reset(self):
        # Nothing special to do.  Just need this to satisfy the ABC.
        pass
