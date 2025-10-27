import pygame
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from uielement import UiElement


class Background(UiElement):

    def __init__(self):
        self.__image_original = pygame.image.load("./img/space.png")
        self.__imagage_resized = pygame.transform.scale(self.__image_original, (SCREEN_WIDTH, SCREEN_WIDTH))
        y = ( SCREEN_HEIGHT - self.__imagage_resized.get_height() ) // 2
        super().__init__(0, y)

    def draw(self, screen, player):
       screen.blit(self.__imagage_resized, (self.x, self.y)) 
