import pygame
import sys
from explosion import Explosion
import global_vars

from constants import *

from gameoverscreen import GameOverScreen
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from scoreboard import ScoreBoard
from shot import Shot
from healthbar import HealthBar

def main():
    # Init pygam
    pygame.init()
    pygame.font.init()

    # Init font for Score
    font = pygame.font.Font(None, 30)
    
    # Init screen and timers for FPS lock
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    fps_clock = pygame.time.Clock()
    dt = 0

    # Init grps
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    explosions = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    AsteroidField.containers = (updatable)
    Explosion.containers = (updatable, drawable)
    Player.containers = (updatable, drawable)

    # Init objects
    asteroid_field = AsteroidField()
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    score_board = ScoreBoard()
    health_bar = HealthBar(player.health.max_health)
    game_over_screen = GameOverScreen()

    global global_vars

    # Game loop
    while True:
        # Quit event to close the game upon clicking on close
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # Go through all objects in groups and update game's logic
        updatable.update(dt)
        if player.health.is_alive() and global_vars.game_state == GAME_RUNNING:
            for asteroid in asteroids:
                if player.check_for_collision(asteroid):
                    player.take_damage(dt)

                for shot in shots:
                    if asteroid.check_for_collision(shot):
                        shot.kill()
                        asteroid.split()
                        player.add_score(asteroid)
        else:
            global_vars.game_state = GAME_OVER
            score_board.visibility = False
            health_bar.visibility = False
            game_over_screen.visibility = True

        # Render BG as black (0,0,0)
        pygame.Surface.fill(screen, "black")

        # Draw objects in pygame.sprit.Group()
        for obj in drawable:
            obj.draw(screen)

        # Draw UI elements
        score_board.draw(screen, player)
        health_bar.draw(screen, player)
        game_over_screen.draw(screen, player)

        # Update content of the screen
        pygame.display.flip()

        # Limit FPS to 60, save delta time 
        dt = fps_clock.tick(60) / 1000

if __name__ == "__main__":
    main()
