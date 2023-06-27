from Multis_Plinko import *
from Obstacle_Plinko import *
from Settings_Plinko import *
from External_Plinko import *

import pygame, pymunk, random

class Ball(pygame.sprite.Sprite):
    def __init__(self, pos, space, board, delta_time):
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.space = space
        self.board = board
        self.delta_time = delta_time
        self.body = pymunk.Body(body_type=pymunk.Body.DYNAMIC)
        self.body.position = pos
        self.shape = pymunk.Circle(self.body, BALL_R)
        self.shape.elasticity = 1.5
        self.shape.density = 10000
        self.shape.mass = 5000
        self.shape.filter = pymunk.ShapeFilter(categories=BALL_CLASS, mask=BALL_MASK)
        self.space.add(self.body, self.shape)
        self.image = pygame.Surface((BALL_R*2, BALL_R*2), pygame.SRCALPHA)
        self.rect = self.image.get_rect(topleft=(self.body.position.x, self.body.position.y))
        
    def update(self):
        pos_x, pos_y = int(self.body.position.x), int(self.body.position.y)
        self.rect.centerx = pos_x
        self.rect.centery = pos_y

        for obstacle in self.board.obstable_sprites:
            if pygame.sprite.collide_rect(self, obstacle):
                obstacle_centerx, obstacle_centery = obstacle.rect_centerx, obstacle.rect_centery
                obstacle_pos = (obstacle_centerx, obstacle_centery)

                for animating_obstacle in animation_group:
                    if obstacle_pos == animating_obstacle.coords:
                        animating_obstacle.kill()

                obstacle_anim = AnimatedObstacle(obstacle_centerx, obstacle_centery, 16, (255, 255, 255), self.delta_time)
                animation_group.add(obstacle_anim)

        # Check where ball ends in multi
        for multi in multi_group:
            if pygame.sprite.collide_rect(self, multi):
                multi.hit_sound()
                multi.animate(multi.color, multi.multi_amt)
                multi.is_animating = True

                # Display previous multion right side
                prev_rgb = multi.color
                prev_multi = PrevMulti(str(multi.multi_amt),prev_rgb)
                prev_multi_group.add(prev_multi)
                self.kill()

        # Draw red ball
        pygame.draw.circle(self.display_surface, (255,51,153), (pos_x, pos_y), BALL_R)
    
