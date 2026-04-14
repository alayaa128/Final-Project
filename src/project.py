import pygame
import random

class Character():

    def __init__(self, pos=(960,950), size=30):
        self.pos = pos
        self.size = size
        self.color = pygame.Color(0, 255, 0)
        self.alpha = 255
    
    def draw(self, surface):
        pygame.draw.circle(surface, self.color, self.pos, self.size)

class Obstacle():

    def __init__(self, pos=(100,70), size=random.randint(30, 40), life=1000):
        self.pos = pos
        self.size = size
        self.color = pygame.Color(100, 0, 255)
        self.alpha = 255
    
    def draw(self, surface):
        pygame.draw.circle(surface, self.color, self.pos, self.size)

#class Obstacle_Rain():

def main():
    #initialize game
    pygame.init()
    pygame.display.set_caption("Dodge or Die!")
    resolution = (1920, 1080)
    screen = pygame.display.set_mode(resolution)
    obstacle = Obstacle()
    character = Character()
    running = True
    #create safe zone
    #game loop
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        black = pygame.Color(0, 0, 0)
        screen.fill(black)
        obstacle.draw(screen)
        character.draw(screen)
        pygame.display.flip()
    pygame.quit()
    #event loop
    #when character gets hit with obstacle
    #hurt sound effect
    #new event loop
    #When character hits safe zone
    #winner sound effect
    #display text
    #background music
    

if __name__ == "__main__":
    main()