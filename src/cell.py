import pygame
from config import CELL_SIZE, WALL_COLOR

class Cell:
    def __init__(self, row, col):
        self.row = row
        self.col = col

        # Walls of the cell
        self.walls = {
            "top": True,
            "right": True,
            "bottom": True,
            "left": True
        }

        # Used later for maze generation (DFS)
        self.visited = False

    def draw(self, window):
        """Draws the cell walls on the pygame window."""

        x = self.col * CELL_SIZE
        y = self.row * CELL_SIZE

        # Draw walls if present
        if self.walls["top"]:
            pygame.draw.line(window, WALL_COLOR, (x, y), (x + CELL_SIZE, y), 2)

        if self.walls["right"]:
            pygame.draw.line(window, WALL_COLOR, (x + CELL_SIZE, y), (x + CELL_SIZE, y + CELL_SIZE), 2)

        if self.walls["bottom"]:
            pygame.draw.line(window, WALL_COLOR, (x + CELL_SIZE, y + CELL_SIZE), (x + CELL_SIZE, y), 2)

        if self.walls["left"]:
            pygame.draw.line(window, WALL_COLOR, (x, y + CELL_SIZE), (x, y), 2)

    def fill(self, window, color):
        x = self.col * CELL_SIZE
        y = self.row * CELL_SIZE
        rect = pygame.Rect(x, y, CELL_SIZE, CELL_SIZE)
        pygame.draw.rect(window, color, rect)
