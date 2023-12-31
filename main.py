import pygame
import time
from GameOfLife import GameOfLife
from ElementaryCA import ElementaryCA
from Buttons import Button

ALIVE = (255,255,255)
BACKGROUND = (40,40,40)
GRID_WIDTH = 1100
GRID_HEIGHT = 800
CELL_SIZE = 7

def main():
    """
    Initializes Pygame and creates a screen. 
    Creates instances of GameOfLife and ElementaryCA classes. 
    Creates instances of Button class for each game and exit button. 
    Runs the game selected by the user or exits the program. 
    """
    pygame.init()
    screen = pygame.display.set_mode((GRID_WIDTH, GRID_HEIGHT))

    gameoflife = GameOfLife(ALIVE, BACKGROUND, GRID_WIDTH, GRID_HEIGHT, CELL_SIZE, screen)
    elementaryca = ElementaryCA(ALIVE, BACKGROUND, GRID_WIDTH, GRID_HEIGHT, CELL_SIZE, screen)

    GameOfLife_btn = Button(550, 370, "images/gameoflife.png", "images/gameoflife_hover.png")
    ElementaryCa_btn = Button(550, 520,"images/elementaryCA.png", "images/elementaryCA_hover.png")
    exit_btn = Button(550, 670,"images/exit.png", ("images/exit_hover.png"))


    while True:
        screen.fill(BACKGROUND)
        pygame.display.set_caption("Cellular automata")

        if GameOfLife_btn.draw(screen):
            gameoflife.run()
        if ElementaryCa_btn.draw(screen):
            elementaryca.run()

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