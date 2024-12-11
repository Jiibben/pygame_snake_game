from enum import Enum
from position import Position


class Direction(Enum):
    UP = Position(0,-1)
    DOWN = Position(0,1)
    LEFT = Position(-1,0)
    RIGHT = Position(1,0)




