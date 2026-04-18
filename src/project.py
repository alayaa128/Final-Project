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

    def __init__(self, pos=(0, 0), size=40, life=1000):
        self.pos = list(pos)
        self.size = size
        self.color = pygame.Color(100, 0, 255)
        self.alpha = 255
        self.life = life
        self.age = 0
        self.dead = False
        self.speed = random.uniform(150, 300)  

    def update(self, dt):
        self.age += dt
        self.pos[1] += self.speed * dt
        if self.age > self.life:
            self.dead = True
        self.alpha = 255 * (1 - (self.age / self.life))

    def draw(self, surface):
        if self.dead:
            return
        pygame.draw.circle(surface, self.color, self.pos, 40)

class Obstacle_Rain():

    def __init__(self, pos=None, size=None, life=1000, width=1920):
        self.pos = pos
        self.size = size
        self.life = life
        self.width = width
        self.obstacles = []
        self.timer = 0
        self.spawn_delay = 0.30

    def update(self, dt):
        self.timer += dt
        if self.timer >= self.spawn_delay:
            self.timer = 0
            x = random.randint(0, self.width)
            y = 0
            obstacle = Obstacle((x, y), self.size, self.life)
            self.obstacles.insert(0, obstacle)
        self._update_obstacles(dt)

    def _update_obstacles(self, dt):
        for obstacle in self.obstacles:
            obstacle.update(dt)
        for idx, obstacle in enumerate(self.obstacles):
            obstacle.update(dt)
            if obstacle.dead:
                del self.obstacles[idx]

    def draw(self, surface):
        for obstacle in self.obstacles:
            obstacle.draw(surface)

def main():
    #initialize game
    pygame.init()
    dt = 0
    clock = pygame.time.Clock()
    pygame.display.set_caption("Dodge or Die!")
    x = 1920
    y = 1080
    resolution = (x, y)
    screen = pygame.display.set_mode(resolution)
    rain = Obstacle_Rain()
    character = Character()
    running = True
    #create safe zone
    #game loop
    while running:
        
        dt = clock.tick(60) / 1000
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        rain.update(dt)
        black = pygame.Color(0, 0, 0)
        screen.fill(black)
        safe = pygame.draw.rect(screen, (0, 220, 255), (x//2 - 80, 0, 150, 90))
        character.draw(screen)
        rain.draw(screen)
        pygame.display.flip()
        #moving character with mouse
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            character.pos = mouse_pos
        if event.type == pygame.MOUSEBUTTONUP:
            mouse_pos = pygame.mouse.get_pos()

          #event loop
    #when character gets hit with obstacle
    #hurt sound effect
    #new event loop
    #When character hits safe zone
    #winner sound effect
    #display text
    #background music
    pygame.quit()
  
    

if __name__ == "__main__":
    main()