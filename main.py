import numpy as np
from scipy import ndimage
import pygame 
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

h, w, d = 10, 10, 10

kernel = np.array([[[1, 1, 1], [1, 1, 1], [1, 1, 1]], [[1, 1, 1], [1, 0, 1], [1, 1, 1]], [[1, 1, 1], [1, 1, 1], [1, 1, 1]]])
state = (np.random.rand(h, w, d) > 0.5) * 1.0


def game_of_life(state):
    neighborHood = ndimage.convolve(state, kernel, mode="constant")
    c2 = (neighborHood == 6) * 1
    c3 = (neighborHood == 7) * 1
    c4 = (neighborHood == 8) * 1
    stay = ((c2 + c3 + c4) > 0) * 1
    live = (neighborHood == 4) * 1
    return state * stay + live

// Execute and draw board
if __name__ == "__main__":
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_zlabel("z")
    ax.grid(True)

    while True:
        state = game_of_life(state)
        ax.voxels(state, edgecolors='gray')
        plt.show(block=False)
        plt.pause(0.001)
        ax.clear()




