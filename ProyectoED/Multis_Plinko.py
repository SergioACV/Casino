from typing import Any
from Settings_Plinko import *

import pygame, pygame.gfxdraw

# Sprite for multipliers beneath obtacles
multi_group = pygame.sprite.Group()
clock = pygame.time.Clock()
delta_time = clock.tick(FPS) / 1000.0

class Multi(pygame.sprite.Sprite):
    def __init__(self, pos, color, multi_amt):
        super().__init__()
        self.display_sufarce = pygame.display.get_surface()
        self.font = pygame.font.SysFont(None, 26)
        self.color = color
        self.border_radius = 10
        self.position = pos
        self.rect_width, self.rect_height = OBSTACLE_P-(OBSTACLE_P/14), MULTI_HEIGTH
        self.image = pygame.Surface((self.rect_width, self.rect_height), pygame.SRCALPHA)
        pygame.draw.rect(self.image, self.color, self.image.get_rect(), border_radius = self.border_radius)
        self.rect = self.image.get_rect(center=self.position)
        self.multi_amt = multi_amt
        self.prev_multi = int(WIDTH/21.3)

        # Animation stuff, framerate independent
        self.animated_frame = 0
        self.animation_frame = int(0.25/delta_time)
        self.is_animating = False

        # Draw multiplier amount on rectangle
        self.render_multi()

    def animate(self, color, amount):
        if self.animated_frame < self.animation_frame // 2:
            self.rect.bottom += 2
        else:
            self.rect.bottom -= 2
        self.animated_frame += 1
        if self.animated_frame == (self.animation_frame // 2) * 2:
            self.is_animating = False
            self.animated_frame = 0

    def render_multi(self):
        text_surface = self.font.render(f"{self.multi_amt}x", True, [0, 0, 0])
        text_rect = text_surface.get_rect(center=self.image.get_rect().center)
        self.image.blit(text_surface, text_rect)

    def hit_sound(self): 
        if str(self.multi_amt) == "0":
            sound04.play()
        elif str(self.multi_amt) == "2":
            sound03.play()
        elif str(self.multi_amt) == "10":
            sound03.play()
        elif str(self.multi_amt) == "50":
            sound03.play()
        elif str(self.multi_amt) == "100":
            sound03.play()
        elif str(self.multi_amt) == "200":
            sound03.play()
        elif str(self.multi_amt) == "500":
            sound02.play()
        elif str(self.multi_amt) == "1000":
            sound01.play()

    def incress_credits(self):
        if str(self.multi_amt) == "0":
            return -1000
        elif str(self.multi_amt) == "2":
            return 1000 * 2
        elif str(self.multi_amt) == "10":
            return 1000 * 10
        elif str(self.multi_amt) == "50":
            return 1000 * 50
        elif str(self.multi_amt) == "100":
            return 1000 * 100
        elif str(self.multi_amt) == "200":
            return 1000 * 200
        elif str(self.multi_amt) == "500":
            return 1000 * 500
        elif str(self.multi_amt) == "1000":
            return 1000 * 1000

    def update(self):
        if self.is_animating:
            self.animate(self.color, self.multi_amt)

# Class for previous multi won
class PrevMulti(pygame.sprite.Sprite):
    def __init__(self, multi_amt, rgb_capture):
        super().__init__()
        self.display_surface = pygame.display.get_surface()

        self.multi_amt = multi_amt
        self.font = pygame.font.SysFont(None, 36)
        self.rect_width = SCORE_RECT
        self.rect_height = SCORE_RECT
        self.prev_surf = pygame.Surface((self.rect_width, self.rect_height), pygame.SRCALPHA)
        self.rgb = rgb_capture
        pygame.draw.rect(self.prev_surf, self.rgb, (0, 0, self.rect_width, self.rect_height))
        self.prev_rect = self.prev_surf.get_rect(midbottom=(int(WIDTH * 0.85), (HEIGTH/2)-(SCORE_RECT*2)))
        #self.creditos = Creditos()

        # Animation
        self.y_traverse = 0
        self.traveled = 0
        
        self.render_multi()

    def render_multi(self):
        text_surface = self.font.render(f"{self.multi_amt}x", True, [0, 0, 0])
        text_rect = text_surface.get_rect(center=self.prev_surf.get_rect().center)
        self.prev_surf.blit(text_surface, text_rect)

    def update(self):
        if self.prev_rect.bottom > (HEIGTH-(SCORE_RECT*2)): #864 at 1080
            self.kill()
        else:
            if self.traveled < self.y_traverse:
                total_distance = SCORE_RECT
                distance_per_second = 1800
                distance_per_frame = distance_per_second * delta_time  # 28 at dt=0.016
                divisor = int(SCORE_RECT/distance_per_frame)
                distance_per_frame = SCORE_RECT/divisor
                self.prev_rect.bottom += int(distance_per_frame)
                self.traveled += int(distance_per_frame)
            self.display_surface.blit(self.prev_surf, self.prev_rect)

class PrevMultiGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        pass

    def update(self):
        super().update()
    
        # Maintain four previous multis at a maximum; animate
        if len(self) > 5:
            self.remove(self.sprites().pop(0))        
        if len(self) == 1:
            self.sprites()[0].y_traverse = SCORE_RECT
        elif len(self) == 2:
            self.sprites()[0].y_traverse, self.sprites()[1].y_traverse = SCORE_RECT * 2, SCORE_RECT
        elif len(self) == 3:
            self.sprites()[0].y_traverse, self.sprites()[1].y_traverse, self.sprites()[2].y_traverse = SCORE_RECT * 3, SCORE_RECT * 2, SCORE_RECT
        elif len(self) == 4:
            self.sprites()[0].y_traverse, self.sprites()[1].y_traverse, self.sprites()[2].y_traverse, self.sprites()[3].y_traverse = SCORE_RECT * 4, SCORE_RECT * 3, SCORE_RECT * 2, SCORE_RECT
        elif len(self) == 5:
            self.sprites()[0].y_traverse, self.sprites()[1].y_traverse, self.sprites()[2].y_traverse, self.sprites()[3].y_traverse, self.sprites()[4].y_traverse = SCORE_RECT * 5, SCORE_RECT * 4, SCORE_RECT * 3, SCORE_RECT * 2, SCORE_RECT

prev_multi_group = PrevMultiGroup()
