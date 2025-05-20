import pygame
from constants import Direction

class Entity:

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def draw(self, screen):
        # sub-classes must override
        pass

    def update(self, dt):
        # sub-classes must override
        pass

    def check_for_collisions(self, other):
        if self.x >= other.x + other.width or self.x + self.width <= other.x:
            return False
        if self.y >= other.y + other.height or self.y + self.height <= other.y:
            return False
        return True
    
    def collide(self):
        match(self.move_direction):
            case Direction.UP:
                self.y += 4
            case Direction.LEFT:
                self.x += 4
            case Direction.DOWN:
                self.y -= 4
            case Direction.RIGHT:
                self.x -= 4