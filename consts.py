import pygame

pygame.init()
pygame.mixer.init()

SNARE_SOUND = pygame.mixer.Sound('resources/snare.wav')
KICK_SOUND = pygame.mixer.Sound('resources/kick.wav')
HH_SOUND = pygame.mixer.Sound('resources/hihat.wav')

# Color consts
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Wav consts
SNARE_POS = (150,150)
HH_POS = (80,100)
KICK_POS = (300,250)

SIZE = (650, 412)


