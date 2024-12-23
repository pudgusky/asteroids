import pygame
from circleshape import *
from constants import *

class Shot(CircleShape):
    def __init__(self, x, y, rotation):
        super().__init__(x, y, SHOT_RADIUS)
        self.rotation = rotation


    def draw(self, screen):
        pygame.draw.circle(screen, (255,255,255), self.position, SHOT_RADIUS, STD_LINE_WIDTH)
    
    def update(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * dt * PLAYER_SHOOT_SPEED
