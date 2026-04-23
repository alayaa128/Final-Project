import pygame
import random

class Character():

    def __init__(self, pos=(960,950), size=30):
        self.pos = pos
        self.size = size
        self.color = pygame.Color(0, 255, 0)
        self.alpha = 255
        self.rect = pygame.Rect(pos[0], pos[1], 30, 30)

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
        self.speed = random.uniform(230, 400)
        self.rect = pygame.Rect(pos[0], pos[1], 40, 40)

    def update(self, dt):
        self.age += dt
        self.pos[1] += self.speed * dt
        self.rect.topleft = self.pos
        if self.age > self.life:
            self.dead = True
        self.alpha = 255 * (1 - (self.age / self.life))

    def draw(self, surface):
        if self.dead:
            return
        pygame.draw.circle(surface, self.color, self.pos, 50)

class Obstacle_Rain():

    def __init__(self, pos=None, size=None, life=1000, width=1920):
        self.pos = pos
        self.size = size
        self.life = life
        self.width = width
        self.obstacles = []
        self.timer = 0
        self.spawn_delay = 0.10

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
    pygame.init()
    dt = 0
    clock = pygame.time.Clock()
    pygame.display.set_caption("Dodge or Die!")
    width = 1920
    height = 1080
    resolution = (width, height)
    screen = pygame.display.set_mode(resolution)
    obstacle = Obstacle()
    rain = Obstacle_Rain()
    character = Character()
    og_pos = character.pos
    running = True
    game_font = pygame.font.SysFont('arial', 80)
    win_font = game_font.render('You Win!', True, 'white')
    lose_font = game_font.render('You Lose!', True, 'red')
    win_font_rect = win_font.get_rect()
    lose_font_rect = lose_font.get_rect()
    win_font_rect.center = (width//2, 300)
    lose_font_rect.center = (width//2, 400)
    
    game_over = False
    win = False
    
    while running:
        #background music
        dt = clock.tick(60) / 1000
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            #moving character with mouse
            if pygame.mouse.get_pressed()[0]:
                if event.type == pygame.MOUSEMOTION:
                    mouse_pos = pygame.mouse.get_pos()
                    character.pos = mouse_pos
                    character.rect.topleft = mouse_pos
            
        rain.update(dt)
        black = pygame.Color(0, 0, 0)
        screen.fill(black)
        safe = pygame.draw.rect(screen, (0, 220, 255), ((random.randint(500, 1300)) - 80, 0, 150, 90))
        character.draw(screen)
        rain.draw(screen)

        if not win and not game_over:
            if safe.colliderect(character.rect):
                win = True
        if win:
            #winner sound effect
            screen.blit(win_font, win_font_rect)
        if win:
            if obstacle.rect.colliderect(character.rect):
                game_over = False
        
        if not game_over and not win:
            for obstacle in rain.obstacles:
                if obstacle.rect.colliderect(character.rect):
                    game_over = True
        if game_over:
            screen.blit(lose_font, lose_font_rect)
            #hurt sound effect
        if game_over:
            if safe.colliderect(character.rect):
                win = False
        #backspace restart
        #for event in pygame.event.get():
            #if event.type == pygame.KEYDOWN:
                #if event.key == pygame.K_BACKSPACE:
                    #game_over = False
                   # win = False
                    #character.pos = og_pos
        
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()