class Mine:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.visible = False
    
    def visible(self):
        self.visible = True