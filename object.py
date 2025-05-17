import pygame
from entity import Entity

class Object(Entity):

    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)

    def draw(self, screen):
        # sub-classes must override
        pygame.draw.rect(screen, "pink", (self.x, self.y, self.width, self.height))
        pass

    def update(self, dt):
        # sub-classes must override
        pass