from projectile import Projectile
from monster import Monster
import pygame
import math
from game import Game      
pygame.init()

#charger l'image
pygame.display.set_caption("Comet Fall Game")
(largeur, hauteur) = (1080, 700)
screen = pygame.display.set_mode((largeur, hauteur))

background = pygame.image.load('assets/bg.jpg')

#importer puis charger notre bannière
banner = pygame.image.load('assets/banner.png')
banner = pygame.transform.scale(banner, (500, 500)) #  # taille de la bannière
banner_rect = banner.get_rect()
banner_rect.x = math.ceil(screen.get_width() / 4) 

#  importer notre bouton pour charger notre bouton
play_button = pygame.image.load('assets/button.png')
play_button = pygame.transform.scale(play_button, (400, 150)) # taille du bouton
play_button_rect = play_button.get_rect()
play_button_rect.x = math.ceil(screen.get_width() / 3.33) 
play_button_rect.y = math.ceil(screen.get_height() / 2) 


#charger notre jeu
game = Game()

running = True;

#tant que l'objectif n'est pas atteint
while running:
    # appliquer l'image de fond
    screen.blit(background, (0, -200))
    
    #vérifier si notre jeu à commencé ou non
    if game.is_playing:
        #déclencher les instructions de la partie
        game.update(screen)
        #vérifier si notre jeu n' pas commencé 
    else:
        #ajouter mon écran de bienvenue
        screen.blit(play_button, play_button_rect)
        screen.blit(banner, banner_rect)
        
    # mettre à jour l'image
    pygame.display.flip()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            #savoir si une touche reste appuyer
            game.pressed[event.key] = True
            #détecter si la touche espace t enchlenchée pour lancer notre projectile
            if event.key == pygame.K_SPACE:
                game.player.launch_projectile()
        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
        # vérification pour savoir si le button est cliquer par la souris
            if play_button_rect.collidepoint(event.pos):
            # mettre le jeu en mode "lancé"
                game.start()
            






            # if event.key == pygame.K_d:
            #        game.player.move_right()
            # if event.key == pygame.K_q:
            #     game.player.move_left()   