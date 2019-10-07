import numpy as np
from scipy import signal
import pygame 

#set initial width and height of the board
h, w = 700, 700

#initialize game
pygame.init()
screen = pygame.display.set_mode((w, h))

kernel = np.array([[1, 1, 1], [1, 0, 1], [1, 1, 1]])
state = (np.random.rand(h, w) > 0.5) * 1.0

def game_of_life():
    neighborHood = signal.convolve2d(state, kernel, mode='same', boundary='fill', fillvalue=0)
    c0 = (neighborHood == 2) * 1
    c1 = (neighborHood == 3) * 1
    return state * c0 + c1

while True:
    for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()
    
    state = game_of_life()
    surface = pygame.surfarray.make_surface(state * 50)
    screen.blit(surface, (1, 1))
    pygame.display.flip()


