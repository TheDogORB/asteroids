from constants import SCREEN_HEIGHT, SCREEN_WIDTH
import pygame

class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius
        self.times_crossed = 0 

    def draw(self, screen):
        pass

    def update(self, dt):
        # Logic for X coords
        x, y = self.position
        changed = False
        if x > SCREEN_WIDTH + self.radius:
            x = 0 - self.radius
            changed = True
        elif x < 0 - self.radius:
            x = SCREEN_WIDTH + self.radius
            changed = True
        # Logic for Y coords
        if y > SCREEN_HEIGHT + self.radius:
            y = 0 - self.radius
            changed = True
        elif y < 0 - self.radius:
            y = SCREEN_HEIGHT + self.radius
            changed = True
        if changed == True:
            self.times_crossed += 1
        self.position = pygame.Vector2(x, y)

    def check_for_collision(self, other):
        return self.position.distance_to(other.position) <= ( self.radius + other.radius )
