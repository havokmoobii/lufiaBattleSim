import pygame
from entity import Entity

class Player(Entity):

    def __init__(self, x, y):
        super().__init__(self, x)

        self.sprite_sheet = pygame.image.load("./sprites/maxim.png")

    def draw(self, screen):
    # sub-classes must override
        screen.blit(self.sprite_sheet, (30,30))

    def update(self, dt):
        # sub-classes must override
        pass