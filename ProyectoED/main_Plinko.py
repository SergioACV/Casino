from Settings_Plinko import *
from Board_Plinko import *
from Multis_Plinko import *
from Balls_Plinko import Ball
from Button import Button

import ctypes, pygame, pymunk, sys, random

ctypes.windll.user32.SetProcessDPIAware()
class Game:
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
        self.score = Win()

        # Debugging
        self.balls_played = 0


    def run(self):
        self.start_time = pygame.time.get_ticks()

        self.intento = 10

        #Boton
        QUIT_BUTTON = Button(image=pygame.image.load("Graphics/TinyBt.png"), pos=(1150, 150), 
                            text_input="QUIT", font=pygame.font.Font("Font/font.ttf", 10), base_color="#d7fcd4", hovering_color="White")
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    # Get the position of the mouse click
                    mouse_pos = pygame.mouse.get_pos()
                    
                    if QUIT_BUTTON.checkForInput(mouse_pos):
                        return True

                    # Check if the mouse click position collides with the image rectangle
                    if self.board.play_rect.collidepoint(mouse_pos):
                        self.board.pressing_play = True
                    else:
                        self.board.pressing_play = False
                        
                # Spawn ball on left mouse button release
                elif event.type == pygame.MOUSEBUTTONUP and event.button == 1 and self.board.pressing_play and self.intento > 0:
                    mouse_pos = pygame.mouse.get_pos()
                    self.intento -= 1
                    if self.board.play_rect.collidepoint(mouse_pos):
                        random_x = WIDTH//2 + random.choice([random.randint(-20,-1),random.randint(1,20)])
                        click.play()
                        self.ball = Ball((random_x,25), self.space, self.board, self.delta_time)
                        self.ball_group.add(self.ball)
                        self.board.pressing_play = False
                    else:
                        self.board.pressing_play = False
            

            self.screen.fill(BACKGROUND_C)

            for button in [QUIT_BUTTON]:
                button.changeColor(mouse_pos)
                button.update(self.screen)

            self.delta_time = self.clock.tick(FPS)/1000

            self.space.step(self.delta_time)
            self.board.update()
            self.score.update(self.intento)
            self.ball_group.update()

            pygame.display.update()
        

if __name__ == '__main__':
    game = Game()
    game.run()
