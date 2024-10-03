from index import restart


class Controller:
    def __init__(self, pygame, screen, grid, view):
        self.pygame = pygame
        self.screen = screen
        self.grid = grid
        self.view = view
    
    def update(self):
        mouse_pos = self.get_mouse_pos()
        hover_cell = self.grid.get_cell(mouse_pos[0], mouse_pos[1])
        if hover_cell:
            for event in self.pygame.event.get():
                if event.type == self.pygame.MOUSEBUTTONDOWN and event.button == 1 and not ( self.grid.mine_spawner.visible_mines or self.grid.win_state):
                    if not self.grid.mine_spawner.visible_mines:
                        self.grid.open(hover_cell.x, hover_cell.y)
                    self.grid.is_win()
                    self.grid.update_mines_left()
                
                if event.type == self.pygame.KEYDOWN:
                    if event.key == self.pygame.K_SPACE and not (self.grid.mine_spawner.visible_mines or self.grid.win_state):
                        if self.grid.grid[hover_cell.y][hover_cell.x].is_open:
                            self.grid.open_around(hover_cell.x, hover_cell.y)
                        else:
                            hover_cell.toggle_flag()
                        self.grid.is_win()
                        self.grid.update_mines_left()
                    if event.key == self.pygame.K_r:
                        restart()

                
    
    def get_mouse_pos(self):
        return self.pygame.mouse.get_pos()