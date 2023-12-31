# créer une 1er class qui représente le joueur
import pygame
from projectile import Projectile

class Player(pygame.sprite.Sprite):
    
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 10
        self.velocity = 5
        self.image = pygame.image.load('assets/player.png')
        self.rect = self.image.get_rect()
        self.rect.x = 400
        self.rect.y = 500
        self.all_projectiles = pygame.sprite.Group()
  
    def damage(self, amount):
      if self.health - amount > amount:
        self.health -= amount
      else:
      # si le joueur na plus assez de points de vie
        self.game.game_over()
           
        
    def move_right(self): 
        #vérifier si le joueur n'entre pas en colision avec un monstre
        if not self.game.check_colision(self, self.game.all_monsters):
            self.rect.x += self.velocity
        
    def move_left(self):
        self.rect.x -= self.velocity
        
    def launch_projectile(self):
        self.all_projectiles.add(Projectile(self))
        
    def update_health_bar(self, surface):   
    # axe x largeur axe y hauteur
    # dessiner sa barre de vie surface color position(position x, y largeur)
        pygame.draw.rect(surface, (60, 63, 60), [self.rect.x + 50, self.rect.y + 20, self.max_health, 7])
        pygame.draw.rect(surface, (111, 210, 46), [self.rect.x + 50, self.rect.y + 20, self.health, 7])
        