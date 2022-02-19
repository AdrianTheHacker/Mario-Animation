from GameSetup import Settings

from GameAssets.Thwomp import Thwomp
from GameAssets.Mario import Mario
from GameAssets.Goomba import Goomba

import pygame

pygame.init()

surface = pygame.display.set_mode((Settings.WIDTH, Settings.HEIGHT))

enemyGroup = pygame.sprite.Group()
mario = pygame.sprite.GroupSingle(Mario(Settings.tileSize, Settings.tileSize,
                                        0, Settings.HEIGHT - Settings.tileSize,
                                        surface,
                                        Settings.red,
                                        "R",
                                        Settings.tileSize))

for cell in range(3):
    enemyGroup.add(Thwomp(Settings.tileSize, Settings.tileSize * 2,
                          cell * cell * Settings.tileSize, 0,
                          surface, Settings.grey,
                         "D",
                          Settings.tileSize))

enemyGroup.add(Goomba(Settings.tileSize, Settings.tileSize,
                                        6 * Settings.tileSize, Settings.HEIGHT - Settings.tileSize,
                                        surface,
                                        Settings.brown,
                                        "R",
                                        Settings.tileSize))


def main():
    while Settings.running:
        """
        Check if user exits the window
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Settings.running = False

        surface.fill(Settings.black)
        mario.update()
        enemyGroup.update()

        pygame.display.flip()
        pygame.time.Clock().tick(Settings.fps)


if __name__ == '__main__':
    main()
