import pygame
import numpy as np
import time
from GameOfLife import GameOfLife

ALIVE = (255,255,255)
BACKGROUND = (40,40,40)
GRID_WIDTH = 1100
GRID_HEIGHT = 800
CELL_SIZE = 7

pygame.init()

screen = pygame.display.set_mode((GRID_WIDTH, GRID_HEIGHT))
pygame.display.set_caption("Cellular automata")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        
                
    #GameOfLife = GameOfLife(ALIVE, BACKGROUND, GRID_WIDTH, GRID_HEIGHT, CELL_SIZE)