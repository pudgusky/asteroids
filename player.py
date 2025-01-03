import pygame
from circleshape import *
from shot import *
from constants import *

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.cooldown = 0
    
    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        pygame.draw.polygon(screen, (255, 255, 255), self.triangle(), STD_LINE_WIDTH)
        #pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, 2)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt):
        keys = pygame.key.get_pressed()
        self.cooldown -= dt

        if keys[pygame.K_a]:
            self.rotate(-1 * dt)
        if keys[pygame.K_d]:
            self.rotate( 1 * dt)
        if keys[pygame.K_w]:
            self.move( 1 * dt) 
        if keys[pygame.K_s]:
            self.move(-1 * dt)
        if keys[pygame.K_SPACE] and self.cooldown <= 0:
            self.shoot()
            self.cooldown = PLAYER_SHOOT_COOLDOWN

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt
    
    def shoot(self):
        shot = Shot(self.position.x, self.position.y, self.rotation)

        