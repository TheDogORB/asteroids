import pygame
from constants import GAME_RUNNING, UI_OFFSET
import global_vars
from player import Player
from uielement import UiElement

class ScoreBoard(UiElement):

    def __init__(self):
        super().__init__(UI_OFFSET, UI_OFFSET)
        self.font = pygame.font.Font(None, 30)

    def draw(self, screen, player):
        if not self.visibility:
            return
        score_text = self.font.render(f"Score: {player.score}", True, "white")
        screen.blit(score_text, (self.x, self.y))


