from GameAssets.GameObject import GameObject

from GameSetup import Settings

import pygame


class Goomba(GameObject):
    def __init__(self, width, height, xCord, yCord, surface, colour, direction, speed):
        super().__init__(width, height, xCord, yCord, surface, colour)

        self.direction = direction
        self.speed = speed

        self.image = pygame.image.load("images/Bolder.png")

    def move(self):
        if self.direction == 'R':
            self.rect.x += self.speed

        elif self.direction == 'L':
            self.rect.x -= self.speed

    def checkCollision(self):
        if self.rect.x == 6 * Settings.tileSize:
            self.direction = 'R'

        elif self.rect.x == 10 * Settings.tileSize:
            self.direction = 'L'

    def update(self):
        self.draw()
        self.move()
        self.checkCollision()