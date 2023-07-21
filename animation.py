import pygame

# définir une class qui va s'occuper des animations

class AnimateSprite(pygame.sprite.Sprite):
    
    def __init__(self, sprite_name):
        super().__init__()
        self.image = pygame.image.load('assets/' + sprite_name + '.png')

# définir une fonction pour charger les images d'un sprite
def load_animation_images(sprite_name):
    #charger les 24 images de ce sprite dans le dossier correspondant
    images = []
    # récupérer le chemin du dossier pour ce sprite
    path = f"assets/{sprite_name}/{sprite_name}"
    
    #boucler sur chaque image dans se dossier
    for num in range(1, 24):
        image_path =f"{path}{num}.png"
        images.append(pygame.image.load(image_path))
    #renvoyer le contenu de la liste d'image
    return images

# définir un dict qui va contenir les images 