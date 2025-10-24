import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_ANGLE, ASTEROID_MAX_ANGLE, ASTEROID_MIN_RADIUS


class Asteroid(CircleShape):

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
       self.position += self.velocity * dt 

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        angle = random.uniform(ASTEROID_MIN_ANGLE, ASTEROID_MAX_ANGLE)
        random_angle = self.velocity.rotate(angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        x, y = self.position

        asteroid1 = Asteroid(x, y, new_radius)
        asteroid1.velocity = random_angle * 1.2

        asteroid2 = Asteroid(x, y, new_radius)
        asteroid2.velocity = -random_angle * 1.2
