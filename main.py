import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from player import Player
from monster import Monster
from object import Object
from game_map import Map

def main():
    
    #pygame.mixer.init()
    #pygame.mixer.music.load("music/07 cave")
    #pygame.mixer.music.play()
    # I guess sound it tricky with WSL
    
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    camera =pygame.Rect(0,0, SCREEN_WIDTH, SCREEN_HEIGHT)

    maxim = Player(224, 128, 32, 32)
    jelly = Monster(224, 256, 32, 32)
    walls = [
        Object(32 * 8, 32 * 13, 32, 32),
        Object(32 * 9, 32 * 13, 32, 32),
        Object(32 * 10, 32 * 13, 32, 32),
        Object(32 * 11, 32 * 13, 32, 32),
        Object(32 * 12, 32 * 13, 32, 32),
        Object(32 * 13, 32 * 12, 32, 32),
        Object(32 * 14, 32 * 11, 32, 32),
        Object(32 * 14, 32 * 10, 32, 32),
        Object(32 * 14, 32 * 9, 32, 32),
        Object(32 * 14, 32 * 8, 32, 32),
        Object(32 * 14, 32 * 7, 32, 32),
        Object(32 * 14, 32 * 6, 32, 32),
        Object(32 * 14, 32 * 5, 32, 32),
        Object(32 * 14, 32 * 4, 32, 32),
        Object(32 * 13, 32 * 3, 32, 32),
        Object(32 * 12, 32 * 2, 32, 32),
        Object(32 * 11, 32 * 1, 32, 32),
        Object(32 * 10, 32 * 1, 32, 32),
        Object(32 * 9, 32 * 1, 32, 32),
        Object(32 * 8, 32 * 1, 32, 32),
        Object(32 * 7, 32 * 1, 32, 32),
        Object(32 * 6, 32 * 1, 32, 32),
        Object(32 * 5, 32 * 1, 32, 32),
        Object(32 * 4, 32 * 1, 32, 32),
        Object(32 * 3, 32 * 1, 32, 32),
        Object(32 * 2, 32 * 2, 32, 32),
        Object(32 * 1, 32 * 3, 32, 32),
        Object(32 * 0, 32 * 11, 32, 32),
        Object(32 * 0, 32 * 10, 32, 32),
        Object(32 * 0, 32 * 9, 32, 32),
        Object(32 * 0, 32 * 8, 32, 32),
        Object(32 * 0, 32 * 7, 32, 32),
        Object(32 * 0, 32 * 6, 32, 32),
        Object(32 * 0, 32 * 5, 32, 32),
        Object(32 * 0, 32 * 4, 32, 32),
        Object(32 * 2, 32 * 13, 32, 32),
        Object(32 * 3, 32 * 13, 32, 32),
        Object(32 * 4, 32 * 13, 32, 32),
        Object(32 * 5, 32 * 13, 32, 32),
        Object(32 * 6, 32 * 13, 32, 32),
        Object(32 * 1, 32 * 12, 32, 32),
        ]
    
    exit = Object(32 * 7, 32 * 14, 32, 32)

    game_map = Map()
    game_map.load("02SecretSkillsCave")

    while True:
        # Close game when clicking the X button
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        # Close game when pressing the esc key    
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            return
        
        maxim.update(dt)
        # Monsters will only move when the player moves
        if maxim.is_moving():
            jelly.update(dt)
            
        for wall in walls:
            if maxim.check_for_collisions(wall):
                maxim.collide()

        if maxim.check_for_collisions(jelly):
            maxim.collide()

        for wall in walls:
            if jelly.check_for_collisions(wall):
                jelly.collide()

        if jelly.check_for_collisions(maxim):
            jelly.collide()

        if jelly.check_for_collisions(exit):
            jelly.collide()

        if maxim.check_for_collisions(exit):
            return

        camera.center = (maxim.x + 16, maxim.y)
        screen.fill("#080800")
        game_map.draw_background(screen, camera, 0)
        
        #npc height is going to be an issue. Maybe sort all entities in a list by y value and draw them in that order?
        jelly.draw(screen, camera)
        maxim.draw(screen, camera)
        game_map.draw_foreground(screen, camera, 0)

        #for wall in walls:
            #wall.draw(screen, camera)

        pygame.display.flip()

        # limit framerate to 60 FPS
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()



# Next: The jelly is sometimes moving out of the 16x16 grid. Find out why.
# Also figure out monster move patterns