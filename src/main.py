import pygame
import sys

from config import (
    WINDOW_WIDTH, WINDOW_HEIGHT, FPS,
    BACKGROUND_COLOR, ROWS, COLS
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


def main():
    window = init_pygame()
    clock = pygame.time.Clock()

    # Build grid
    grid = create_grid()

    # Generate maze using DFS recursive backtracking
    grid = generate_maze(grid)

    # Define start and end cells
    start = grid[0][0]
    end = grid[ROWS - 1][COLS - 1]

    running = True
    while running:
        clock.tick(FPS)

        # Handle window events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # Temporary BFS trigger
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    exploration_order, path = bfs_solve(grid, start, end)
                    print("BFS complete!")
                    print("Visited:", len(exploration_order), "cells")
                    print("Path length:", len(path))

                # Regenerate maze later (Phase 6)
                # if event.key == pygame.K_r:
                #     grid = create_grid()
                #     grid = generate_maze(grid)

        # Fill background
        window.fill(BACKGROUND_COLOR)

        # Draw the generated maze
        draw_grid(window, grid)

        pygame.display.update()

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
