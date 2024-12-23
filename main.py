import pygame
from constants import *
from player import *
from asteroids import *
from asteroidfield import *


def main():
	pygame.init()
	print("Starting asteroids!")
	print(f"Screen width: {SCREEN_WIDTH}")
	print(f"Screen height: {SCREEN_HEIGHT}")
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	clock = pygame.time.Clock()
	dt = 0
	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	asteroids = pygame.sprite.Group()
	shots = pygame.sprite.Group()
	Player.containers = (updatable, drawable)
	Asteroid.containers = (asteroids, updatable, drawable)
	AsteroidField.containers = (updatable)
	Shot.containers = (shots, updatable, drawable)
	player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
	asteroidfield = AsteroidField()
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
		screen.fill((0,0,0))
		for draws in drawable:
			draws.draw(screen)
		for updates in updatable:
			updates.update(dt)
		for asteroid in asteroids:
			if player.collision(asteroid):
				print("Game over!")
				return
			for shot in shots:
				if shot.collision(asteroid):
					shot.kill()
					asteroid.split()
		pygame.display.flip()
		dt = clock.tick(60) / 1000


if __name__ == "__main__":
	main()
