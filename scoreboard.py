import pygame
from constants import UI_OFFSET
from player import Player

class ScoreBoard:

    def __init__(self, font):
        self.x = UI_OFFSET
        self.y = UI_OFFSET
        self.font = font

    def draw(self, screen, player):
        score_text = self.font.render(f"Score: {player.score}", True, "white")
        screen.blit(score_text, (self.x, self.y))


