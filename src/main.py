import pygame
import sys

from config import (
    WINDOW_WIDTH, WINDOW_HEIGHT, FPS,
    BACKGROUND_COLOR, ROWS, COLS
)

from cell import Cell


def init_pygame():
    """Initialize pygame and create window."""
    pygame.init()
    window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("BFS Maze Solver")
    return window


def create_grid():
    """Create a 2D grid of Cell objects."""
    grid = [[Cell(r, c) for c in range(COLS)] for r in range(ROWS)]
    return grid


def draw_grid(window, grid):
    """Draws the grid walls."""
    for row in grid:
        for cell in row:
            cell.draw(window)


def main():
    window = init_pygame()
    clock = pygame.time.Clock()

    # Build initial empty grid (full walls)
    grid = create_grid()

    running = True
    while running:
        clock.tick(FPS)

        # Handle window events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # Keyboard controls will be added later
            # if event.type == pygame.KEYDOWN:
            #     if event.key == pygame.K_s:    # start BFS
            #     if event.key == pygame.K_r:    # regenerate maze

        # Fill background
        window.fill(BACKGROUND_COLOR)

        # Draw the static grid (walls only)
        draw_grid(window, grid)

        # Update frame
        pygame.display.update()

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
