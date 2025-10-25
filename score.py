from asteroid import Asteroid
from constants import ASTEROID_MAX_RADIUS, ASTEROID_KINDS, ASTEROID_MIN_RADIUS

class Score:

    def __init__(self):
        self.score = 0

    def add_score(self, asteroid):
        self.score += ( ASTEROID_MAX_RADIUS + ASTEROID_MIN_RADIUS - asteroid.radius)
