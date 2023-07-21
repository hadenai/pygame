import pygame
import animation
from random import randint

# créer une class qui va gérer la notion de monstre sur le jeu
class Monster(animation.AnimateSprite):
    
    def __init__(self, game):
        super().__init__("mummy")
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 0.5
        self.rect = self.image.get_rect()
        self.rect.x = 1000 + randint(0, 300)
        self.rect.y = 540
        self.velocity = randint(1, 3)
    
    def damage(self, amount):
        # infliger les dégâts
        self.health -= amount
        
        # vérifiez si son nouveau nombre de points de vie est inférieur ou égale à 0
        if self.health <= 0:
        # réaparaître comme un nouveau monstre
            self.rect.x = 1000 + randint(0, 300)
            self.velocity = randint(1, 3)
            self.health = self.max_health
    
        # si la barre d'évènement est chargé à son maximun
        if self.game.comet_event.is_full_loaded():
            # retirer du jeu
            self.game.all_monsters.remove(self)
            
            # appel de la methode pour déclencher la pluie de comète
            self.game.comet_event.attempt_fall()

    def update_health_bar(self, surface):        
        # dessiner sa barre de vie surface color position(position x, y largeur)
        pygame.draw.rect(surface, (60, 63, 60), [self.rect.x + 10, self.rect.y - 20, self.max_health, 5])
        pygame.draw.rect(surface, (111, 210, 46), [self.rect.x + 10, self.rect.y - 20, self.health, 5])
        
    def forward(self):
        # le deplacement ne se fait que s'il n'y pas de colision avec un joueur
        if not self.game.check_colision(self, self.game.all_players):
            self.rect.x -= self.velocity
        # si le monstre entre en colision avec le joueur
        else:
        # infliger des dégats au joueur
            self.game.player.damage(self.attack)