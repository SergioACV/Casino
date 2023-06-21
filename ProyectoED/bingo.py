import pygame
from moviepy.editor import *
from pygame.locals import *
from create_players import create_tables, add_tables
from class_queue import Queue
from config import *
from sets import *
from Button import Button


class Bingo():
    
    def __init__(self):
        
        pygame.init()

        self.screen = pygame.display.set_mode((1280, 720))
        pygame.display.set_caption("Bingo!")
        self.background_image = pygame.image.load("graphics/bg.jpg")
        self.background_image = pygame.transform.scale(self.background_image, (1280, 720))

        self.bingo_ticket = pygame.image.load("graphics/bingo_ticket.png")
        self.bingo_ticket = pygame.transform.scale(self.bingo_ticket, (344, 412))

        self.machine = pygame.image.load("graphics/machine.png").convert_alpha()
        self.machine = pygame.transform.scale(self.machine, (290, 280))

        pygame.mixer.music.load("audio/track2.mp3")
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(-1)

        self.winner_sound = pygame.mixer.Sound("audio/winner.mp3")
        self.looser_sound = pygame.mixer.Sound("audio/looser.mp3")
        self.pop_sound = pygame.mixer.Sound("audio/pop.mp3")


        self.font = pygame.font.Font('graphics/font/04B_30__.TTF', 24)

    def render_grid(self,dictionary, number_list=[]):

        grid_x = 170 
        grid_y = 220  

        for y in range(grid_height):
            for x in range(grid_width):
                cell_rect = pygame.Rect(
                    grid_x + x * cell_size, grid_y + y * cell_size, cell_size, cell_size
                )
                pygame.draw.rect(self.screen, (0, 0, 0), cell_rect, 2)

                key = y * grid_width + x
                key_text = f"{dictionary.get(key, '')}"
                text_surface = self.font.render(str(key_text), True, (0, 0, 0))
                text_rect = text_surface.get_rect(center=cell_rect.center)
                self.screen.blit(text_surface, text_rect)

                if int(key_text) in number_list:
                    radius = 10
                    center_x = cell_rect.centerx
                    center_y = cell_rect.centery
                    height = 20  
                    width = 40  
                    octagon_points = [
                        (center_x + width // 2, center_y - height // 2),
                        (center_x + width // 2, center_y + height // 2),
                        (center_x + width // 4, center_y + height // 2 + radius),
                        (center_x - width // 4, center_y + height // 2 + radius),
                        (center_x - width // 2, center_y + height // 2),
                        (center_x - width // 2, center_y - height // 2),
                        (center_x - width // 4, center_y - height // 2 - radius),
                        (center_x + width // 4, center_y - height // 2 - radius)
                    ]
                    pygame.draw.polygon(self.screen, (255, 0, 0), octagon_points)

    def players_name(self,player_index):

        if player_index == 0:
            text='MY BINGO!!!'
        else:
            text = f"BINGO PLAYER {player_index + 1}"
        text_surface = self.font.render(text, True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=(300, 94))
        self.screen.blit(text_surface, text_rect)

    def buttons(self,activate):
        if activate == False:

            button_rect = pygame.Rect(
                1100,350,button_width,button_height
            )
            pygame.draw.rect(self.screen, (0, 255, 0), button_rect)
            next_text = self.font.render("PLAY", True, (255, 255, 255))
            next_text_rect = next_text.get_rect(center=button_rect.center)
            self.screen.blit(next_text, next_text_rect)
            return

        button_rect = pygame.Rect(
            400,600,button_width,button_height
        )
        pygame.draw.rect(self.screen, (0, 255, 0), button_rect)
        next_text = self.font.render("NEXT", True, (255, 255, 255))
        next_text_rect = next_text.get_rect(center=button_rect.center)
        self.screen.blit(next_text, next_text_rect)

        button_rect = pygame.Rect(
            200,600,button_width,button_height
        )
        pygame.draw.rect(self.screen, (0, 0, 0), button_rect)
        next_text = self.font.render("BALL", True, (255, 255, 255))
        next_text_rect = next_text.get_rect(center=button_rect.center)
        self.screen.blit(next_text, next_text_rect)

        

    def render_ball(self,number_ball):

        ball_radius = 80
        ball_color = (255, 255, 255)
        text_color = (0, 0, 0)

        ball_font = pygame.font.Font('graphics/font/04B_30__.TTF', 40)
        circle= pygame.draw.circle(self.screen, ball_color, (760,300), ball_radius)
        text_surface = ball_font.render(str(number_ball), True, text_color)
        text_rect = text_surface.get_rect(center=circle.center)
        self.screen.blit(text_surface, text_rect)

    def render_winner(self,index):
        winner_font = pygame.font.Font('graphics/font/04B_30__.TTF', 40)
        if index == 0:
            text='YOU ARE THE WINNEEEER!!!'
        else:
            text = f"PLAYER #{index + 1} IS THE WINNER :("
        text_surface = winner_font.render(text, True, (219, 172, 52))
        text_rect = text_surface.get_rect(center=(550, 600))
        self.screen.blit(text_surface, text_rect)

    def add_buttons(self):

        button_rect = pygame.Rect(
            1100,200,button_width,button_height
        )
        pygame.draw.rect(self.screen, (0, 255, 0), button_rect)
        next_text = self.font.render("+", True, (255, 255, 255))
        next_text_rect = next_text.get_rect(center=button_rect.center)
        self.screen.blit(next_text, next_text_rect)

    def main(self):
        current_dict_index = 0
        start = False
        ball = None
        winner = None
        running = True
        balls_out = []

        dictionary_list,random_numbers = create_tables()
        bingo_numbers = Queue(random_numbers)
        new_list = create_list(dictionary_list)
        
        #Boton
        QUIT_BUTTON = Button(image=pygame.image.load("Graphics/TinyBt.png"), pos=(1150, 150), 
                            text_input="QUIT", font=pygame.font.Font("Font/font.ttf", 10), base_color="#d7fcd4", hovering_color="White")

        while running:
            MENU_MOUSE_POS = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False
                elif event.type == MOUSEBUTTONDOWN:
                    
                    if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                        pygame.mixer.music.set_volume(0)
                        running = False
                        return
                    
                    mouse_pos = pygame.mouse.get_pos()
                    if (
                        1100<= mouse_pos[0]<= 1200
                        and 200 <= mouse_pos[1]<= 250 and start == True and ball == None
                    ):
                        dictionary_list.append(add_tables())
                        new_list = create_list(dictionary_list)

                    if (
                        1100<= mouse_pos[0]<= 1200
                        and 350 <= mouse_pos[1]<= 400 and start == False
                        and winner != None
                    ):
                        self.main()
                    if (
                        1100<= mouse_pos[0]<= 1200
                        and 350 <= mouse_pos[1]<= 400 and start == False
                    ):
                        start = True
                    if (
                        400<= mouse_pos[0]<= 500
                        and 600 <= mouse_pos[1]<= 650
                    ):
                        current_dict_index = (current_dict_index + 1) % len(dictionary_list)
                    if (
                        200<= mouse_pos[0]<= 300
                        and 600 <= mouse_pos[1]<= 650
                        and winner == None
                    ):
                        self.pop_sound.play()
                        if bingo_numbers.size != 0:
                            ball = bingo_numbers.dequeue()
                            balls_out.append(ball)
                        if bingo_numbers.size <=25:
                            winner = check_set(new_list, balls_out)
                        if winner == 0:
                            self.winner_sound.play()
                        if winner != 0 and winner != None:
                            self.looser_sound.play()
                

            self.screen.blit(self.background_image, (0, 0))
            self.buttons(start)
            
            
            for button in [QUIT_BUTTON]:
                button.changeColor(MENU_MOUSE_POS)
                button.update(self.screen)

            if start is True:
                self.screen.blit(self.bingo_ticket, (170, 150))
                self.render_grid(dictionary_list[current_dict_index],balls_out)
                self.players_name(current_dict_index)
                self.screen.blit(self.machine,(620,400))

            if ball != None:
                self.render_ball(ball)
            elif start is True:
                self.add_buttons()
            if winner != None :
                start = False
                ball = None
                self.screen.blit(self.bingo_ticket, (170, 150))
                self.render_winner(winner)
                self.render_grid(dictionary_list[winner],balls_out)
                self.players_name(winner)


            pygame.display.flip()

        pygame.quit()
    


