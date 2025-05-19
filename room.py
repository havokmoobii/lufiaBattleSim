import pygame
from object import Object

class Room:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.background = None
        self.foreground = None

    def load(self, background_map, foreground_map):
        self.background = pygame.Surface([self.width, self.height], pygame.SRCALPHA)
        self.background.blit(background_map, (0,0), (self.x,self.y,self.width,self.height))
        self.foreground = pygame.Surface([self.width, self.height], pygame.SRCALPHA)
        self.foreground.blit(foreground_map, (0,0), (self.x,self.y,self.width,self.height))

    def draw_background(self, screen, camera):
        screen.blit((pygame.transform.scale(self.background, (self.width * 2, self.height * 2))), (0 - camera.x, 0 - camera.y))

    def draw_foreground(self, screen, camera):
        screen.blit((pygame.transform.scale(self.foreground, (self.width * 2, self.height * 2))), (0 - camera.x, 0 - camera.y))