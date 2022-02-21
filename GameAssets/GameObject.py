import pygame


class GameObject(pygame.sprite.Sprite):
    """
    Init Method

    parameters:
        1. Surface
        2. Width, Height
        3. xCord, yCord
        4. Colour

    creates GameObject image and GameObject rect
    """
    def __init__(self, width, height, xCord, yCord, surface, colour):
        super().__init__()
        self.surface = surface
        self.colour = colour

        self.image = pygame.Surface([width, height])
        self.image.fill(self.colour)

        self.rect = self.image.get_rect(topleft=(xCord, yCord))

    """
    Draw Method
    
    uses the pygame.blit() method to display GameObject on screen
    """
    def draw(self):
        self.surface.blit(self.image, self.rect)

    """
    Update Method
    
    constantly runs the Draw Method
    """
    def update(self):
        self.draw()
