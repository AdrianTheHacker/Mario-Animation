from GameSetup import Settings

import pygame
pygame.init()


def main():
    while Settings.running:
        """
        Check if user exits the window
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Settings.running = False

        """
        Call method that runs the screen:
        
        screen.run()
        """


if __name__ == '__main__':
    main()
