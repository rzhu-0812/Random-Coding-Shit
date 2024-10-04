import pygame
import random
import sys


class SpaceAdventure:
  def __init__(self):
    pygame.init()

    self.WIDTH, self.HEIGHT = 800, 600
    self.FPS = 60
    self.WHITE = (255, 255, 255)
    self.BLACK = (0, 0, 0)

    self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
    pygame.display.set_caption("Space Adventure")

    self.asteroid_img = self.image("images/asteroid.png", (40, 40))
    self.spaceship_img = self.image("images/spaceship.png", (40, 50))
    self.health_img = self.image("images/health.png", (40, 40))
    self.lost_health_img = self.image("images/health_outline.png", (40, 40))
    self.shield_img = self.image("images/shield.png", (40, 40))
    self.shoot_img = self.image("images/shoot.png", (40, 40))
    self.bullet_img = self.image("images/bullet.png", (10, 30))

    self.font = pygame.font.Font(None, 36)

    self.health = 3
    self.game_over = False
    self.shield_active = False
    self.shield_activated = False
    self.shield_duration = 120
    self.shield_timer = 0
    self.shield_count = 0
    self.shoot_active = False
    self.shoot_duration = 300
    self.shoot_timer = 0

    self.spaceship_rect = self.spaceship_img.get_rect()
    self.spaceship_rect.center = (self.WIDTH // 2, self.HEIGHT - 50)


  def image(self, path, size = None):
    image = pygame.image.load(path)
    if size:
      image = pygame.transform.scale(image, size)
    return image

  
  def render_text(self, text, color, x, y):
    text = self.font.render(text, True, color)
    self.screen.blit(text, (x, y))

  
  def centered(self, text, color):
    text = self.font.render(text, True, color)
    text_rect = text.get_rect(center = (self.WIDTH // 2, self.HEIGHT // 2))
    self.screen.blit(text, text_rect)


  def hearts(self):
    for i in range(3):
      x = self.WIDTH - 40 - i * 40
      y = 10
      if i < self.health:
        self.screen.blit(self.health_img, (x, y))
      else:
        self.screen.blit(self.lost_health_img, (x, y))

    if self.health <= 0:
      self.game_over = True


  def shields(self):
    if self.shield_active and self.shield_count > 0:
      shield_rect = self.screen.blit(self.shield_img, (self.WIDTH - 120, 60))

      if self.shield_activated:
        bar = int((self.shield_timer / self.shield_duration) * 80)
        pygame.draw.rect(self.screen, self.WHITE, (self.WIDTH - 80, shield_rect.centery - 10, bar, 20))

        self.shield_timer -= 1
        
        if self.shield_timer <= 0:
          if self.shield_count == 0:
            self.shield_active = False
          self.shield_activated = False
          self.shield_count -= 1
          self.shield_timer = self.shield_duration

      else:
        self.render_text(f"{self.shield_count}", self.WHITE, self.WIDTH - 70, shield_rect.centery - 10)

  def shoots(self):
    if self.shoot_active:
      self.shoot_timer -= 1
      shoot_rect = self.screen.blit(self.shoot_img, (self.WIDTH - 120, 110))

      bar = int((self.shoot_timer / self.shoot_duration) * 80)
      pygame.draw.rect(self.screen, self.WHITE, (self.WIDTH - 80, shoot_rect.centery - 10, bar, 20))

      if self.shoot_timer <= 0:
        self.shoot_active = False
        self.shoot_timer = self.shoot_duration
  

def main():
  s = SpaceAdventure()
  level = 1
  score = 0
  spacebar = False
  clock = pygame.time.Clock()
  obstacles = []
  shields = []
  shoots = []
  bullets = []

  while not s.game_over:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and s.spaceship_rect.left > 0:
      s.spaceship_rect.x -= 5
    if keys[pygame.K_RIGHT] and s.spaceship_rect.right < s.WIDTH:
      s.spaceship_rect.x += 5
    if keys[pygame.K_UP] and s.spaceship_rect.top > 0:
      s.spaceship_rect.y -= 5
    if keys[pygame.K_DOWN] and s.spaceship_rect.bottom < s.HEIGHT:
      s.spaceship_rect.y += 5
    if s.shoot_active and keys[pygame.K_SPACE] and not spacebar:
      bullet = s.bullet_img.get_rect(center = (s.spaceship_rect.x + 20, s.spaceship_rect.y - 12))
      bullets.append(bullet)
      spacebar = True
    elif s.shoot_active and not keys[pygame.K_SPACE]:
      spacebar = False
    if (keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT]) and s.shield_active:
      s.shield_activated = True
    
    if random.randint(0, 100) < level * 2:
      asteroid = s.asteroid_img.get_rect(center = (random.randint(0, s.WIDTH), 0))
      obstacles.append(asteroid)

    if random.randint(0, 1000) == 0:
      shield = s.shield_img.get_rect(center = (random.randint(0, s.WIDTH), 0))
      shields.append(shield)

    if random.randint(0, 1000) == 0:
      shoot = s.shoot_img.get_rect(center = (random.randint(0, s.WIDTH), 0))
      shoots.append(shoot)

    for obstacle in obstacles:
      obstacle.y += 5

      if obstacle.colliderect(s.spaceship_rect):
        if not s.shield_activated:
          s.health -= 1
          if s.health > 0:
            obstacles.remove(obstacle)
        else:
          obstacles.remove(obstacle)
        
    for shield in shields:
      shield.y += 5
      
      if shield.colliderect(s.spaceship_rect):
        shields.remove(shield)
        s.shield_count += 1
        s.shield_active = True

    for shoot in shoots:
      shoot.y += 5

      if shoot.colliderect(s.spaceship_rect):
        shoots.remove(shoot)
        s.shoot_active = True
        s.shoot_timer = s.shoot_duration

    for bullet in bullets:
      bullet.y -= 5

      for obstacle in obstacles:
        if bullet.colliderect(obstacle):
          obstacles.remove(obstacle)
          bullets.remove(bullet)
    
    obstacles = [obstacle for obstacle in obstacles if obstacle.y < s.HEIGHT]
    shields = [shield for shield in shields if shield.y < s.HEIGHT]
    shoots = [shoot for shoot in shoots if shoot.y < s.HEIGHT]
    bullets = [bullet for bullet in bullets if bullet.y > -11]

    s.screen.fill(s.BLACK)
    s.screen.blit(s.spaceship_img, s.spaceship_rect)
  
    for obstacle in obstacles:
      s.screen.blit(s.asteroid_img, obstacle)
    for shield in shields:
      s.screen.blit(s.shield_img, shield)
    for shoot in shoots:
      s.screen.blit(s.shoot_img, shoot)
    for bullet in bullets:
      s.screen.blit(s.bullet_img, bullet)

    if score % 1000 == 0 and score != 0:
      level += 1

    score += 1

    text = s.font.render(f"Score {score}", True, s.WHITE)
    s.screen.blit(text, (5, 5))
    text = s.font.render(f"Level {level}", True, s.WHITE)
    s.screen.blit(text, (5, 30))
      
    s.hearts()
    s.shields()
    s.shoots()
    
    pygame.display.flip()
    clock.tick(s.FPS)  

  pygame.time.delay(500)
  s.screen.fill(s.BLACK)
  s.centered(f"Your final score is {score}", s.WHITE)
  pygame.display.flip()
  pygame.time.delay(5000)
  return False

if __name__ == "__main__":
  main()