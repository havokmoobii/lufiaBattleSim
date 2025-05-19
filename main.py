import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from player import Player
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
        for wall in walls:
            if maxim.check_for_collisions(wall):
                maxim.collide()

        if maxim.check_for_collisions(exit):
            return

        camera.center = (maxim.x + 16, maxim.y)
        screen.fill("#080800")
        game_map.draw_background(screen, camera, 0)
        maxim.draw(screen, camera)  
        game_map.draw_foreground(screen, camera, 0)

        for wall in walls:
            wall.draw(screen, camera)

        pygame.display.flip()

        # limit framerate to 60 FPS
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()



# Next: Put a jelly into the room. Touching it also closes the game.
# Then figure out how a jelly moves in the original game and replicate it.