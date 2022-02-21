from GameAssets.TextBox import TextBox
from GameSetup import Settings

from GameAssets.Thwomp import Thwomp
from GameAssets.Mario import Mario
from GameAssets.Goomba import Goomba

import pygame, sys

pygame.init()

surface = pygame.display.set_mode((Settings.WIDTH, Settings.HEIGHT))

entityGroup = pygame.sprite.Group()

for cell in range(3):
    entityGroup.add(Thwomp(Settings.tileSize, Settings.tileSize * 2,
                                            cell * cell * Settings.tileSize, 0,
                                            surface, Settings.grey,
                                            "D",
                                            Settings.tileSize))

entityGroup.add(Goomba(Settings.tileSize, Settings.tileSize,
                                        6 * Settings.tileSize, Settings.HEIGHT - Settings.tileSize,
                                        surface,
                                        Settings.brown,
                                        "R",
                                        Settings.tileSize))

entityGroup.add((Mario(Settings.tileSize, Settings.tileSize,
                                        0, Settings.HEIGHT - Settings.tileSize,
                                        surface,
                                        Settings.red,
                                        "R",
                                        Settings.tileSize)))

startScreenText = TextBox(surface, "Press Space to Start", 'Arial', 30, Settings.white, None)


def main():
    while Settings.running:
        """
        Check if user exits the window
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Settings.running = False

        if Settings.animate:
            surface.fill(Settings.black)
            entityGroup.update()

        else:
            startScreenText.update()

        pygame.display.flip()
        pygame.time.Clock().tick(Settings.fps)


if __name__ == '__main__':
    main()
