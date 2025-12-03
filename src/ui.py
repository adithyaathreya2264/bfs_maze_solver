import pygame

BUTTON_COLOR = (150, 150, 150)
BUTTON_HOVER = (180, 180, 180)
TEXT_COLOR = (255, 255, 255)
BAR_COLOR = (220, 220, 220)

pygame.font.init()
FONT = pygame.font.SysFont("times new roman", 20)


class Button:
    def __init__(self, x, y, w, h, text):
        self.rect = pygame.Rect(x, y, w, h)
        self.text = text

    def draw(self, window):
        mouse_pos = pygame.mouse.get_pos()

        # Hover effect
        if self.rect.collidepoint(mouse_pos):
            color = BUTTON_HOVER
        else:
            color = BUTTON_COLOR

        pygame.draw.rect(window, color, self.rect, border_radius=8)

        # Draw text centered
        label = FONT.render(self.text, True, TEXT_COLOR)
        label_rect = label.get_rect(center=self.rect.center)
        window.blit(label, label_rect)

    def is_clicked(self, event):
        """Returns True if this button was clicked."""
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                return True
        return False
