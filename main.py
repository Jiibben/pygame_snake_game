import pygame
from grid import Grid
from snake import Snake
from position import Position
from const import SCREEN_WIDTH,SCREEN_HEIGHT,GAME_OVER_EVENT, NUMBER_OF_CELL_HEIGHT, NUMBER_OF_CELL_WIDTH
from direction import Direction


pygame.init()
# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Font
font = pygame.font.SysFont("Arial", 60)
small_font = pygame.font.SysFont("Arial", 30)

#initialize game


pygame.display.set_caption('pysnake')


screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
snake = Snake(Position(4,5))
grid = Grid(snake)
is_running = True
clock = pygame.time.Clock()
is_game_over = False

    


def show_game_over_screen():
    screen.fill(BLACK)

    # Render the "Game Over" text
    game_over_text = font.render("GAME OVER", True, RED)
    text_rect = game_over_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 50))
    screen.blit(game_over_text, text_rect)

    # Render the "Press R to Restart or Q to Quit" text
    restart_text = small_font.render("Press R to Restart or Q to Quit", True, WHITE)
    restart_rect = restart_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50))
    screen.blit(restart_text, restart_rect)

    pygame.display.flip()



while is_running:
    screen.fill((255,0,0))
    if not is_game_over:
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                is_running = False
            elif event.type == GAME_OVER_EVENT:
                is_game_over = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    snake.add_movement(Direction.UP)
                elif event.key == pygame.K_RIGHT:
                    snake.add_movement(Direction.RIGHT)
                elif event.key == pygame.K_LEFT:
                    snake.add_movement(Direction.LEFT)
                elif event.key == pygame.K_DOWN:
                    snake.add_movement(Direction.DOWN)
        grid.update()
        grid.draw(screen)
    else:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    is_running = False
                elif event.key == pygame.K_r:
                    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
                    snake = Snake(Position.randomPosition(NUMBER_OF_CELL_WIDTH, NUMBER_OF_CELL_HEIGHT))
                    grid = Grid(snake)
                    is_running = True
                    clock = pygame.time.Clock()
                    is_game_over = False
        show_game_over_screen()

    
    clock.tick(9)
    pygame.display.update()

