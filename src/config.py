# Screen settings
WINDOW_WIDTH = 725
WINDOW_HEIGHT = 800
FPS = 60

# Grid settings
ROWS = 40
COLS = 40
CELL_SIZE = WINDOW_WIDTH // COLS  # assuming square window

# Colors (R, G, B)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)

WALL_COLOR = BLACK
BACKGROUND_COLOR = WHITE

VISITED_COLOR = (135, 206, 250)   # Light blue for BFS exploration
PATH_COLOR = (255, 255, 0)        # Yellow for final path
START_COLOR = (0, 255, 0)         # Green
END_COLOR = (255, 0, 0)           # Red

UI_BAR_HEIGHT = 80

MAZE_HEIGHT = WINDOW_HEIGHT - UI_BAR_HEIGHT
CELL_SIZE = (WINDOW_HEIGHT - UI_BAR_HEIGHT) // ROWS

