import pygame

pygame.init()

pygame.mixer.music.load('D:\Mari\Documents\Paradox Interactive\Victoria II\HPM\music\queensscherzo.mp3')

pygame.mixer.music.play(loops=0, start=0.0)

pygame.event.wait()

