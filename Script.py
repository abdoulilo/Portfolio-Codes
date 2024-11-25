import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 300
SCREEN_HEIGHT = 600
GRID_WIDTH = 10
GRID_HEIGHT = 20
BLOCK_SIZE = SCREEN_WIDTH // GRID_WIDTH

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
CYAN = (0, 255, 255)
YELLOW = (255, 255, 0)
MAGENTA = (255, 0, 255)
ORANGE = (255, 165, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Tetromino shapes
SHAPES = [
    [[1, 1, 1, 1]],  # I
    [[1, 1], [1, 1]],  # O
    [[0, 1, 0], [1, 1, 1]],  # T
    [[1, 0, 0], [1, 1, 1]],  # L
    [[0, 0, 1], [1, 1, 1]],  # J
    [[1, 1, 0], [0, 1, 1]],  # S
    [[0, 1, 1], [1, 1, 0]]   # Z
]

# Colors for each shape
SHAPE_COLORS = [CYAN, YELLOW, MAGENTA, ORANGE, BLUE, GREEN, RED]

class Tetromino:
    def __init__(self, shape, color):
        self.shape = shape
        self.color = color
        self.x = GRID_WIDTH // 2 - len(shape[0]) // 2
        self.y = 0

    def rotate(self):
        self.shape = [list(row) for row in zip(*self.shape[::-1])]

    def flip(self):
        self.shape = [list(row)[::-1] for row in zip(*self.shape)]

def create_grid(locked_positions={}):
    grid = [[BLACK for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]
    for (x, y), color in locked_positions.items():
        grid[y][x] = color
    return grid

def draw_background(surface, step):
    """
    Draws a gradient background that changes dynamically over time.

    :param surface: Pygame surface to draw on.
    :param step: Controls the dynamic color change (can be the frame count or another variable).
    """
    for i in range(0, SCREEN_HEIGHT, BLOCK_SIZE):
        # Change the colors dynamically using modulo arithmetic
        r = (50 + step * 2) % 255
        g = (100 + step * 3) % 255
        b = (150 + step * 4) % 255
        color = (r, g, b)
        pygame.draw.rect(surface, color, (0, i, SCREEN_WIDTH, BLOCK_SIZE))

def valid_space(tetromino, grid):
    accepted_positions = [[(x, y) for x in range(GRID_WIDTH) if grid[y][x] == BLACK] for y in range(GRID_HEIGHT)]
    accepted_positions = [x for sub in accepted_positions for x in sub]

    formatted_shape = convert_shape_format(tetromino)

    for pos in formatted_shape:
        if pos not in accepted_positions:
            if pos[1] > -1:
                return False
    return True

def convert_shape_format(tetromino):
    positions = []
    shape_format = tetromino.shape
    for i, line in enumerate(shape_format):
        row = list(line)
        for j, column in enumerate(row):
            if column == 1:
                positions.append((tetromino.x + j, tetromino.y + i))
    return positions

def check_lost(positions):
    for pos in positions:
        x, y = pos
        if y < 1:
            return True
    return False

def clear_rows(grid, locked):
    increment = 0
    for i in range(len(grid)-1, -1, -1):
        row = grid[i]
        if BLACK not in row:
            increment += 1
            ind = i
            for j in range(len(row)):
                try:
                    del locked[(j, i)]
                except:
                    continue
    if increment > 0:
        for key in sorted(list(locked), key=lambda x: x[1])[::-1]:
            x, y = key
            if y < ind:
                newKey = (x, y + increment)
                locked[newKey] = locked.pop(key)
    return increment

def draw_grid(surface, grid):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            pygame.draw.rect(surface, grid[i][j], (j*BLOCK_SIZE, i*BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE), 0)
    for i in range(GRID_HEIGHT):
        pygame.draw.line(surface, WHITE, (0, i*BLOCK_SIZE), (SCREEN_WIDTH, i*BLOCK_SIZE))
    for j in range(GRID_WIDTH):
        pygame.draw.line(surface, WHITE, (j*BLOCK_SIZE, 0), (j*BLOCK_SIZE, SCREEN_HEIGHT))

def draw_window(surface, grid, score):
    draw_background(surface, score)
    draw_grid(surface, grid)
    draw_text_middle(surface, f'Score: {score}', 30, WHITE)
    pygame.display.update()

def draw_text_middle(surface, text, size, color):
    font = pygame.font.SysFont('comicsans', size, bold=True)
    label = font.render(text, 1, color)
    surface.blit(label, (SCREEN_WIDTH//2 - label.get_width()//2, 30))

def main():
    locked_positions = {}
    grid = create_grid(locked_positions)

    change_piece = False
    run = True
    current_piece = Tetromino(random.choice(SHAPES), random.choice(SHAPE_COLORS))
    next_piece = Tetromino(random.choice(SHAPES), random.choice(SHAPE_COLORS))
    clock = pygame.time.Clock()
    fall_time = 0
    level_time = 0
    score = 0
    step = 0

    while run:
        grid = create_grid(locked_positions)
        fall_speed = 0.27

        fall_time += clock.get_rawtime()
        level_time += clock.get_rawtime()
        clock.tick()

        if level_time / 1000 > 5:
            level_time = 0
            if fall_speed > 0.12:
                fall_speed -= 0.005

        if fall_time / 1000 >= fall_speed:
            fall_time = 0
            current_piece.y += 1
            if not valid_space(current_piece, grid) and current_piece.y > 0:
                current_piece.y -= 1
                change_piece = True

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    current_piece.x -= 1
                    if not valid_space(current_piece, grid):
                        current_piece.x += 1
                if event.key == pygame.K_RIGHT:
                    current_piece.x += 1
                    if not valid_space(current_piece, grid):
                        current_piece.x -= 1
                if event.key == pygame.K_DOWN:
                    current_piece.y += 1
                    if not valid_space(current_piece, grid):
                        current_piece.y -= 1
                if event.key == pygame.K_UP:
                    current_piece.flip()
                    if not valid_space(current_piece, grid):
                        current_piece.flip()

        shape_pos = convert_shape_format(current_piece)

        for i in range(len(shape_pos)):
            x, y = shape_pos[i]
            if y > -1:
                grid[y][x] = current_piece.color

        if change_piece:
            for pos in shape_pos:
                locked_positions[(pos[0], pos[1])] = current_piece.color
            current_piece = next_piece
            next_piece = Tetromino(random.choice(SHAPES), random.choice(SHAPE_COLORS))
            change_piece = False

            score += clear_rows(grid, locked_positions) * 10

        draw_background(surface, step)
        draw_window(surface, grid, score)
        step += 1

        if check_lost(locked_positions):
            run = False

    pygame.display.quit()

def main_menu():
    run = True
    while run:
        surface.fill(BLACK)
        pygame.font.init()
        font = pygame.font.SysFont('comicsans', 30)
        label = font.render('Press any key to play', 1, WHITE)
        surface.blit(label, (SCREEN_WIDTH//2 - label.get_width()//2, SCREEN_HEIGHT//2 - label.get_height()//2))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                main()
    
    pygame.quit()

# Entry Point
if __name__ == "__main__":
    surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('Tetris')
    main_menu()
