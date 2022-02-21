import pygame


class BackgroundImage(pygame.sprite.Sprite):
    def __init__(self, surface):
        super().__init__()
        self.surface = surface

        self.image = pygame.image.load("images/AnimationBackground.png")

        self.rect = self.image.get_rect(topleft=(0, -100))

    def draw(self):
        self.surface.blit(self.image, self.rect)

    def update(self):
        self.draw()
