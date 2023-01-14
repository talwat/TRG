from enum import Enum
from type import Map

"""
Describes the mode the game is in
"""
class Mode(Enum):
    MAP = 1
    INVENTORY = 2
    SHOP = 3
    BATTLE = 4

"""
Game information

This is a class so that we can actually edit information like the mode
"""
class Game:
    map: Map = []
    NAME = "TRG"
    mode = Mode.MAP