import pygame
import random
from entity import Entity
from constants import Direction

random.seed()

class Monster(Entity):

    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)

        self.sprite_sheet = pygame.image.load("sprites/enemies_overworld.png").convert_alpha()

        self.animation = 0

        self.moving = False
        self.move_frame = 0
        self.move_direction = random.choice(list(Direction))
        
        self.idle_counter = random.randrange(0, 63, 16)

    def draw(self, screen, camera):
        self.image = pygame.Surface([self.width/2, self.height/2], pygame.SRCALPHA)

        if self.moving:
            if self.move_frame <= 0:
                self.moving = False
                self.move_frame = 0
            else:
                self.move_frame -= 1
        
        if self.animation == 0 or self.animation % 64 > 32:
            self.image.blit(self.sprite_sheet, (0,0), (3,12,16,14))
        else:
            self.image.blit(self.sprite_sheet, (0,0), (22,12,16,14))

        if self.animation > 64:
            self.animation = 0
        else:
            self.animation += 1

        screen.blit((pygame.transform.scale(self.image, (32, 32))), (self.x - camera.x, self.y - camera.y))

    def update(self, dt):
        if self.moving:
            match(self.move_direction):
                case Direction.UP:
                    self.y -= 4
                case Direction.LEFT:
                    self.x -= 4
                case Direction.DOWN:
                    self.y += 4
                case Direction.RIGHT:
                    self.x += 4
        else:
            if self.idle_counter == 63:
                self.idle_counter = random.randrange(0, 63, 16)
                self.move_direction = random.choice(list(Direction))
                self.moving = True
                self.move_frame = 8
            else:
                self.idle_counter += 1