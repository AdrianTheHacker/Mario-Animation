import pygame

from GameAssets.Goomba import Goomba
from GameAssets.Mario import Mario
from GameAssets.TextBox import TextBox
from GameAssets.Thwomp import Thwomp
from GameAssets.BackgroundImage import BackgroundImage
from GameAssets.MusicPlayer import MusicPlayer
from GameSetup import Settings

pygame.init()

surface = pygame.display.set_mode((Settings.WIDTH, Settings.HEIGHT))
pygame.display.set_caption("Scratch Animation Project")

entityGroup = pygame.sprite.Group()
background = pygame.sprite.GroupSingle(BackgroundImage(surface))

for cell in range(3):
    entityGroup.add(Thwomp(Settings.tileSize, Settings.tileSize / 2,
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

gameSong = MusicPlayer("Sounds/AnimationMusic.mp3")

startScreenText = TextBox(surface, "Press Space to Start", 'Arial', 30, Settings.white, None)


def main():
    gameSong.play()
    
    while Settings.running:
        """
        Check if user exits the window
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Settings.running = False

        if Settings.animate:
            background.update()

            entityGroup.update()

        else:
            startScreenText.update()

        pygame.display.flip()
        pygame.time.Clock().tick(Settings.fps)


if __name__ == '__main__':
    main()
