class View:
    def __init__(self, pygame, screen, grid):
        self.grid = grid
        self.pygame = pygame
        self.screen = screen
    
    def draw(self):
        self.screen.fill((20, 20, 20))
        self.draw_title()
        self.write_text("Mines: " + str(self.grid.mines_left), 10, 75, 20)
        for y, row in enumerate(self.grid.grid):
            for x, cell in enumerate(row):
                color = "gray"
                if cell.is_open:
                    color = "white"
                if cell.is_flagged:
                    color = "red"
                self.pygame.draw.rect(self.screen, color, (x * self.grid.cell_size + self.grid.x + 1, y * self.grid.cell_size + self.grid.y + 1, self.grid.cell_size - 2, self.grid.cell_size - 2))
        
        if self.grid.mine_spawner.visible_mines:
            for mine in self.grid.mine_spawner.get_mines():
                self.pygame.draw.circle(self.screen, "black", (mine.x * self.grid.cell_size + self.grid.x + self.grid.cell_size // 2, mine.y * self.grid.cell_size + self.grid.y + self.grid.cell_size // 2), self.grid.cell_size // 3)
        
        if self.grid.number_spawner.numbers:
            self.pygame.font.init()
            font = self.pygame.font.SysFont('Comic Sans MS', round(self.grid.cell_size / 1.5))
            for number in self.grid.number_spawner.numbers:
                if self.grid.grid[number.y][number.x].is_open and number.number > 0:
                    text = font.render(str(number.number), True, (0, 128, 0))
                    self.screen.blit(text, (number.x * self.grid.cell_size + self.grid.x + self.grid.cell_size // 2 - 5, number.y * self.grid.cell_size + self.grid.y + self.grid.cell_size // 2 - 10))

        if self.grid.win_state:
            self.write_text("You win!", 75, 200, 100, (0, 150, 0))
        if self.grid.mine_spawner.visible_mines and not self.grid.win_state:
            self.write_text("You lose!", 75, 200, 100, (150, 0, 0))

        self.pygame.display.update()
    
    def draw_title(self):
        self.pygame.font.init()
        font = self.pygame.font.SysFont('Comic Sans MS', 50)
        for i, letter in enumerate("Minesweeper"):
            text = font.render(letter, True, ((50+i*3247)%255, (255+i*412)%255, (200+i*60)%255))
            self.screen.blit(text, (30+i*43, 7 if i % 2 == 0 else 17))
    
    def write_text(self, text, x, y, size, color=(255, 255, 255)):
        font = self.pygame.font.SysFont('Comic Sans MS', size)
        text = font.render(text, True, color)
        self.screen.blit(text, (x, y))
        