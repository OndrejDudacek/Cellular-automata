import pygame
import numpy as np
import time

BACKGROUND = (40,40,40)
ALIVE = (255,255,255)
CELL_SIZE = 7
GRID_WIDTH = 1100
GRID_HEIGHT = 800
DELAY = 0.1

def update(currentGen):
    nextGen = np.zeros((GRID_HEIGHT // CELL_SIZE, GRID_WIDTH // CELL_SIZE))

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

def draw(currentGen, screen):
    for row, col in np.ndindex(currentGen.shape):
            if currentGen[row, col] == 1:
                rect = pygame.Rect(col *CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE)
                pygame.draw.rect(screen, ALIVE, rect)
            else:
                rect = pygame.Rect(col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE)
                pygame.draw.rect(screen, BACKGROUND, rect)
    pygame.display.update()

def main():
    pygame.init()

    screen = pygame.display.set_mode((GRID_WIDTH, GRID_HEIGHT))
    currentGen = np.zeros((GRID_HEIGHT // CELL_SIZE, GRID_WIDTH // CELL_SIZE))

    draw(currentGen, screen)
    pygame.display.set_caption("Game of Life")

    running = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    running = not running

                if event.key == pygame.K_DOWN:
                    DELAY = DELAY * 10
                if event.key == pygame.K_UP:
                    DELAY = DELAY / 10

                if event.key == pygame.K_c:
                    currentGen = np.zeros((GRID_HEIGHT // CELL_SIZE, GRID_WIDTH // CELL_SIZE))
                    draw(currentGen, screen)

                if event.key == pygame.K_r:
                    currentGen = np.random.randint(2, size=(GRID_HEIGHT // CELL_SIZE, GRID_WIDTH // CELL_SIZE))
                    draw(currentGen, screen)

 #               if event.key == pygame.K_s:
 #                   np.save('my_array.npy', currentGen)

                if event.key == pygame.K_1:
                    currentGen = np.load('examples/The R-pentomino.npy')
                    draw(currentGen, screen)
                if event.key == pygame.K_2:
                    currentGen = np.load('examples/Gosper glider gun.npy')
                    draw(currentGen, screen)
                if event.key == pygame.K_3:
                    currentGen = np.load('examples/example.npy')
                    draw(currentGen, screen)
                

            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()

                row = pos[1] // CELL_SIZE
                col = pos[0] // CELL_SIZE

                currentGen[row, col] = 1 - currentGen[row, col]
                draw(currentGen, screen)

        if running:
            currentGen = update(currentGen)
            draw(currentGen, screen)
            pygame.display.update()
            time.sleep(DELAY)

if __name__ == "__main__":
    main()


    
