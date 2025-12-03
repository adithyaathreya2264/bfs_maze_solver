import pygame
import sys

from config import (
    WINDOW_WIDTH, WINDOW_HEIGHT, FPS,
    BACKGROUND_COLOR, ROWS, COLS,
    VISITED_COLOR, PATH_COLOR
)

from cell import Cell
from maze_generator import generate_maze
from bfs_solver import bfs_solve


def init_pygame():
    """Initialize pygame and create window."""
    pygame.init()
    window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("BFS Maze Solver")
    return window


def create_grid():
    """Create a 2D grid of Cell objects."""
    return [[Cell(r, c) for c in range(COLS)] for r in range(ROWS)]


def draw_grid(window, grid):
    """Draws the grid walls for each cell."""
    for row in grid:
        for cell in row:
            cell.draw(window)


def fill_explored(window, cells, step):
    """Fill all BFS visited cells up to current step."""
    for i in range(step):
        cells[i].fill(window, VISITED_COLOR)


def fill_path(window, path):
    """Fill final BFS path."""
    for cell in path:
        cell.fill(window, PATH_COLOR)


def main():
    window = init_pygame()
    clock = pygame.time.Clock()

    # Build grid
    grid = create_grid()
    grid = generate_maze(grid)

    # Define start and end cells
    start = grid[0][0]
    end = grid[ROWS - 1][COLS - 1]

    # Animation state variables
    exploration_order = []
    path = []

    bfs_step = 0
    is_animating_bfs = False
    is_showing_path = False

    running = True
    while running:
        clock.tick(FPS)

        # ---------------- EVENT HANDLING ----------------
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # Start BFS animation
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s and not is_animating_bfs:
                    exploration_order, path = bfs_solve(grid, start, end)
                    bfs_step = 0
                    is_animating_bfs = True
                    is_showing_path = False

        # ---------------- DRAWING ----------------
        window.fill(BACKGROUND_COLOR)

        # Animate BFS exploration
        if is_animating_bfs:
            if bfs_step < len(exploration_order):
                bfs_step += 1
            else:
                is_animating_bfs = False
                is_showing_path = True  # show path after BFS completes

            fill_explored(window, exploration_order, bfs_step)

        # Draw final path
        if is_showing_path:
            fill_path(window, path)

        # Draw maze walls on top of colored cells
        draw_grid(window, grid)

        pygame.display.update()

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
