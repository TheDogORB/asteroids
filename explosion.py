import pygame
from circleshape import CircleShape
from constants import ASTEROID_EXPLOSION_TIME, ASTEROID_KINDS, ASTEROID_MAX_RADIUS, ASTEROID_MIN_RADIUS

class Explosion(CircleShape):

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.__image = pygame.image.load("./img/explosion.png")
        self.__explosion_time = 0

    def draw(self, screen):
        # Calculate 'size'/'radius' of explosion based on stage going from smallest to biggest as all explosions do (not implosion)
        diameter = 2 * ASTEROID_MAX_RADIUS
        size = diameter * (0.9 + self.__explosion_time)
        resized_image = pygame.transform.scale(self.__image, (size, size))

        # Calculate new center for the image to pop at
        x, y = self.position
        x -= resized_image.get_width()//2
        y -= resized_image.get_height()//2

        screen.blit(resized_image, (x, y)) 

    def update(self, dt):
        self.__explosion_time += dt 
        if self.__explosion_time >= ASTEROID_EXPLOSION_TIME:
            self.kill()
