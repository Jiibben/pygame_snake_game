import pygame
from grid import Grid
from snake import Snake
from position import Position
from const import *
from direction import Direction
from apple import Apple

pygame.init()
# Colors

# Fonts
font = pygame.font.SysFont("Arial", 60)
small_font = pygame.font.SysFont("Arial", 30)
score_font = pygame.font.SysFont("Arial",28)
#initialize game
pygame.display.set_caption('PySnake')


screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
snake = Snake(Position.randomPosition(NUMBER_OF_CELL_WIDTH, NUMBER_OF_CELL_HEIGHT))
apple = Apple.get_random_apple_not_on_snake(snake)
grid = Grid(snake, apple)
is_running = True
clock = pygame.time.Clock()
is_game_over = False
score = 0
speed = 5
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

def render_score():
    score_text = score_font.render(f"Score: {score}", True, (200,10,10))
    text_rect = score_text.get_rect(topleft=(0,0))
    screen.blit(score_text, text_rect)

while is_running:
    screen.fill((255,0,0))
    if not is_game_over:
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                is_running = False
            elif event.type == GAME_OVER_EVENT:
                is_game_over = True
            elif event.type == APPLE_EATEN_EVENT:
                score +=1
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_x:
                    speed *=2
                elif event.key == pygame.K_y:
                    speed /=2
                elif event.key == pygame.K_UP and snake.movement != Direction.DOWN:
                    snake.add_movement(Direction.UP)
                elif event.key == pygame.K_RIGHT and snake.movement != Direction.LEFT:
                    snake.add_movement(Direction.RIGHT)
                elif event.key == pygame.K_LEFT and snake.movement != Direction.RIGHT:
                    snake.add_movement(Direction.LEFT)
                elif event.key == pygame.K_DOWN and snake.movement != Direction.UP:
                    snake.add_movement(Direction.DOWN)
        grid.update()
        grid.draw(screen)
        render_score()
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
                    apple = Apple.get_random_apple_not_on_snake(snake)
                    grid = Grid(snake, apple)
                    is_running = True
                    is_game_over = False
                    score = 0
        show_game_over_screen()

    
    clock.tick(speed)
    pygame.display.update()

