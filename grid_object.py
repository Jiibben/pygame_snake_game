from drawable import Drawable
import pygame
from position import Position
from const import *



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

    @staticmethod
    def from_pos_to_pixel(pos : Position):
        return (pos.x * CELL_WIDTH, pos.y * CELL_HEIGHT)

    def draw(self, surface):
       x,y = GridObject.from_pos_to_pixel(self.pos)
       pygame.draw.rect(surface, self.color, pygame.Rect(x, y , self.width, self.height))
 
