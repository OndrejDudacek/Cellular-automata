import pygame
import time
from GameOfLife import GameOfLife
from Buttons import Button

ALIVE = (255,255,255)
BACKGROUND = (40,40,40)
GRID_WIDTH = 1100
GRID_HEIGHT = 800
CELL_SIZE = 7

def main():
    pygame.init()
    screen = pygame.display.set_mode((GRID_WIDTH, GRID_HEIGHT))
    pygame.display.set_caption("Cellular automata")

    gameoflife = GameOfLife(ALIVE, BACKGROUND, GRID_WIDTH, GRID_HEIGHT, CELL_SIZE, screen)

    GameOfLife_btn = Button(550, 370, "images/gameoflife.png")
    ElementaryCa_btn = Button(550, 520,"images/elementaryCA.png")
    exit_btn = Button(550, 670,"images/exit.png")

    gameoflife_running = False

    while True:
        screen.fill(BACKGROUND)

        if GameOfLife_btn.draw(screen):
            gameoflife.run()
        if ElementaryCa_btn.draw(screen):
            print("Elementary CA")

        if exit_btn.draw(screen):
            pygame.quit()
            exit()

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        
        time.sleep(0.01)

if __name__ == "__main__":
    main()