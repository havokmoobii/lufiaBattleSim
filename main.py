import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from entity import Entity
from player import Player
from object import Object

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    maxim = Player(SCREEN_WIDTH/2 - 28, SCREEN_HEIGHT/2 + 12, 32, 32)
    wall = Object(SCREEN_WIDTH/2 + 4, SCREEN_HEIGHT/2 + 12, 32, 32)

    while True:
        # Close game when clicking the X button
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        # Close game when pressing the esc key    
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            return
            
        full_map = pygame.image.load("maps/02SecretSkillsCave.png").convert_alpha()
        room = pygame.Surface([253, 227], pygame.SRCALPHA)
        room.blit(full_map, (0,0), (326,664,240,224))
            
        screen.fill("#080800")
        screen.blit((pygame.transform.scale(room, (room.get_width() * 2, room.get_height() * 2))), (SCREEN_WIDTH/2 - room.get_width(), SCREEN_HEIGHT/2 - room.get_height()))
        
        maxim.update(dt)
        if maxim.check_for_collisions(wall):
            maxim.collide()

        wall.draw(screen)
        maxim.draw(screen)        

        pygame.display.flip()

        # limit framerate to 60 FPS
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()



# Next: Figure out camera, then align everything to 32x32 grid
# Then make multiple walls that actually go where they should on the map