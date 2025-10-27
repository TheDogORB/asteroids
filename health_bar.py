import pygame
from player import Player, Health
from ui_element import UiElement
from constants import SCREEN_HEIGHT, SCREEN_WIDTH, UI_OFFSET

class HealthBar(UiElement):
    def __init__(self, count):
        self.__full_heart = pygame.image.load("./img/heart.png")
        self.__empty_heart = pygame.image.load("./img/heart_empty.png")
        
        x = UI_OFFSET
        y = UI_OFFSET + SCREEN_WIDTH - self.__full_heart.get_height() 
        super().__init__(0, y)

    def draw(self, screen, player):
        if not self.visibility:
            return
        for health in range(player.health.max_health):
            img_offset_y = SCREEN_HEIGHT - self.__full_heart.get_height()
            img_offset_x = health * self.__full_heart.get_width()
            if health < player.health.current_health:
                screen.blit(self.__full_heart, (img_offset_x, img_offset_y))
            screen.blit(self.__empty_heart, (img_offset_x, img_offset_y))
