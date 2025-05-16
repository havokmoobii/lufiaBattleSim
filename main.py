import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from entity import Entity

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    maxim = Entity("white", 16, 26, SCREEN_WIDTH/2 - 28, SCREEN_HEIGHT/2 - 8)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        full_map = pygame.image.load("maps/02SecretSkillsCave.png").convert_alpha()
        room = pygame.Surface([253, 227], pygame.SRCALPHA)
        room.blit(full_map, (0,0), (326,664,240,224))
            
        screen.fill("#080800")
        screen.blit((pygame.transform.scale(room, (room.get_width() * 2, room.get_height() * 2))), (SCREEN_WIDTH/2 - room.get_width(), SCREEN_HEIGHT/2 - room.get_height()))
        maxim.draw(screen)
        maxim.update(dt)

        pygame.display.flip()

        # limit framerate to 60 FPS
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()