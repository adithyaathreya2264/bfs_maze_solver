import pygame
import sys
from config import WINDOW_WIDTH, WINDOW_HEIGHT, FPS, BACKGROUND_COLOR

def init_pygame():
    """Initialize pygame and create window."""
    pygame.init()
    window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("BFS Maze Solver")
    return window


def main():
    window = init_pygame()
    clock = pygame.time.Clock()

    running = True
    while running:
        clock.tick(FPS)

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # --- We will add keyboard controls here later ---
            # if event.type == pygame.KEYDOWN:
            #     if event.key == pygame.K_s:  # start BFS
            #     if event.key == pygame.K_r:  # regenerate maze

        # Fill background
        window.fill(BACKGROUND_COLOR)

        # --- Drawing will come here in later phases ---

        pygame.display.update()

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
