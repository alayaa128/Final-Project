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

def hit_obstacle(rain, character, lives, hit):
    for obstacle in rain.obstacles:
        if obstacle.rect.colliderect(character.rect):
                hit += 1
                lives -= 1
                rain.obstacles.remove(obstacle)

    if lives < 0:
        lives = 0
    return lives, hit

def is_game_over(hit, win):
    if win:
        return False
    return hit >= 3

def is_win(safe, character):
    if safe.colliderect(character.rect):
        return True

def sound_effects(win, game_over, hit):
     # plays sounds when the character gets hit, game over, wins
    win_sound = pygame.mixer.Sound('win sound 3.mp3')
    game_over_sound = pygame.mixer.Sound('game over.mp3')
    hit_sound = pygame.mixer.Sound('hit sound.mp3')
    #background_music = pygame.mixer.Sound('background music.mp3')
    played_game_over_sound = False
    played_win_sound = False

    if win and not played_win_sound:
        win_sound.play()
        played_win_sound = True

    if hit:
        hit_sound.play()

    if game_over and not played_game_over_sound:
        game_over_sound.play()
        played_game_over_sound = True

def display_text(win, game_over, screen, lives):
    #displays text onto the screen
    game_font = pygame.font.SysFont('arial', 80)
    lives_font = pygame.font.SysFont('arial', 50)
    live_font = lives_font.render(f"Lives: {lives}", True, 'yellow')
    win_font = game_font.render('You Win!', True, 'white')
    lose_font = game_font.render('GAME OVER!', True, 'red')
    live_font_rect = live_font.get_rect()
    win_font_rect = win_font.get_rect()
    lose_font_rect = lose_font.get_rect()
    live_font_rect.center = (1700, 80)
    win_font_rect.center = (1920//2, 300)
    lose_font_rect.center = (1920//2, 400)
    

    if win:
        screen.blit(win_font, win_font_rect)

   
    lives_font = lives_font.render(f"Lives: {lives}", True, 'yellow')
    screen.blit(lives_font, live_font_rect)
    
    if game_over:
        screen.blit(lose_font, lose_font_rect)

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
    hit = 0
    lives = 3
    game_over = False
    win = False
    running = True
    while running:
        dt = clock.tick(60) / 1000
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        keys = pygame.key.get_pressed()
        character.update_pos(keys, dt)
        rain.update(dt)
        black = pygame.Color(0, 0, 0)
        screen.fill(black)
        safe = pygame.draw.rect(screen, (0, 220, 255), (1920//2 - 80, 0, 150, 90))
        character.draw(screen)
        rain.draw(screen)
        if not game_over:
            if is_win(safe, character):
                win = True
        game_over = is_game_over(hit, win)
        if game_over:
            win = False
        if not game_over and not win:
            lives, hit = hit_obstacle(rain, character, lives, hit)
        display_text(win, game_over, screen, lives)
        sound_effects
        pygame.display.flip()
    pygame.quit()
if __name__ == "__main__":
    main()