class Enemy:

    def __init__(self, surface):
        self.surface = surface
        self.hp = 100
        self.speed = 1
        self.x_pos = 0
        self.y_pos = 0
        self.direction = 0

    def move(self):
        self.x_pos = self.x_pos + math.cos(self.direction) * self.speed
        self.y_pos = self.y_pos + math.sin(self.direction) * self.speed

    def draw(self):
        pygame.draw.circle(self.surface, (100, 150, 200), (self.x_pos, self.y_pos), 5)
        pass
