import pygame
import random
from circleshape import *
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, (255,255,255), self.position, self.radius, STD_LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius == ASTEROID_MIN_RADIUS:
            return
        else:
            angle = random.uniform(ASTEROID_SPLIT_AVG_ANGLE - ASTEROID_SPLIT_ANGLE_VARIANCE, ASTEROID_SPLIT_AVG_ANGLE + ASTEROID_SPLIT_ANGLE_VARIANCE)
            first = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)
            first.velocity = self.velocity.rotate(angle) * ASTEROID_SPLIT_ACCELERATION
            second = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)
            second.velocity = self.velocity.rotate(-1 * angle) * ASTEROID_SPLIT_ACCELERATION