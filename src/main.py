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
from ui import Button, BAR_COLOR


def init_pygame():
    pygame.init()
    window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("BFS Maze Solver")
    return window


def create_grid():
    return [[Cell(r, c) for c in range(COLS)] for r in range(ROWS)]


def draw_grid(window, grid):
    for row in grid:
        for cell in row:
            cell.draw(window)


def fill_explored(window, cells, step):
    for i in range(step):
        cells[i].fill(window, VISITED_COLOR)


def fill_path(window, path):
    for cell in path:
        cell.fill(window, PATH_COLOR)


def reset_bfs_state():
    return [], [], 0, False, False


def main():
    window = init_pygame()
    clock = pygame.time.Clock()

    # Build initial maze
    grid = create_grid()
    grid = generate_maze(grid)

    # Start/end cells
    start = grid[0][0]
    end = grid[ROWS - 1][COLS - 1]

    # BFS state
    exploration_order, path, bfs_step, is_animating_bfs, is_showing_path = reset_bfs_state()

    # -------- UI BUTTONS (BOTTOM BAR) --------
    UI_BAR_HEIGHT = 70
    BUTTON_W = 180
    BUTTON_H = 45
    SPACING = 40

    start_btn = Button(40, WINDOW_HEIGHT - UI_BAR_HEIGHT + 14, BUTTON_W, BUTTON_H, "Start BFS")
    regen_btn = Button(260, WINDOW_HEIGHT - UI_BAR_HEIGHT + 14, BUTTON_W, BUTTON_H, "Regenerate")
    clear_btn = Button(480, WINDOW_HEIGHT - UI_BAR_HEIGHT + 14, BUTTON_W, BUTTON_H, "Clear Visualization")

    running = True
    while running:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # ---------- CLICK EVENTS ----------
            if start_btn.is_clicked(event):
                if not is_animating_bfs:
                    exploration_order, path = bfs_solve(grid, start, end)
                    bfs_step = 0
                    is_animating_bfs = True
                    is_showing_path = False

            if regen_btn.is_clicked(event):
                grid = create_grid()
                grid = generate_maze(grid)
                start = grid[0][0]
                end = grid[ROWS - 1][COLS - 1]
                exploration_order, path, bfs_step, is_animating_bfs, is_showing_path = reset_bfs_state()

            if clear_btn.is_clicked(event):
                exploration_order, path, bfs_step, is_animating_bfs, is_showing_path = reset_bfs_state()

        # ----------------- DRAWING -----------------
        window.fill(BACKGROUND_COLOR)

        # BFS animation
        if is_animating_bfs:
            if bfs_step < len(exploration_order):
                bfs_step += 1
            else:
                is_animating_bfs = False
                is_showing_path = True

            fill_explored(window, exploration_order, bfs_step)

        if is_showing_path:
            fill_path(window, path)

        # Draw maze walls
        draw_grid(window, grid)

        # Draw bottom UI bar
        pygame.draw.rect(window, BAR_COLOR,
                         (0, WINDOW_HEIGHT - UI_BAR_HEIGHT, WINDOW_WIDTH, UI_BAR_HEIGHT))

        # Draw buttons
        start_btn.draw(window)
        regen_btn.draw(window)
        clear_btn.draw(window)

        pygame.display.update()

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
