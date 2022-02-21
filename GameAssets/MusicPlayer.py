import pygame

pygame.mixer.init()


class MusicPlayer():
    def __init__(self, songPath):
        self.songPath = songPath

    def play(self):
        pygame.mixer.music.load(self.songPath)
        pygame.mixer.music.play(-1)
