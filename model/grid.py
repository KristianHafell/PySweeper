import model.grid_cell as grid_cell
import model.mines.mine_spawner as mine_spawner
import model.numbers.number_spawner as number_spawner

class Grid:
    def __init__(self, x, y, width, height, cell_size, mines):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.cell_size = cell_size
        self.grid = [[grid_cell.GridCell(x, y) for x in range(width // cell_size)] for y in range(height // cell_size)]
        self.mine_spawner = mine_spawner.MineSpawner(self, mines)
        self.number_spawner = number_spawner.NumberSpawner(self, self.mine_spawner)
        self.win_state = False
        self.mines_left = 0
        self.update_mines_left()
    
    def get_cell(self, x, y):
        x = (x - self.x) // self.cell_size
        y = (y - self.y) // self.cell_size
        if 0 <= x < self.width // self.cell_size and 0 <= y < self.height // self.cell_size:
            return self.grid[y][x]
        return None
    
    def open(self, x, y):
        cell = self.grid[y][x]
        if cell and not cell.is_flagged:
            cell.open()
            if self.mine_spawner.is_mine(x, y):
                self.mine_spawner.visible()
            if self.number_spawner.get_number(x, y) == 0:
                for i in range(-1, 2):
                    for j in range(-1, 2):
                        if 0 <= x+i < self.width//self.cell_size and 0 <= y+j < self.height//self.cell_size:
                            if not self.grid[y+j][x+i].is_open:
                                self.open(x+i, y+j)
    
    def open_around(self, x, y):
        num_flags = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                if 0 <= x+i < self.width//self.cell_size and 0 <= y+j < self.height//self.cell_size:
                    if self.grid[y+j][x+i].is_flagged:
                        num_flags += 1
        if num_flags == self.number_spawner.get_number(x, y):
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if 0 <= x+i < self.width//self.cell_size and 0 <= y+j < self.height//self.cell_size:
                        if not self.grid[y+j][x+i].is_flagged:
                            self.open(x+i, y+j)
    
    def update_mines_left(self):
        mines_left = len(self.mine_spawner.get_mines()) - sum([cell.is_flagged for row in self.grid for cell in row])

    def is_win(self):
        self.win_state = all([cell.is_open or self.mine_spawner.is_mine(cell.x, cell.y) for row in self.grid for cell in row])
        if self.win_state:
            self.mark_all_mines()
        return self.win_state

    def mark_all_mines(self):
        for mine in self.mine_spawner.get_mines():
            self.grid[mine.y][mine.x].flag()

        