import pygame
import os
class Card(pygame.sprite.Sprite):
    
    
    def __init__(self, value, suit,pos):
        pygame.sprite.Sprite.__init__(self)
        self.value = value
        self.suit = suit
        self.cardImage = self.value + self.suit + ".png"
        self.position = pos  
        self.rect = pygame.rect
        self.image = pygame.image
        self.image_load()

    def image_load(self):
        fullname = ("Graphics/cards/"+ self.cardImage)

        
        try:
            self.image = pygame.image.load(fullname)
            self.rect = self.image.get_rect()
            
            
        except FileNotFoundError:
            print("could not find: "+fullname)
    
    def update_position(self,pos):
        self.position = pos
        self.rect.center = pos
            
        
    def show(self):
        print(f"{self.value} of {self.suit}")
