from GameAssets.GameObject import GameObject
from GameSetup import Settings

import pygame


class Thwomp(GameObject):
    """
        Init Method

        everything from GameObject.init() except:
            1. Direction Variable added
            2. Width and Height are set to GameSetup.tileSize
            3. Colour set to Grey
    """
    def __init__(self, width, height, xCord, yCord, surface, colour, direction, speed):
        super().__init__(width, height, xCord, yCord, surface, colour)

        self.direction = direction
        self.speed = speed

        self.image = pygame.image.load("images/Spike.png")

    """
    Move Method

    changes the y position to move Thwomp across the screen
    """
    def move(self):
        self.rect.y += self.speed

    def checkCollision(self):
        if self.rect.y == Settings.HEIGHT:
            self.rect.y = 0

    """
    Update Method

    everything from GameObject.init() except:
        1. Also runs Move() method
    """
    def update(self):
        self.draw()
        self.move()
        self.checkCollision()
