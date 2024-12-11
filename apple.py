from grid_object import GridObject
from snake import Snake
from const import NUMBER_OF_CELL_HEIGHT, NUMBER_OF_CELL_WIDTH
from position import Position
class Apple(GridObject):
    def __init__(self, pos):
        super().__init__(pos, (255,0,0))

    @staticmethod
    def get_random_apple_not_on_snake(snake):
        position = [snake.head.get_postion()].extend(snake.tail)
        randPos = Position.randomPosition(NUMBER_OF_CELL_HEIGHT, NUMBER_OF_CELL_WIDTH)

        while randPos in position:
            randPos = Position.randomPosition(NUMBER_OF_CELL_HEIGHT, NUMBER_OF_CELL_WIDTH)
            
        return Apple(randPos)