import math
import pygame

class Enemy:

    def __init__(self, surface):
        self.surface = surface
        self.hp = 100
        self.speed = 1
        self.x_pos = 220
        self.y_pos = 220
        self.direction = 1

    def move(self):
        self.x_pos = self.x_pos + math.cos(self.direction) * self.speed
        self.y_pos = self.y_pos + math.sin(self.direction) * self.speed

    def draw(self):
        print( (round(self.x_pos), round(self.y_pos)) )
        pygame.draw.circle(self.surface, (100, 150, 200), (round(self.x_pos), round(self.y_pos)), 5)
