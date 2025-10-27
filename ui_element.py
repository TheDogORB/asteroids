class UiElement:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.visibility = True

    def toggle(self):
        self.visibility = not self.visibility

    def draw(self, screen, player):
        pass
