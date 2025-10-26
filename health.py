import pygame
from constants import SCREEN_HEIGHT, SCREEN_WIDTH

class Health:

    def __init__(self, count):
        self.max_health = count
        self.current_health = count

    def is_alive(self):
        return self.current_health >= 0
