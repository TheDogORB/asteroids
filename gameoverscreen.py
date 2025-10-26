import pygame
import global_vars
from constants import GAME_RUNNING, SCREEN_HEIGHT, SCREEN_WIDTH, UI_OFFSET
from uielement import UiElement

class GameOverScreen(UiElement):

    def __init__(self):
        super().__init__(UI_OFFSET, UI_OFFSET)
        self.visibility = False
        self.font_large = pygame.font.Font(None, 80)
        self.font_medium = pygame.font.Font(None, 60)

    def draw(self, screen, player):
        if not self.visibility:
            return
        game_over_overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        game_over_title = self.font_large.render(f"Game over!", True, "white")
        final_score = self.font_medium.render(f"Score: {player.score}", True, "white")

        game_over_overlay.set_alpha(200)
        game_over_overlay.fill((25, 25, 25))
        
        padding = 50
        game_over_rect = game_over_title.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2))
        final_score_rect = final_score.get_rect(center=(SCREEN_WIDTH//2, game_over_rect.bottom + padding))

        screen.blit(game_over_overlay, (0, 0))
        screen.blit(game_over_title, game_over_rect)
        screen.blit(final_score, final_score_rect)
