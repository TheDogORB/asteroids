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
        self.__image = pygame.transform.scale(pygame.image.load("./img/player.png"), (PLAYER_RADIUS * 2, PLAYER_RADIUS * 2))
        # Unit stats
        self.health = Health(5)
        self.score = 0
        # Unit movement/positional
        self.rotation = 0
        # Cooldowns
        self.shoot_cd = 0
        self.damage_cd = 0

    def draw(self, screen):
        rotated_image = pygame.transform.rotate(self.__image, -self.rotation)
        rotated_rect = rotated_image.get_rect(center=self.position)
        screen.blit(rotated_image, rotated_rect.topleft)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def reset_position(self):
        self.rotation = 0
        self.velocity = pygame.Vector2(0, 0)
        self.position = pygame.Vector2(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

    def update(self, dt):
        if global_vars.game_state != GAME_RUNNING:
            return
        super().update(dt)
        self.shoot_cd -= dt
        self.damage_cd -= dt
        keys = pygame.key.get_pressed()

        # Movement keys
        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt, 1)
        elif keys[pygame.K_s]:
            self.move(-dt, 1)
        else:
            self.move(dt, 0)
        # Space key
        if keys[pygame.K_SPACE]:
            self.shoot()

        # Acceleration
        self.position += self.velocity * dt
                
    def move(self, dt, moving):
        movement = pygame.Vector2(0, 1).rotate(self.rotation)
        # self.position += movement * PLAYER_SPEED * dt        
        if moving != 0:
            if self.velocity.length() > PLAYER_MAX_SPEED:
                self.velocity = self.velocity.normalize() * PLAYER_MAX_SPEED
            else:
                self.velocity += movement * PLAYER_SPEED * PLAYER_ACCELERATION * moving * dt
        else:
            if self.velocity.length() > 0:
                deceleration = PLAYER_DECELERATION * dt 
                new_speed = max(0, self.velocity.length() - deceleration)
                if new_speed == 0:
                    self.velocity = pygame.Vector2(0, 0)
                else:
                    self.velocity = self.velocity.normalize() * new_speed


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
