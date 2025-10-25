import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from score import Score

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

    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    AsteroidField.containers = (updatable)
    asteroid_field = AsteroidField()

    Player.containers = (updatable, drawable)

    # Init objects
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    score = Score()

    # Game loop
    while True:
        # Quit event to close the game upon clicking on close
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # Go through all objects in groups
        updatable.update(dt)
        for asteroid in asteroids:
            if player.check_for_collision(asteroid):
                print("Game over!")
                print(f"Final score: {score.score}")
                sys.exit()

            for shot in shots:
                if asteroid.check_for_collision(shot):
                    shot.kill()
                    asteroid.split()
                    score.add_score(asteroid)

        # Render BG as black (0,0,0)
        pygame.Surface.fill(screen, "black")

        # Draw score
        score_text = font.render(f"Score: {score.score}", True, "white")
        screen.blit(score_text, (10, 10))

        for obj in drawable:
            obj.draw(screen)

        # Update content of the screen
        pygame.display.flip()

        # Limit FPS to 60, save delta time 
        dt = fps_clock.tick(60) / 1000

if __name__ == "__main__":
    main()
