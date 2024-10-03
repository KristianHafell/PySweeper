class Number:
    def __init__(self, x, y, number):
        self.x = x
        self.y = y
        self.number = number
        self.visible = False
    
    def visible(self):
        self.visible = True