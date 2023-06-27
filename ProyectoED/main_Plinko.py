from Settings_Plinko import *
from Board_Plinko import *
from Multis_Plinko import *
from Balls_Plinko import Ball
from External_Plinko import *

import ctypes, pygame, pymunk, sys, random

ctypes.windll.user32.SetProcessDPIAware()
class Plinko:
    def __init__(self):

        # General Setup
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGTH))
        pygame.display.set_caption(TITLE_STRING)
        self.clock = pygame.time.Clock()
        self.delta_time = 10000

        # Pymunk
        self.space = pymunk.Space()
        self.space.gravity = (0,1800)

        # Plinko Setup
        self.ball_group = pygame.sprite.Group()
        self.board = Board(self.space)

        # Debugging
        self.balls_played = 0

    def run(self):

        self.start_time = pygame.time.get_ticks()

        self.creditos = Creditos()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    # Get the position of the mouse click
                    mouse_pos = pygame.mouse.get_pos()

                    # Check if the mouse click position collides with the image rectangle
                    if self.board.play_rect.collidepoint(mouse_pos):
                        self.board.pressing_play = True
                    else:
                        self.board.pressing_play = False
                        
                # Spawn ball on left mouse button release
                elif event.type == pygame.MOUSEBUTTONUP and event.button == 1 and self.board.pressing_play:  #and self.creditos.creditos >= 1000
                    mouse_pos = pygame.mouse.get_pos()
                    self.creditos.creditos -= 1000
                    if self.board.play_rect.collidepoint(mouse_pos):
                        random_x = WIDTH//2 + random.choice([random.randint(-20,-1),random.randint(1,20)])
                        click.play()
                        self.ball = Ball((random_x,25), self.space, self.board, self.delta_time)
                        self.ball_group.add(self.ball)
                        self.board.pressing_play = False
                    else:
                        self.board.pressing_play = False

            self.screen.fill(BACKGROUND_C)

            self.delta_time = self.clock.tick(FPS)/1000

            self.space.step(self.delta_time)
            self.board.update()
            self.ball_group.update()

            pygame.display.update()
        
