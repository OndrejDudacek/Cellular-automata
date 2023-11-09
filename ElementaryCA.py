import numpy as np
import pygame
import time

class ElementaryCA:
    def __init__(self, ALIVE, BACKGROUND, GRID_WIDTH, GRID_HEIGHT, CELL_SIZE, screen):
        self.ALIVE = ALIVE
        self.BACKGROUND = BACKGROUND
        self.GRID_WIDTH = GRID_WIDTH
        self.GRID_HEIGHT = GRID_HEIGHT
        self.CELL_SIZE = CELL_SIZE
        self.screen = screen
        self.mainGrid = np.zeros((self.GRID_HEIGHT // self.CELL_SIZE, self.GRID_WIDTH // self.CELL_SIZE))
        self.currentRow = 0
        self.ruleset = "00011110" #30


    def nextGen(self):
        nextGen = np.copy(self.mainGrid)
        ruleset_int = [int(bit) for bit in self.ruleset]

        for col in range(1, self.GRID_WIDTH // self.CELL_SIZE - 1):
            neighbourhood = str(int(self.mainGrid[self.currentRow][col-1])) + str(int(self.mainGrid[self.currentRow][col])) + str(int(self.mainGrid[self.currentRow][col+1]))
            nextGen[self.currentRow + 1][col] = ruleset_int[7 - int(neighbourhood, 2)]

        self.currentRow += 1

        if self.currentRow == self.GRID_HEIGHT // self.CELL_SIZE - 1:
            nextGen[:-1] = self.mainGrid[1:]
            self.currentRow -= 1

        self.mainGrid = nextGen
    

    def draw(self):
        for col in range(self.GRID_WIDTH // self.CELL_SIZE):
            rect = pygame.Rect(col * self.CELL_SIZE, self.currentRow * self.CELL_SIZE, self.CELL_SIZE, self.CELL_SIZE)
            if self.mainGrid[self.currentRow][col] == 1:
                pygame.draw.rect(self.screen, self.ALIVE, rect)
            else:
                pygame.draw.rect(self.screen, self.BACKGROUND, rect)
        pygame.display.update()


    def drawStart(self):
        self.mainGrid = np.zeros((self.GRID_HEIGHT // self.CELL_SIZE, self.GRID_WIDTH // self.CELL_SIZE))
        self.mainGrid[0, self.GRID_WIDTH // self.CELL_SIZE // 2] = 1

        for row, col in np.ndindex(self.mainGrid.shape):
            rect = pygame.Rect(col * self.CELL_SIZE, row * self.CELL_SIZE, self.CELL_SIZE, self.CELL_SIZE)
            if self.mainGrid[row][col] == 1:
                pygame.draw.rect(self.screen, self.ALIVE, rect)
            else:
                pygame.draw.rect(self.screen, self.BACKGROUND, rect)
        pygame.display.update()


    def run(self):
        pygame.init()
        delay = 0.01
        running = False
        
        pygame.display.set_caption("Elementary Ca")
        self.drawStart()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
    
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        return False
                    
                    if event.key == pygame.K_SPACE:
                        running = not running

                    if event.key == pygame.K_c:
                        self.drawStart()
    
                    if event.key == pygame.K_DOWN and delay > 0.00125:
                        delay = delay / 2
                    if event.key == pygame.K_UP and delay < 1.2:
                        delay = delay * 2
            
            if running:
                self.nextGen()
                self.draw()
            
            time.sleep(delay)