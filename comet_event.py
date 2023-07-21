import pygame
from comet import Comet

#créer ne classpour gérer cette évènement

class CometFallEvent:

# lors du chargement on va devoir créer un compteur

    def __init__(self, game):
        self.percent = 0 
        self.percent_speed = 20
        # définir un goup de sprite pour stocker nos comètes
        self.all_comets = pygame.sprite.Group()
        self.game = game
        self.fall_mode = False
        
    def add_pourcent(self):
        self.percent += self.percent_speed / 100
        
    def reset_percent(self):
        self.percent = 0
        
    def is_full_loaded(self):
        return self.percent >= 100
    
    def meteor_fall(self):
        # boucle pour les valeurs de 1 à 10
        for i in range(1, 10):
            # faire aparaître une 1ere boule de feu
            self.all_comets.add(Comet(self))
            
    
    def attempt_fall(self):
        # la jauge d'évènement est totalement chargé
        if self.is_full_loaded() and len(self.game.all_monsters) == 0:
            print("Pluie de comète !!")
            self.meteor_fall()
            self.fall_mode = True # activer l'évènement
        
    def update_bar(self, surface):
        # ajouter du pourcentage a la barre
        self.add_pourcent()
        
        # barre noire en arrière plan
        pygame.draw.rect(surface, (0, 0, 0), [
            0, # l'axe des x
            surface.get_height() -20, # l'axe des y
            surface.get_width(), # longueur de la fenêtre
            10 # largeur de la barre
        ])
        # barre rouge (jauge d'event)
        pygame.draw.rect(surface, (187, 11, 11), [
        0, # l'axe des x
        surface.get_height() -20, # l'axe des y
        (surface.get_width() / 100) * self.percent, # longueur de la fenêtre tu calcule un pourcent de la taille de l'écran
        10 # largeur de la barre
    ])
        

