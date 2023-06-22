import pygame
import os
class CasinoChip(pygame.sprite.Sprite):
    
    
    def __init__(self, denomination,pos):
        pygame.sprite.Sprite.__init__(self)
        self.denomination = denomination
        self.amount = 0
        self.cardImage = str(self.denomination) + "Chip.png"
        self.position = pos  
        self.rect = pygame.rect
        self.image = pygame.image
        self.image_load()
    
    def add_chips(self, amount):
        self.amount += amount

    def remove_chips(self, amount):
        if self.amount >= amount:
            self.amount -= amount
            return True
        else:
            print("No hay suficientes fichas de esa denominación.")
            return False

    def display(self):
        print(f"{self.amount} fichas de {self.denomination} denominación")
        
    
    def display2(self):
        
        return f"{self.amount} fichas \nde {self.denomination} denominación"
        

    def image_load(self):
        fullname = ("Graphics/Chips/"+ self.cardImage)

        try:
            self.image = pygame.image.load(fullname)
            self.rect = self.image.get_rect()
            self.rect.center = self.position
  
        except FileNotFoundError:
            print("could not find: "+fullname)
    
    def update_position(self,pos):
        self.position = pos
        self.rect.center = pos
            

