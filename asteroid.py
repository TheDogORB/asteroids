import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_CROSS_TO_LIVE, ASTEROID_MIN_ANGLE, ASTEROID_MAX_ANGLE, ASTEROID_MIN_RADIUS
from explosion import Explosion

class Asteroid(CircleShape):

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.__image = pygame.image.load("./img/asteroid.png")
        self.__image_resized = pygame.transform.scale(self.__image, (self.radius * 2, self.radius * 2))

    def draw(self, screen):
        x, y = self.position
        x -= self.radius
        y -= self.radius
        screen.blit(self.__image_resized, (x, y))
        # pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt 
        super().update(dt)
        if self.times_crossed >= ASTEROID_CROSS_TO_LIVE:
           self.kill()

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        angle = random.uniform(ASTEROID_MIN_ANGLE, ASTEROID_MAX_ANGLE)
        random_angle = self.velocity.rotate(angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        x, y = self.position

        explosion = Explosion(x, y, self.radius)
        # explosion.velocity = 0

        asteroid1 = Asteroid(x, y, new_radius)
        asteroid1.velocity = random_angle * 1.2
        asteroid1.times_crossed = self.times_crossed

        asteroid2 = Asteroid(x, y, new_radius)
        asteroid2.velocity = -random_angle * 1.2
        asteroid2.times_crossed = self.times_crossed
