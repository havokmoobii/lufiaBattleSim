import pygame
from object import Object
from room import Room

class Map:
    def __init__(self):
        self.background = None
        self.foreground = None
        self.rooms = []

    def load(self, map_name):
        self.background = pygame.image.load(f"maps/{map_name}.png").convert_alpha()
        self.foreground = pygame.image.load(f"maps/{map_name}Foreground.png").convert_alpha()
        
        #Need to figure out how to read this from a file. Might just doing something with another .py file
        self.rooms.append(Room(326,664,240,224))
        
        for room in self.rooms:
            room.load(self.background, self.foreground)

    def draw_background(self, screen, camera, room_index):
        self.rooms[room_index].draw_background(screen, camera)

    def draw_foreground(self, screen, camera, room_index):
        self.rooms[room_index].draw_foreground(screen, camera)