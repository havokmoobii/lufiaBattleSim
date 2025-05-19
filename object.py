import pygame
from entity import Entity

class Object(Entity):

    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)

    def draw(self, screen, camera):
        # Temporary for testing
        pygame.draw.rect(screen, "pink", (self.x - camera.x, self.y - camera.y, self.width, self.height))

    def update(self, dt):
        # sub-classes must override
        pass