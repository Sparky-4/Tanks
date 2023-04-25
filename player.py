import pygame

class Player:
  def __init__(self, xPos, yPos, width, height, color):
    self.color = color
    self.rect = pygame.Rect((xPos, yPos, width, height))

  def update(self, screen):
    key = pygame.key.get_pressed()
    if key[pygame.K_a] == True:
        self.rect.move_ip(-1, 0)
    elif key[pygame.K_d] == True:
        self.rect.move_ip(1, 0)
    if key[pygame.K_w] == True:
        self.rect.move_ip(0, -1)
    elif key[pygame.K_s] == True:
        self.rect.move_ip(0, 1)


    if(self.rect.x < 0):
        self.rect.x = 0
    if(self.rect.y < 0):
        self.rect.y = 0
    if(self.rect.x + self.rect.width > screen.get_width()):
        self.rect.x = screen.get_width() - self.rect.width
    if(self.rect.y + self.rect.height > screen.get_height()):
        self.rect.y = screen.get_height() - self.rect.height

  def render(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)


