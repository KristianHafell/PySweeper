class GridCell:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.is_flagged = False
        self.is_open = False
    
    def open(self):
        self.is_open = True
        self.is_flagged = False
    
    def toggle_flag(self):
        self.is_flagged = not self.is_flagged
    
    def flag(self):
        self.is_flagged = True
    
