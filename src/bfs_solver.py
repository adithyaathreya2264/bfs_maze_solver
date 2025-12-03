from collections import deque
from config import ROWS, COLS

def get_accessible_neighbors(grid, cell):
    """Return neighbors that are reachable (no walls between them)."""
    neighbors = []
    r, c = cell.row, cell.col

    # TOP
    if not cell.walls["top"] and r > 0:
        neighbors.append(grid[r - 1][c])

    # RIGHT
    if not cell.walls["right"] and c < COLS - 1:
        neighbors.append(grid[r][c + 1])

    # BOTTOM
    if not cell.walls["bottom"] and r < ROWS - 1:
        neighbors.append(grid[r + 1][c])

    # LEFT
    if not cell.walls["left"] and c > 0:
        neighbors.append(grid[r][c - 1])

    return neighbors


def bfs_solve(grid, start, end):
    """
    BFS to find shortest path from start to end.
    Returns:
        exploration_order: list of cells in order of visit
        path: final shortest path from start to end
    """
    queue = deque()
    queue.append(start)

    visited = set()
    visited.add((start.row, start.col))

    parent = {}  # maps each cell to the cell it came from

    exploration_order = []

    while queue:
        current = queue.popleft()
        exploration_order.append(current)

        if current == end:
            break  # reached goal

        neighbors = get_accessible_neighbors(grid, current)

        for nb in neighbors:
            key = (nb.row, nb.col)
            if key not in visited:
                visited.add(key)
                parent[nb] = current
                queue.append(nb)

    # Reconstruct path
    path = []
    if end in parent or end == start:
        cell = end
        while cell != start:
            path.append(cell)
            cell = parent[cell]
        path.append(start)
        path.reverse()

    return exploration_order, path
