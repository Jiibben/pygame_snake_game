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
        self.apples = [apple]
        self.level = 1
    def draw(self, surface):
        for cell in self.cells:
            cell.draw(surface)
        for apple in self.apples:
            apple.draw(surface)
        self.snake.draw(surface)
        
    def __next_level_apple(self):
        for i in range(0,self.level):
            self.apples.append(Apple.get_random_apple_not_on_snake(self.snake))

    def update(self):
        #check if apple and snake get on the same cell
        for i in range(len(self.apples)):
            if self.apples[i].get_position() == self.snake.head.get_position():
                
            #if it's the case add an empty Position
                self.snake.add_segment(Position.get_none())
                #create another apple when one is eaten
                pygame.event.post(pygame.event.Event(APPLE_EATEN_EVENT))
                del self.apples[i]
                if len(self.apples) == 0:
                    print("huh")
                    self.level +=1
                    self.__next_level_apple()
                break
        #check if snake collide with his tail
        if self.snake.head.get_position() in [a.get_position() for a in self.snake.tail]:
            pygame.event.post(pygame.event.Event(GAME_OVER_EVENT))  # Post custom event
        self.snake.update()


    
        