import pygame
from circleshape import CircleShape
from constants import SHOT_RADIUS

class Shot(CircleShape):

    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)
        self.__image = pygame.image.load("./img/shot.png")
        self.__image_resized = pygame.transform.scale(self.__image, (SHOT_RADIUS * 2, SHOT_RADIUS * 2))
        
    def draw(self, screen):
        # pygame.draw.circle(screen, "white", self.position, self.radius, width=2)
        x, y = self.position
        x -= self.radius
        y -= self.radius
        screen.blit(self.__image_resized, (x, y))

    def update(self, dt):
        self.position += self.velocity * dt
        super().update(dt)
