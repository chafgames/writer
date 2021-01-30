#!/usr/bin/env python3

# -*- coding: utf-8 -*-
import sys
from writer.textframe import TextFrame
from math import sin, cos, pi, copysign, floor
from asciimatics.effects import Effect
from asciimatics.event import KeyboardEvent
from asciimatics.exceptions import ResizeScreenError, StopApplication
from asciimatics.screen import Screen
from asciimatics.scene import Scene
from asciimatics.widgets import PopUpDialog
import string
from random import choice

import logging
logging.basicConfig(filename='writer.log', encoding='utf-8', level=logging.INFO)



HELP = """
Use the following keys:

- Cursor keys to move.
- M to toggle the mini-map
- X to quit
- 1 or 2 to change rendering mode.
"""
LEVEL_MAP = """
XXXXXXXXXXXXXXXX
X              X
X  X        X  X
X  X  X     X  X
XAXXX X  XXXX  X
X XXX X XX    XX
XBX XXX    XXXXX
X X XXX XXXXX  X
XCX     X      X
X XXXXX   XXXXXX
XD E           X
XXXXXXXXXXXXXX X
""".strip().split("\n")


class GameState(object):
    """
    Persistent state for this application.
    """

    def __init__(self):
        self.player_angle = pi / 2
        self.x, self.y = 1.5, 1.5
        self.map = LEVEL_MAP
        self.mode = 1
        self.show_mini_map = True
        self.found_letters = []

    @property
    def map_x(self):
        return int(floor(self.x))

    @property
    def map_y(self):
        return int(floor(self.y))

    def collide_letter(self, letter):
        logging.info(f'Found letter {letter}')
        logging.info(f'Map1 {self.map}')
        self.found_letters.append(letter)
        self.map = [x.replace(letter, ' ') for x in self.map]


    def safe_update_x(self, new_x):
        new_x += self.x
        if 0 <= self.y < len(self.map) and 0 <= new_x < len(self.map[0]):
            tile = self.map[self.map_y][int(floor(new_x))]
            if tile == "X":
                return
            if tile in string.ascii_uppercase:
                self.collide_letter(tile)
                return
        self.x = new_x

    def safe_update_y(self, new_y):
        new_y += self.y
        if 0 <= new_y < len(self.map) and 0 <= self.x < len(self.map[0]):
            tile = self.map[int(floor(new_y))][self.map_x]
            if tile  == "X":
                return
            if tile in string.ascii_uppercase:
                self.collide_letter(tile)
                return
        self.y = new_y

    def safe_update_angle(self, new_angle):
        self.player_angle += new_angle
        if self.player_angle < 0:
            self.player_angle += 2 * pi
        if self.player_angle > 2 * pi:
            self.player_angle -= 2 * pi


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

    def __init__(self, screen, game_state, size=5):
        super(MiniMap, self).__init__(screen)
        self._state = game_state
        self._size = size
        self._x = self._screen.width - 2 * (self._size + 1)
        self._y = self._screen.height - (self._size + 1)

    def _update(self, _):
        # Draw the miniature map.
        for mx in range(self._size  * 2):
            for my in range(self._size):
                px = self._state.map_x + mx - self._size // 2
                py = self._state.map_y + my - self._size // 2
                if (0 <= py < len(self._state.map) and
                        0 <= px < len(self._state.map[0]) and self._state.map[py][px] != " "):
                    bg_colour = Screen.COLOUR_RED
                    fg_colour = Screen.COLOUR_WHITE
                    pixel = self._state.map[py][px] if self._state.map[py][px] != 'X' else " "
                else:
                    bg_colour = Screen.COLOUR_BLACK
                    fg_colour = Screen.COLOUR_BLACK
                    pixel = " "
                self._screen.print_at(pixel, self._x + mx, self._y + my, fg_colour, bg=bg_colour)

        # Draw the player
        text = ">"
        for a, b, direction in self._DIRECTIONS:
            if a < self._state.player_angle <= b:
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

    def __init__(self, screen, game_state):
        super(RayCaster, self).__init__(screen)
        self._state = game_state
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
            camera_x = cos(self._state.player_angle + pi / 2) * self.FOV
            camera_y = sin(self._state.player_angle + pi / 2) * self.FOV
            camera_segment = 2 * sx / self._screen.width - 1
            ray_x = cos(self._state.player_angle) + camera_x * camera_segment
            ray_y = sin(self._state.player_angle) + camera_y * camera_segment

            # Representation of the ray within our map
            map_x = self._state.map_x
            map_y = self._state.map_y
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
            side_x = (self._state.x - map_x) if ray_x < 0 else (map_x + 1.0 - self._state.x)
            side_x *= ratio_to_x
            side_y = (self._state.y - map_y) if ray_y < 0 else (map_y + 1.0 - self._state.y)
            side_y *= ratio_to_y

            # Give up if we'll never intersect the map
            while (((step_x < 0 and map_x >= 0) or (step_x > 0 and map_x < len(self._state.map[0]))) and
                   ((step_y < 0 and map_y >= 0) or (step_y > 0 and map_y < len(self._state.map)))):
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
                if 0 <= map_x < len(self._state.map[0]) and 0 <= map_y < len(self._state.map):
                    if self._state.map[map_y][map_x] == "X":
                        hit = True
                        break

                # Check whether the ray has now hit a letter.
                if 0 <= map_x < len(self._state.map[0]) and 0 <= map_y < len(self._state.map):
                    if self._state.map[map_y][map_x] == "A":
                        hit_letter = True
                        break

            # Draw wall if needed.
            if hit:
                # Figure out textures and colours to use based on the distance to the wall.
                if hit_side:
                    dist = (map_y - self._state.y + (1 - step_y) / 2) / ray_y
                else:
                    dist = (map_x - self._state.x + (1 - step_x) / 2) / ray_x
                wall = min(self._screen.height, int(self._screen.height / dist))
                colour, attr, bg = self._colours[min(len(self._colours) - 1, int(3 * dist))]
                text = self._TEXTURES[min(len(self._TEXTURES) - 1, int(2 * dist))]

                # Now draw the wall segment
                for sy in range(wall):
                    self._screen.print_at(
                        text * 2, sx, (self._screen.height - wall) // 2 + sy,
                        colour, attr, bg=0 if self._state.mode == 1 else bg)

                # Draw a line when we change surfaces to help make it easier to see the 3d effect
                if hit_side != last_side:
                    last_side = hit_side
                    for sy in range(wall):
                        self._screen.print_at("|", sx, (self._screen.height - wall) // 2 + sy, 0, bg=0)


            # Draw letter if needed.
            if hit_letter:
                # Figure out textures and colours to use based on the distance to the wall.
                if hit_letter_side:
                    dist = (map_y - self._state.y + (1 - step_y) / 2) / ray_y
                else:
                    dist = (map_x - self._state.x + (1 - step_x) / 2) / ray_x
                letter = min(self._screen.height, int(self._screen.height / dist))
                redList = [9, 52, 88, 124, 126, 131, 160, 167, 196, 202, 203, 204, 211]
                colour, attr, bg = (choice(redList), 0, 0)
                text = self._A_TEXTURES[min(len(self._TEXTURES) - 1, int(2 * dist))]

                # Now draw the wall segment
                for sy in range(letter):
                    self._screen.print_at(
                        text * 2, sx, (self._screen.height - letter) // 2 + sy,
                        colour, attr, bg=0 if self._state.mode == 1 else bg)

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
