import pygame

class Entity(pygame.sprite.Sprite):

    def __init__(self, color, width, height, x, y):
        pygame.sprite.Sprite.__init__(self)

        self.sprite_sheet = pygame.image.load("./sprites/maxim.png").convert_alpha()

        self.image = pygame.Surface([width, height], pygame.SRCALPHA)

        self.image.get_rect()

        self.move_frame = 0

        self.x = x
        self.y = y

    def draw(self, screen):
        # sub-classes must override

        if self.move_frame == 31:
            self.move_frame = 0            
        else:
            self.move_frame += 1

        if self.move_frame > 15:
            self.image.blit(self.sprite_sheet, (0,0), (22,5,16,26))
        else:
            self.image.blit(self.sprite_sheet, (0,0), (4,5,16,26))

        screen.blit((pygame.transform.scale(self.image, (32, 52))), (self.x, self.y))

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            self.y -= 4
        if keys[pygame.K_a]:
            self.x -= 4
        if keys[pygame.K_s]:
            self.y += 4
        if keys[pygame.K_d]:
            self.x += 4
        