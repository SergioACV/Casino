from Multis_Plinko import *
from Obstacle_Plinko import *
from Settings_Plinko import *
from Tree_Plinko import *
from Balls_Plinko import *

import pygame, pymunk

class Board:
    def __init__(self, space):
        self.space = space
        self.display_surface = pygame.display.get_surface()

        # Obstacles
        self.curr_row_count = 3
        self.final_row_count = 18
        self.obstables_list = []
        self.obstable_sprites = pygame.sprite.Group()
        self.update_coords = OBSTACLE_S

        # Play button
        self.play_up = pygame.image.load("Items_Plinko/Button.png").convert_alpha()
        self.play_down = pygame.image.load("Items_Plinko/ButtonPress.png").convert_alpha()
        self.pressing_play = False
        self.play_orig_width = self.play_up.get_width()
        self.play_orig_height = self.play_up.get_height()

        # Scale the play image by 50%
        self.play_scaled_width = self.play_orig_width * 1.5
        self.play_scaled_height = self.play_orig_height * 1.5
        self.scaled_play_up = pygame.transform.scale(self.play_up, (self.play_scaled_width, self.play_scaled_height))
        self.scaled_play_down = pygame.transform.scale(self.play_down, (self.play_scaled_width, self.play_scaled_height))
        self.play_rect = self.scaled_play_up.get_rect(center=(WIDTH // 12, HEIGTH // 1.75))

        # Get second point for segmentA
        self.segmentA_2 = OBSTACLE_S

        while self.curr_row_count <= self.final_row_count:
            for i in range(self.curr_row_count):
                # Get first point for SegmentB
                if self.curr_row_count == 3 and self.update_coords[0] > OBSTACLE_S[0]+OBSTACLE_P:
                    self.segmentB_1 = self.update_coords
                # Get first point for SegmentA
                elif self.curr_row_count == self.final_row_count and i == 0:
                    self.segmentA_1 = self.update_coords
                # Get second point for segmentB
                elif self.curr_row_count == self.final_row_count and i == self.curr_row_count - 1:
                    self.segmentB_2 = self.update_coords
                self.obstables_list.append(self.spawn_obstacle(self.update_coords, self.space))
                self.update_coords = (int(self.update_coords[0]+OBSTACLE_P), self.update_coords[1])
            self.update_coords = (int(WIDTH-self.update_coords[0] + (0.5*OBSTACLE_P)), int(self.update_coords[1]+OBSTACLE_P))
            self.curr_row_count += 1
        self.multi_x, self.multi_y = self.update_coords[0]+OBSTACLE_P, self.update_coords[1]
        self.root = self.tree = to_binary_tree(self.obstables_list)    

        # Segment (boundaries on side of obstacles)
        self.spawn_segments(self.segmentA_1, self.segmentA_2, self.space)
        self.spawn_segments(self.segmentB_1, self.segmentB_2, self.space)

        # Segment at the top of obstacles
        self.spawn_segments((self.segmentA_2[0], 0), self.segmentA_2, self.space)
        self.spawn_segments(self.segmentB_1, (self.segmentB_2[0], 0), self.space)

        # Spawn multis
        self.spawn_multis()

    def draw_obstacle(self, obstacles):
        for obstacle in obstacles:
            pos_X, pos_Y = int(obstacle.body.position.x), int(obstacle.body.position.y)
            pygame.draw.circle(self.display_surface, OBSTACLE_C, (pos_X,pos_Y), OBSTACLE_R)

    # Used to give a border radius to previous multi display on right side
    def draw_prev_multi_mask(self):
        multi_mask_surface = pygame.Surface((WIDTH / 4, HEIGTH), pygame.SRCALPHA)
        multi_mask_surface.fill(BACKGROUND_C)
        right_side_of_board = (WIDTH / 16) * 13
        right_side_pad = right_side_of_board / 130
        mask_y = (HEIGTH / 4) + ((HEIGTH / 4) / 9)
        pygame.draw.rect(multi_mask_surface, (0, 0, 0, 0), (right_side_pad, mask_y, SCORE_RECT, SCORE_RECT * 4), border_radius=30)
        self.display_surface.blit(multi_mask_surface, (right_side_of_board, 0))

    def spawn_multis(self):
        self.multi_amounts = [val[1] for val in multipliers_c.keys()]
        self.rgb_values = [val for val in multipliers_c.values()]
        for i in range(NUM_MULTI):
            multi = Multi((self.multi_x, self.multi_y), self.rgb_values[i], self.multi_amounts[i])
            multi_group.add(multi)
            self.multi_x += OBSTACLE_P

    def spawn_obstacle(self, pos, space):
        body = pymunk.Body(body_type=pymunk.Body.STATIC)
        body.position = pos
        body.friction = 0.6
        shape = pymunk.Circle(body, OBSTACLE_R)
        shape.elasticity = 0.4
        shape.filter = pymunk.ShapeFilter(categories=OBSTACLE_CLASS, mask=OBSTACLE_MASK)
        self.space.add(body, shape)
        return shape
    
    def spawn_segments(self, pointA, pointB, space):
        segment_body = pymunk.Body(body_type =  pymunk.Body.STATIC)
        segment_shape = pymunk.Segment(segment_body, pointA, pointB, 5) #Radius = 5
        self.space.add(segment_body, segment_shape)

    def update(self):
        self.draw_obstacle(printLevelOrder(self.root))
        multi_group.draw(self.display_surface)
        multi_group.update()
        if len(list(prev_multi_group)) > 0:
            prev_multi_group.update()
        self.draw_prev_multi_mask()
        if self.pressing_play:
            self.display_surface.blit(self.scaled_play_down, (WIDTH//16, HEIGTH//2))
        else:
            self.display_surface.blit(self.scaled_play_up, (WIDTH//16, HEIGTH//2))

class Win:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()
        self.score_font = pygame.font.Font(None, 50)
    
    def update(self,x):
        self.text_score = self.score_font.render(f'Intentos restantes: {x}', True, [255,255,255])
        self.display_surface.blit(self.text_score, (10,10))

        
