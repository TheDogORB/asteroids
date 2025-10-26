import pygame
import global_vars
from circleshape import CircleShape
from health import Health
from shot import Shot
from constants import *

DAMAGE_CD = 1 # in seconds

class Player(CircleShape):

    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS) 
        self.health = Health(-1)
        self.score = 0
        self.rotation = 0
        self.shoot_cd = 0
        self.damage_cd = 0

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        pygame.draw.polygon(screen, (255, 255, 255), self.triangle(), 2)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def reset_position(self):
        self.position = pygame.Vector2(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

    def update(self, dt):
        if global_vars.game_state != GAME_RUNNING:
            return
        self.shoot_cd -= dt
        self.damage_cd -= dt
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)

        if keys[pygame.K_SPACE]:
            self.shoot()
                
    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt        

    def shoot(self):
        if self.shoot_cd > 0:
            return
        self.shoot_cd = PLAYER_SHOOT_CD
        x, y = self.position
        new_shot = Shot(x, y) 
        new_shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOT_SPEED

    def take_damage(self, dt):
        self.damage_cd -= dt
        if self.damage_cd > 0:
            return 
        self.damage_cd = DAMAGE_CD
        self.health.current_health -= 1
        self.reset_position()

    def add_score(self, asteroid):
        self.score += ( ASTEROID_MAX_RADIUS + ASTEROID_MIN_RADIUS - asteroid.radius)
