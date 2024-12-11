from drawable import Drawable
import pygame
from position import Position


from const import CELL_HEIGHT, CELL_WIDTH

class GridObject(Drawable):
    def __init__(self, pos : Position, color : pygame.Color, width = CELL_WIDTH, height=CELL_HEIGHT):
        self.pos = pos
        self.color = color
        self.width = width
        self.height = height

    def get_position(self):
        return self.pos.copy()
    
    def set_position(self, pos: Position):
        self.pos = pos

    def draw(self, surface):
    
       pygame.draw.rect(surface, self.color, pygame.Rect(self.pos.x* CELL_WIDTH, self.pos.y * CELL_HEIGHT, self.width, self.height))
 
