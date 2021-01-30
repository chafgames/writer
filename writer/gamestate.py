from math import pi, floor
import string
import logging

from asciimatics.exceptions import NextScene

LEVEL_MAP = """
################
# YOU BROKE IT #
################
""".strip().split("\n")

HELP = """
Use the following keys:

- Cursor keys to move.
- M to toggle the mini-map
- X to quit
- 1 or 2 to change rendering mode.
"""


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
        self.frames = {'right': {'text': 'THIS IS THE RIGHT TEXT'},
                       'left': {'text': 'THIS IS THE LEFT TEXT'}}

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
        if len(self.found_letters) == len(self.word):
            raise NextScene

    def safe_update_x(self, new_x):
        new_x += self.x
        if 0 <= self.y < len(self.map) and 0 <= new_x < len(self.map[0]):
            tile = self.map[self.map_y][int(floor(new_x))]
            if tile == "#":
                return
            if tile in string.ascii_uppercase:
                self.collide_letter(tile)
                return
        self.x = new_x

    def safe_update_y(self, new_y):
        new_y += self.y
        if 0 <= new_y < len(self.map) and 0 <= self.x < len(self.map[0]):
            tile = self.map[int(floor(new_y))][self.map_x]
            if tile == "#":
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

    def get_frame_by_name(self, name):
        try:
            return self.frames[name]
        except Exception:
            return None


STATE = GameState()
