import pygame
from player import Player
from monster import Monster
from comet_event import CometFallEvent

# créer une seconde class qui représente le jeu


class Game:

    def __init__(self):
        # définir si notre jeu à commencer ou pas
        self.is_playing = False
        # générer notre joueur
        self.all_players = pygame.sprite.Group()
        self.player = Player(self)
        # génerer l'évènement
        self.comet_event = CometFallEvent(self)
        self.all_players.add(self.player)
        # groupe de monstre
        self.all_monsters = pygame.sprite.Group()
        self.pressed = {}

    def start(self):
        self.is_playing = True
        self.spawn_monster()
        self.spawn_monster()
        
    def game_over(self):
        #remettre le jeu à neuf, retirer les monstres, remettre le joueur à 100 pts de vie, jeu en attente
        #enlever les cometes, retstart la jauge de comete
        self.all_monsters = pygame.sprite.Group()
        self.comet_event.all_comets = pygame.sprite.Group()
        self.comet_event.reset_percent()
        self.player.health = self.player.max_health
        self.is_playing = False
        
    
    def update(self, screen):
        # appliquer l'image de mon joueur
        screen.blit(self.player.image, self.player.rect)

        # actualiser la barre de vie du joueur
        self.player.update_health_bar(screen)
        
        # actualiser la barre d'évènement du jeu
        self.comet_event.update_bar(screen)
        
        # récupérer les projectiles du joueur
        for projectile in self.player.all_projectiles:
            projectile.move()

        # récupérer les monstres du joueur
        for monster in self.all_monsters:
            monster.forward()
            monster.update_health_bar(screen)

        # récupérer les comètes de notre jeu
        for comet in self.comet_event.all_comets:
            comet.fall()
            
        # appliquer l'ensemble des images de mon groupe de projectiles
        self.player.all_projectiles.draw(screen)

        # apliquer l'ensemble des images de notre groupe de monstre
        self.all_monsters.draw(screen)
        
        # appliquer l'ensemble des images de mon groupe de comète
        self.comet_event.all_comets.draw(screen)
        
        # vérifier si le joueur veux aller à droite ou à gauche et vérifier s'il atteint les bord de l'écran
        # à droite la taille maximun de l'écran à gauche 0
        if self.pressed.get(pygame.K_d) and self.player.rect.x + self.player.rect.width < screen.get_width():
            self.player.move_right()
        elif self.pressed.get(pygame.K_q) and self.player.rect.x > 0:
            self.player.move_left()

    def spawn_monster(self):
        monster = Monster(self)
        self.all_monsters.add(monster)

    def check_colision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)
