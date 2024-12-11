from position import Position
from snake import Snake
from updatable import Updatable
from cell import Cell
from const import NUMBER_OF_CELL_HEIGHT, NUMBER_OF_CELL_WIDTH, GAME_OVER_EVENT
from random import randint
from apple import Apple
import pygame


class Grid(Updatable):
    def __init__(self, snake : Snake):
        self.cells = [Cell(Position(x,y)) for x in range(0,NUMBER_OF_CELL_WIDTH) for y in range(NUMBER_OF_CELL_HEIGHT)]
        self.snake = snake
        self.apple = Apple(Position.randomPosition(NUMBER_OF_CELL_WIDTH, NUMBER_OF_CELL_HEIGHT))

    def draw(self, surface):
        for cell in self.cells:
            cell.draw(surface)
        self.apple.draw(surface)
        self.snake.draw(surface)
        
    def update(self):
        if self.apple.get_position() == self.snake.head.get_position():
            self.snake.add_segment(Position.get_none())
            self.apple.set_position(Position.randomPosition(NUMBER_OF_CELL_WIDTH, NUMBER_OF_CELL_HEIGHT))
        elif self.snake.head.get_position() in [a.get_position() for a in self.snake.tail]:
            print("game over")
            pygame.event.post(pygame.event.Event(GAME_OVER_EVENT))  # Post custom event
        self.snake.update()


    
        