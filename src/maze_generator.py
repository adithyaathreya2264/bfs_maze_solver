import random
from config import ROWS, COLS

def get_unvisited_neighbors(grid, cell):
    """Returns all unvisited neighbors of a cell."""
    neighbors = []
    r, c = cell.row, cell.col

    # TOP neighbor
    if r > 0 and not grid[r - 1][c].visited:
        neighbors.append(grid[r - 1][c])

    # RIGHT neighbor
    if c < COLS - 1 and not grid[r][c + 1].visited:
        neighbors.append(grid[r][c + 1])

    # BOTTOM neighbor
    if r < ROWS - 1 and not grid[r + 1][c].visited:
        neighbors.append(grid[r + 1][c])

    # LEFT neighbor
    if c > 0 and not grid[r][c - 1].visited:
        neighbors.append(grid[r][c - 1])

    return neighbors


def remove_walls(current, next_cell):
    """Remove walls between two adjacent cells."""
    dx = next_cell.col - current.col
    dy = next_cell.row - current.row

    # Moving right
    if dx == 1:
        current.walls["right"] = False
        next_cell.walls["left"] = False

    # Moving left
    if dx == -1:
        current.walls["left"] = False
        next_cell.walls["right"] = False

    # Moving down
    if dy == 1:
        current.walls["bottom"] = False
        next_cell.walls["top"] = False

    # Moving up
    if dy == -1:
        current.walls["top"] = False
        next_cell.walls["bottom"] = False


def generate_maze(grid):
    """Generates a perfect maze using DFS backtracking."""
    stack = []
    
    # Start at (0, 0) — you can change this later
    current = grid[0][0]
    current.visited = True
    stack.append(current)

    while stack:
        current = stack[-1]
        neighbors = get_unvisited_neighbors(grid, current)

        if neighbors:
            next_cell = random.choice(neighbors)
            next_cell.visited = True

            remove_walls(current, next_cell)

            stack.append(next_cell)
        else:
            stack.pop()

    # Reset visited state for BFS later
    for row in grid:
        for cell in row:
            cell.visited = False

    return grid
