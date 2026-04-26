import pygame
import random

class Character():

    def __init__(self, pos=[960,950], size=30):
        self.pos = pos
        self.size = size
        self.color = pygame.Color(0, 255, 0)
        self.alpha = 255
        self.rect = pygame.Rect(pos[0], pos[1], 30, 30)

    def update_pos(self, keys, dt):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.pos[1] -= 300 * dt
            self.rect.topleft = self.pos
        if keys[pygame.K_DOWN]:
            self.pos[1] += 300 * dt
            self.rect.topleft = self.pos

        if keys[pygame.K_LEFT]:
            self.pos[0] -= 300 * dt
            self.rect.topleft = self.pos
        if keys[pygame.K_RIGHT]:
            self.pos[0] += 300 * dt
            self.rect.topleft = self.pos

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
        self.spawn_delay = 0.15

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
    lives = 3
    running = True
    game_font = pygame.font.SysFont('arial', 80)
    lives_font = pygame.font.SysFont('arial', 50)
    lives_font = lives_font.render(f"Lives: {lives}", True, 'yellow')
    win_font = game_font.render('You Win!', True, 'white')
    lose_font = game_font.render('GAME OVER!', True, 'red')
    lives_font_rect = lives_font.get_rect()
    win_font_rect = win_font.get_rect()
    lose_font_rect = lose_font.get_rect()
    lives_font_rect.center = (1700, 80)
    win_font_rect.center = (width//2, 300)
    lose_font_rect.center = (width//2, 400)
    
    win_sound = pygame.mixer.Sound('win sound 3.mp3')
    game_over_sound = pygame.mixer.Sound('game over.mp3')
    hit_sound = pygame.mixer.Sound('hit sound.mp3')
    #background_music = pygame.mixer.Sound('background music.mp3')
    played_game_over_sound = False
    played_win_sound = False
    game_over = False
    win = False
    hit = 0
    while running:
        #background_music.play()
        dt = clock.tick(60) / 1000
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            #moving chracter with arrow keys
        keys = pygame.key.get_pressed()
        character.update_pos(keys, dt)
        rain.update(dt)
        black = pygame.Color(0, 0, 0)
        screen.fill(black)
        safe = pygame.draw.rect(screen, (0, 220, 255), (width//2 - 80, 0, 150, 90))
        character.draw(screen)
        rain.draw(screen)
        screen.blit(lives_font, lives_font_rect)
        if not win and not game_over:
            if safe.colliderect(character.rect):
                win = True
        if win and not played_win_sound:
            win_sound.play()
            screen.blit(win_font, win_font_rect)
            played_win_sound = True
        if win and played_win_sound:
            screen.blit(win_font, win_font_rect)
        if win:
            if obstacle.rect.colliderect(character.rect):
                game_over = False
        if not game_over and not win:
            for obstacle in rain.obstacles:
                if obstacle.rect.colliderect(character.rect):
                    hit += 1
                    lives -= 1
                    hit_sound.play()
                    rain.obstacles.remove(obstacle)
        lives_font = pygame.font.SysFont('arial', 60)
        lives_font = lives_font.render(f"Lives: {lives}", True, 'yellow')
        screen.blit(lives_font, lives_font_rect)
        if hit == 3:
            game_over = True
        if game_over and not played_game_over_sound:
            screen.blit(lose_font, lose_font_rect)
            game_over_sound.play()
            played_game_over_sound = True
        if game_over and played_game_over_sound:
            screen.blit(lose_font, lose_font_rect)
        if game_over:
            if safe.colliderect(character.rect):
                win = False
        pygame.display.flip()
    pygame.quit()
if __name__ == "__main__":
    main()