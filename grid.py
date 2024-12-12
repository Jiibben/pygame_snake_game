from position import Position
from snake import Snake
from updatable import Updatable
from cell import Cell
from const import *
from apple import Apple
import pygame


class Grid(Updatable):
    def __init__(self, snake : Snake, apple: Apple):
        self.cells = [Cell(Position(x,y)) for x in range(0,NUMBER_OF_CELL_WIDTH) for y in range(NUMBER_OF_CELL_HEIGHT)]
        self.snake = snake
        self.apple = apple

    def draw(self, surface):
        for cell in self.cells:
            cell.draw(surface)

        self.apple.draw(surface)
        self.snake.draw(surface)
        
    def update(self):
        #check if apple and snake get on the same cell
        if self.apple.get_position() == self.snake.head.get_position():
            #if it's the case add an empty Position
            self.snake.add_segment(Position.get_none())
            #create another apple when one is eaten
            self.apple = Apple.get_random_apple_not_on_snake(self.snake)
            pygame.event.post(pygame.event.Event(APPLE_EATEN_EVENT))

        #check if snake collide with his tail
        elif self.snake.head.get_position() in [a.get_position() for a in self.snake.tail]:
            pygame.event.post(pygame.event.Event(GAME_OVER_EVENT))  # Post custom event
        self.snake.update()


    
        