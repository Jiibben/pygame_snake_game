from direction import Direction
from grid_object import GridObject
from position import Position
import pygame
from const import CELL_HEIGHT, CELL_WIDTH

class SnakeSegment(GridObject):
    def __init__(self, pos):
        super().__init__(pos, (0,255,0))

    def draw(self, surface):
       pygame.draw.rect(surface, self.color, pygame.Rect(self.pos.x* CELL_WIDTH, self.pos.y * CELL_HEIGHT, self.width, self.height))
 



