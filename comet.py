import pygame
import random

# créer une class pour gérer notre comète

class Comet(pygame.sprite.Sprite):
    
    def __init__(self, comet_event):
        super().__init__()
        # définir l'image de la comète
        self.image = pygame.image.load('assets/comet.png')
        self.rect = self.image.get_rect()
        self.velocity = random.randint(1, 3)
        self.rect.x = random.randint(20, 800)
        self.rect.y = -random.randint(20, 800)
        self.comet_event = comet_event

    def remove(self):
        self.comet_event.all_comets.remove(self)
        
        # vérifier si le nombre de comète est égale à 0
        if len(self.comet_event.all_comets) == 0:
            print("l'évènement est terminé")
            #remettre la barre à 0
            self.comet_event.reset_percent()
            # apparaitre les 2 1er monstres
            self.comet_event.game.spawn_monster()
            self.comet_event.game.spawn_monster()

    def fall(self):
        self.rect.y += self.velocity
        # ne tombe pas sur le sol
        if self.rect.y >= 500:
            print("Sol")
        # retirer la boule de feu
            self.remove()
        # vérifier si la boule de feu touche le joueur
        if self.comet_event.game.check_colision(
            self, self.comet_event.game.all_players
        ):
            print("joueur touché !")
            #retirer la boule de feu
            self.remove()
            
            # s'il n'y a plus de boule de feu
            if len(self.comet_event.all_comets) == 0:
                print("l'évènement est fini")
                # remettre la jauge au départ
                self.comet_event.reset_percent()
                self.comet_event.fall_mode = False
            
            # subir 20 pts de dégats au joueur
            self.comet_event.game.player.damage(20)