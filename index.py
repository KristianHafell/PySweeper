import pygame
import view.game_view as game_view
import model.grid as grid_cells
import controller.game_controller as game_controller

def play():
    pygame.init()
    screen = pygame.display.set_mode((520, 610))
    grid = grid_cells.Grid(10, 100, 500, 500, 25, mines=100)
    view = game_view.View(pygame, screen, grid)
    controller = game_controller.Controller(pygame, screen, grid, view)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        view.draw()
        controller.update()

def restart():
    pygame.quit()
    play()

if __name__ == "__main__":
    play()
