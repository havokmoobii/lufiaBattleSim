import pygame
from enum import Enum

class Direction(Enum):
    UP = "up",
    LEFT = "left",
    DOWN = "down",
    RIGHT = "right"

class Entity(pygame.sprite.Sprite):

    def __init__(self, color, width, height, x, y):
        pygame.sprite.Sprite.__init__(self)

        self.width = width
        self.height = height

        self.sprite_sheet = pygame.image.load("sprites/maxim.png").convert_alpha()

        self.moving = False
        self.move_frame = 0
        self.move_direction = Direction.DOWN

        self.x = x
        self.y = y

    def draw(self, screen):
        # sub-classes must override

        self.image = pygame.Surface([self.width, self.height], pygame.SRCALPHA)

        match(self.move_direction):
            case Direction.UP:
                sprite_sheet_x_offest = 78
            case Direction.LEFT:
                sprite_sheet_x_offest = 41
            case Direction.DOWN:
                sprite_sheet_x_offest = 5
            case Direction.RIGHT:
                sprite_sheet_x_offest = 41

        if self.moving:
            if self.move_frame <= 0:
                self.moving = False
                self.move_frame = 0
            else:
                self.move_frame -= 2

        if self.move_frame == 0 or self.move_frame % 16 > 8:
            self.image.blit(self.sprite_sheet, (0,0), (4,sprite_sheet_x_offest,16,26))
        else:
            self.image.blit(self.sprite_sheet, (0,0), (22,sprite_sheet_x_offest,16,26))

        if self.move_direction == Direction.LEFT:
            self.image = pygame.transform.flip(self.image, True, False)

        screen.blit((pygame.transform.scale(self.image, (32, 52))), (self.x, self.y))

    def update(self, dt):
        keys = pygame.key.get_pressed()

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

        if not self.moving:
            if keys[pygame.K_w]:
                self.move_direction = Direction.UP
                self.moving = True
                self.move_frame = 16
        if not self.moving:
            if keys[pygame.K_s]:
                self.move_direction = Direction.DOWN
                self.moving = True
                self.move_frame = 16
        if not self.moving:
            if keys[pygame.K_a]:
                self.move_direction = Direction.LEFT
                self.moving = True
                self.move_frame = 16
        if not self.moving:
            if keys[pygame.K_d]:
                self.move_direction = Direction.RIGHT
                self.moving = True
                self.move_frame = 16
            
        
        
            
        