from GameAssets.GameObject import GameObject
from GameSetup import Settings

import pygame


class Mario(GameObject):
    """
    Init Method

    everything from GameObject.init() except:
        1. Direction Variable added
        2. Width and Height are set to GameSetup.tileSize
        3. Colour set to Red
    """
    def __init__(self, width, height, xCord, yCord, surface, colour, direction, speed):
        super().__init__(width, height, xCord, yCord, surface, colour)

        self.direction = direction
        self.speed = speed

        self.image = pygame.image.load("images/RobotPerson.png")

    """
    Move Method
    
    changes the x position to move Mario across the screen
    """
    def move(self):
        self.rect.x += self.speed

        if self.rect.x >= 6 * Settings.tileSize and self.rect.x < 8 * Settings.tileSize:
            self.rect.y -= Settings.tileSize
            self.image = pygame.image.load("images/RobotPersonJump.png")

        elif self.rect.x > 8 * Settings.tileSize and self.rect.x <= 10 * Settings.tileSize:
            self.rect.y += Settings.tileSize

        else:
            self.image = pygame.image.load("images/RobotPerson.png")

    def checkCollision(self):
        if self.rect.x == Settings.WIDTH:
            self.rect.x = Settings.tileSize

    """
    Update Method
    
    everything from GameObject.init() except:
        1. Also runs Move() method
        2. Runs checkCollision() method
    """
    def update(self):
        self.draw()
        self.move()
        self.checkCollision()
