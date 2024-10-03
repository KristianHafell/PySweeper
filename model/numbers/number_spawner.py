import model.numbers.number as number

class NumberSpawner:
    def __init__(self, grid, mine_spawner):
        self.grid = grid
        self.mine_spawner = mine_spawner
        self.numbers = []
        self.spawn()

    def spawn(self):
        for y in range(self.grid.height//self.grid.cell_size):
            for x in range(self.grid.width//self.grid.cell_size):
                if not self.mine_spawner.is_mine(x, y):
                    self.numbers.append(number.Number(x, y, self.get_number(x, y)))
    
    def get_number(self, x, y):
        n = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                if self.mine_spawner.is_mine(x+i, y+j):
                    n += 1
        return n