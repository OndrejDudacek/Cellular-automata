import pygame
import numpy as np
import time

class GameOfLife:
    def __init__(self, ALIVE, BACKGROUND, GRID_WIDTH, GRID_HEIGHT, CELL_SIZE, screen):
        self.ALIVE = ALIVE
        self.BACKGROUND = BACKGROUND
        self.GRID_WIDTH = GRID_WIDTH
        self.GRID_HEIGHT = GRID_HEIGHT
        self.CELL_SIZE = CELL_SIZE
        self.screen = screen

    def update(self, currentGen):
        nextGen = np.zeros((self.GRID_HEIGHT // self.CELL_SIZE, self.GRID_WIDTH // self.CELL_SIZE))

        for row, col in np.ndindex(currentGen.shape):
            alive = np.sum(currentGen[row-1:row+2, col-1:col+2]) - currentGen[row, col]
            
            if currentGen[row, col] == 1:
                if alive < 2 or alive > 3:
                    nextGen[row, col] = 0
                elif 2 <= alive <= 3:
                    nextGen[row, col] = 1
            else:
                if alive == 3:
                    nextGen[row, col] = 1

        return nextGen

    def draw(self, currentGen):
        for row, col in np.ndindex(currentGen.shape):
                rect = pygame.Rect(col *self.CELL_SIZE, row * self.CELL_SIZE, self.CELL_SIZE, self.CELL_SIZE)
                if currentGen[row, col] == 1:
                    pygame.draw.rect(self.screen, self.ALIVE, rect)
                else:
                    pygame.draw.rect(self.screen, self.BACKGROUND, rect)
        pygame.display.update()

    def run(self):
        pygame.init()
        delay = 0.01
        currentGen = np.zeros((self.GRID_HEIGHT // self.CELL_SIZE, self.GRID_WIDTH // self.CELL_SIZE))

        self.screen.fill(self.BACKGROUND)
        self.draw(currentGen)
        
        pygame.display.set_caption("Game of Life")

        running = False

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        return False
                    
                    if event.key == pygame.K_SPACE:
                        running = not running

                    if event.key == pygame.K_DOWN and delay > 0.00125:
                        delay = delay / 2
                    if event.key == pygame.K_UP and delay < 1.2:
                        delay = delay * 2

                    if event.key == pygame.K_c:
                        currentGen = np.zeros((self.GRID_HEIGHT // self.CELL_SIZE, self.GRID_WIDTH // self.CELL_SIZE))
                        self.draw(currentGen)
                        delay = 0.01

                    if event.key == pygame.K_r:
                        currentGen = np.random.randint(2, size=(self.GRID_HEIGHT // self.CELL_SIZE, self.GRID_WIDTH // self.CELL_SIZE))
                        self.draw(currentGen)

#                   if event.key == pygame.K_s:
#                       np.save('my_array.npy', currentGen)

                    if event.key == pygame.K_1:
                        currentGen = np.load('examples/The R-pentomino.npy')
                        self.draw(currentGen)
                    if event.key == pygame.K_2:
                        currentGen = np.load('examples/Gosper glider gun.npy')
                        self.draw(currentGen)
                    if event.key == pygame.K_3:
                        currentGen = np.load('examples/example.npy')
                        self.draw(currentGen)
                    

                if pygame.mouse.get_pressed()[0]:
                    pos = pygame.mouse.get_pos()

                    row = pos[1] // self.CELL_SIZE
                    col = pos[0] // self.CELL_SIZE

                    currentGen[row, col] = 1 - currentGen[row, col]
                    self.draw(currentGen)

            if running:
                currentGen = self.update(currentGen)
                self.draw(currentGen)
                pygame.display.update()
                time.sleep(delay)


        
