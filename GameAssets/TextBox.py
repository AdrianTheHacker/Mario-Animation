import pygame

from GameSetup import Settings

"""
Credit: https://www.geeksforgeeks.org/python-display-text-to-pygame-window/

This creates a text box which I will display onto the screen

What I changed/added:
- Turned it into a class so I can make instances of the text box
- Added a click function to start the game
- turned it into a sprite
"""


class TextBox(pygame.sprite.Sprite):
    def __init__(self, surface, message, fontStyle, fontSize, fontColour, backgroundColour):
        self.surface = surface

        self.font = pygame.font.SysFont(fontStyle, fontSize)
        self.text = self.font.render(message, True, fontColour, backgroundColour)

        self.rect = self.text.get_rect()
        self.rect.center = (Settings.WIDTH / 2, Settings.HEIGHT / 2)

    def draw(self):
        self.surface.blit(self.text, self.rect)

    def checkInputs(self):
        if pygame.key.get_pressed()[pygame.K_SPACE]:
            Settings.animate = True

    def update(self):
        self.draw()
        self.checkInputs()