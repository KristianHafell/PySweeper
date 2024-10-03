from random import randint
import model.mines.mine as mine

class MineSpawner:
    def __init__(self, grid, mines):
        self.grid = grid
        self.visible_mines = False
        self.mines = []
        self.spawn_mines(mines)
    
    def spawn_mines(self, n):
        cells = self.get_random_cells(n)
        self.mines = [mine.Mine(cell[0], cell[1]) for cell in cells]
    
    def get_mines(self):
        return self.mines

    def get_random_cells(self, n):
        cells = []
        x, y = self.get_random_cell()
        for _ in range(n):
            while [x,y] in cells:
                x, y = self.get_random_cell()
            cells.append([x, y])
        return cells
    
    def get_random_cell(self):
        x = randint(0, self.grid.width//self.grid.cell_size - 1)
        y = randint(0, self.grid.height//self.grid.cell_size - 1)
        return x,y

    def is_mine(self, x, y):
        for mine in self.mines:
            if mine.x == x and mine.y == y:
                return True
        return False

    def visible(self):
        self.visible_mines = True
        