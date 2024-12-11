from updatable import Updatable
from position import Position as Pos
from direction import Direction
from drawable import Drawable
from snakeSegment import SnakeSegment
from const import NUMBER_OF_CELL_WIDTH, NUMBER_OF_CELL_HEIGHT


class Snake(Drawable, Updatable):
    def __init__(self, headPos : Pos):
        self.head = SnakeSegment(headPos)
        self.tail=[SnakeSegment(headPos + Direction.LEFT.value), SnakeSegment(headPos + Direction.LEFT.value*2), SnakeSegment(headPos+ Direction.LEFT.value*3)]
        self.movement = Direction.RIGHT 

    def add_movement(self, direction : Direction):
        self.movement = direction

    def add_segment(self, pos : Pos):
        self.tail.append(SnakeSegment(pos))
    
    def update(self):
        oldTailPosition = [a.get_position() for a in self.tail]
        oldHeadPos = self.head.get_position()
        newPos = self.head.get_position() + self.movement.value
        x = newPos.x % NUMBER_OF_CELL_WIDTH
        y = newPos.y % NUMBER_OF_CELL_HEIGHT
        newHeadPos = Pos(x,y)
        self.head.set_position(newHeadPos)
        self.tail[0].set_position(oldHeadPos)
        for i in range(1,len(self.tail)):
            self.tail[i].set_position(oldTailPosition[i-1])    

    def draw(self, surface):
        self.head.draw(surface)
        for tail in self.tail:
            tail.draw(surface)


