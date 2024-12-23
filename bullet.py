import pygame
from circleshape import *
from constants import *

class Bullet(CircleShape):
    def __init__(self, x, y, rotation):
        super().__init__(x, y, BULLET_RADIUS)
        self.rotation = rotation

    def draw(self, screen):
        pygame.draw.circle(screen,(255,255,255), self.position, BULLET_RADIUS, STD_LINE_WIDTH)
    
    def update(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * dt * BULLET_SPEED
