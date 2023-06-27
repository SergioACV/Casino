
from Settings_Plinko import *

import pygame

class Creditos(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.creditos = 1000
        self.screen = pygame.display.get_surface()
        self.font = pygame.font.SysFont(None, 50)


    @property
    def creditos_x(self):
        return self.creditos.creditos_x
    
    @creditos_x.setter
    def creditos_x(self, val):
        self.creditos.creditos_x

    # Render actual credits
    def draw_actual_credits(self,amt):
        text_credits = self.font.render(f'Creditos: {amt}', True, [255,255,255])
        self.screen.blit(text_credits, (10,10))