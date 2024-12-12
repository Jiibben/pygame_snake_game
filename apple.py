from grid_object import GridObject
from const import *
from position import Position


class Apple(GridObject):
    def __init__(self, pos):
        super().__init__(pos, (255,0,0))

    @staticmethod
    def get_random_apple_not_on_snake(snake):
        position = [snake.head.get_position()]
        position.extend([a.get_position() for a in snake.tail])
        randPos = Position.randomPosition(NUMBER_OF_CELL_WIDTH-1, NUMBER_OF_CELL_HEIGHT-1)

        while randPos in position:
            randPos = Position.randomPosition(NUMBER_OF_CELL_WIDTH, NUMBER_OF_CELL_HEIGHT)
            
        return Apple(randPos)
    
