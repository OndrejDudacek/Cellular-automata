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

    def draw(self, currentGen, screen):
        for row, col in np.ndindex(currentGen.shape):
                if currentGen[row, col] == 1:
                    rect = pygame.Rect(col *self.CELL_SIZE, row * self.CELL_SIZE, self.CELL_SIZE, self.CELL_SIZE)
                    pygame.draw.rect(screen, self.alive, rect)
                else:
                    rect = pygame.Rect(col * self.CELL_SIZE, row * self.CELL_SIZE, self.CELL_SIZE, self.CELL_SIZE)
                    pygame.draw.rect(screen, self.BACKGROUND, rect)
        pygame.display.update()

    def main(self):
        delay = 0.01
        currentGen = np.zeros((self.GRID_HEIGHT // self.CELL_SIZE, self.GRID_WIDTH // self.CELL_SIZE))

        GameOfLife.draw(currentGen, self.screen)
        pygame.display.set_caption("Game of Life")

        running = False

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        return
                    
                    if event.key == pygame.K_SPACE:
                        running = not running

                    if event.key == pygame.K_DOWN:
                        delay = delay / 10
                    if event.key == pygame.K_UP:
                        delay = delay * 10

                    if event.key == pygame.K_c:
                        currentGen = np.zeros((self.GRID_HEIGHT // self.CELL_SIZE, self.GRID_WIDTH // self.CELL_SIZE))
                        GameOfLife.draw(currentGen, self.screen)
                        delay = 0.01

                    if event.key == pygame.K_r:
                        currentGen = np.random.randint(2, size=(self.GRID_HEIGHT // self.CELL_SIZE, self.GRID_WIDTH // self.CELL_SIZE))
                        GameOfLife.draw(currentGen, self.screen)

#                   if event.key == pygame.K_s:
#                       np.save('my_array.npy', currentGen)

                    if event.key == pygame.K_1:
                        currentGen = np.load('examples/The R-pentomino.npy')
                        GameOfLife.draw(currentGen, self.screen)
                    if event.key == pygame.K_2:
                        currentGen = np.load('examples/Gosper glider gun.npy')
                        GameOfLife.draw(currentGen, self.screen)
                    if event.key == pygame.K_3:
                        currentGen = np.load('examples/example.npy')
                        GameOfLife.draw(currentGen, self.screen)
                    

                if pygame.mouse.get_pressed()[0]:
                    pos = pygame.mouse.get_pos()

                    row = pos[1] // self.CELL_SIZE
                    col = pos[0] // self.CELL_SIZE

                    currentGen[row, col] = 1 - currentGen[row, col]
                    GameOfLife.draw(currentGen, self.screen)

            if running:
                currentGen = GameOfLife.update(currentGen)
                GameOfLife.draw(currentGen, self.screen)
                pygame.display.update()
                time.sleep(delay)


        
