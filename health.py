import pygame

from constants import SCREEN_HEIGHT, SCREEN_WIDTH

DAMAGE_CD = 1 # in seconds

class Health:

    def __init__(self, count):
        self.max_health = count
        self.current_health = count
        self.__full_heart = pygame.image.load("./img/heart.png")
        self.__empty_heart = pygame.image.load("./img/heart_empty.png")
        self.__damage_cd = 0

    def take_damage(self, dt):
        self.__damage_cd -= dt
        if self.__damage_cd > 0:
            return 0
        self.__damage_cd = DAMAGE_CD
        self.current_health -= 1
        return 1

    def is_alive(self):
        return self.current_health >= 0

    def draw(self, screen, dt):
        for health in range(self.max_health):
            img_offset_y = SCREEN_HEIGHT - self.__full_heart.get_height()
            img_offset_x = health * self.__full_heart.get_width()
            if health < self.current_health:
                screen.blit(self.__full_heart, (img_offset_x, img_offset_y))
            screen.blit(self.__empty_heart, (img_offset_x, img_offset_y))
