import pygame
from moviepy.editor import *
from pygame.locals import *
from create_players import create_tables, add_tables
from class_queue import Queue
from config import *
from sets import *

pygame.init()

screen = pygame.display.set_mode((1200, 800))
pygame.display.set_caption("Bingo!")
background_image = pygame.image.load("graphics/bg.jpg")
background_image = pygame.transform.scale(background_image, (1200, 800))

bingo_ticket = pygame.image.load("graphics/bingo_ticket.png")
bingo_ticket = pygame.transform.scale(bingo_ticket, (344, 412))

machine = pygame.image.load("graphics/machine.png").convert_alpha()
machine = pygame.transform.scale(machine, (290, 280))

pygame.mixer.music.load("audio/track.mp3")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)

winner_sound = pygame.mixer.Sound("audio/winner.mp3")
looser_sound = pygame.mixer.Sound("audio/looser.mp3")
pop_sound = pygame.mixer.Sound("audio/pop.mp3")


font = pygame.font.Font('graphics/font/04B_30__.TTF', 24)

def render_grid(dictionary, number_list=[]):

    grid_x = 770 
    grid_y = 350  

    for y in range(grid_height):
        for x in range(grid_width):
            cell_rect = pygame.Rect(
                grid_x + x * cell_size, grid_y + y * cell_size, cell_size, cell_size
            )
            pygame.draw.rect(screen, (0, 0, 0), cell_rect, 2)

            key = y * grid_width + x
            key_text = f"{dictionary.get(key, '')}"
            text_surface = font.render(str(key_text), True, (0, 0, 0))
            text_rect = text_surface.get_rect(center=cell_rect.center)
            screen.blit(text_surface, text_rect)

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
                pygame.draw.polygon(screen, (255, 0, 0), octagon_points)

def players_name(player_index):

    if player_index == 0:
        text='MY BINGO!!!'
    else:
        text = f"BINGO PLAYER {player_index + 1}"
    text_surface = font.render(text, True, (255, 255, 255))
    text_rect = text_surface.get_rect(center=(940, 320))
    screen.blit(text_surface, text_rect)

def buttons(activate):
    if activate == False:

        button_rect = pygame.Rect(
            1100/2,800/2,button_width,button_height
        )
        pygame.draw.rect(screen, (0, 255, 0), button_rect)
        next_text = font.render("PLAY", True, (255, 255, 255))
        next_text_rect = next_text.get_rect(center=button_rect.center)
        screen.blit(next_text, next_text_rect)
        return

    button_rect = pygame.Rect(
        1000,700,button_width,button_height
    )
    pygame.draw.rect(screen, (0, 255, 0), button_rect)
    next_text = font.render("NEXT", True, (255, 255, 255))
    next_text_rect = next_text.get_rect(center=button_rect.center)
    screen.blit(next_text, next_text_rect)

    button_rect = pygame.Rect(
        800,700,button_width,button_height
    )
    pygame.draw.rect(screen, (0, 0, 0), button_rect)
    next_text = font.render("BALL", True, (255, 255, 255))
    next_text_rect = next_text.get_rect(center=button_rect.center)
    screen.blit(next_text, next_text_rect)

    

def render_ball(number_ball):

    ball_radius = 100
    ball_color = (255, 255, 255)
    text_color = (0, 0, 0)

    ball_font = pygame.font.Font('graphics/font/04B_30__.TTF', 40)
    circle= pygame.draw.circle(screen, ball_color, (600,400), ball_radius)
    text_surface = ball_font.render(str(number_ball), True, text_color)
    text_rect = text_surface.get_rect(center=circle.center)
    screen.blit(text_surface, text_rect)

def render_winner(index):
    winner_font = pygame.font.Font('graphics/font/04B_30__.TTF', 40)
    if index == 0:
        text='YOU ARE THE WINNEEEER!!!'
    else:
        text = f"PLAYER #{index + 1} IS THE WINNER :("
    text_surface = winner_font.render(text, True, (219, 172, 52))
    text_rect = text_surface.get_rect(center=(550, 250))
    screen.blit(text_surface, text_rect)

def add_buttons():

    button_rect = pygame.Rect(
        600,400,button_width,button_height
    )
    pygame.draw.rect(screen, (0, 255, 0), button_rect)
    next_text = font.render("+", True, (255, 255, 255))
    next_text_rect = next_text.get_rect(center=button_rect.center)
    screen.blit(next_text, next_text_rect)

    # button_rect = pygame.Rect(
    #     450,400,button_width,button_height
    # )
    # pygame.draw.rect(screen, (0, 255, 0), button_rect)
    # next_text = font.render("-", True, (255, 255, 255))
    # next_text_rect = next_text.get_rect(center=button_rect.center)
    # screen.blit(next_text, next_text_rect)



def main():
    current_dict_index = 0
    start = False
    ball = None
    winner = None
    running = True
    balls_out = []

    dictionary_list,random_numbers = create_tables()
    bingo_numbers = Queue(random_numbers)
    new_list = create_list(dictionary_list)

    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            elif event.type == MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if (
                    600<= mouse_pos[0]<= 700
                    and 400 <= mouse_pos[1]<= 450 and start == True and ball == None
                ):
                    dictionary_list.append(add_tables())
                    new_list = create_list(dictionary_list)
                # if (
                #     450<= mouse_pos[0]<= 550
                #     and 400 <= mouse_pos[1]<= 450 and start == True and ball == None
                #     and len(dictionary_list)>2
                # ):
                #     dictionary_list.pop()

                if (
                    550<= mouse_pos[0]<= 650
                    and 400 <= mouse_pos[1]<= 450 and start == False
                    and winner != None
                ):
                    main()
                if (
                    550<= mouse_pos[0]<= 650
                    and 400 <= mouse_pos[1]<= 450 and start == False
                ):
                    start = True
                if (
                    1000<= mouse_pos[0]<= 1100
                    and 700 <= mouse_pos[1]<= 750
                ):
                    current_dict_index = (current_dict_index + 1) % len(dictionary_list)
                if (
                    800<= mouse_pos[0]<= 900
                    and 700 <= mouse_pos[1]<= 750
                    and winner == None
                ):
                    pop_sound.play()
                    if bingo_numbers.size != 0:
                        ball = bingo_numbers.dequeue()
                        balls_out.append(ball)
                    if bingo_numbers.size <=25:
                        winner = check_set(new_list, balls_out)
                    if winner == 0:
                        winner_sound.play()
                    if winner != 0 and winner != None:
                        looser_sound.play()
             

        screen.blit(background_image, (0, 0))
        buttons(start)

        if start is True:
            screen.blit(bingo_ticket, (770, 280))
            render_grid(dictionary_list[current_dict_index],balls_out)
            players_name(current_dict_index)
            screen.blit(machine,(100,100))

        if ball != None:
            render_ball(ball)
        elif start is True:
            add_buttons()
        if winner != None :
            start = False
            ball = None
            screen.blit(bingo_ticket, (770, 280))
            render_winner(winner)
            render_grid(dictionary_list[winner],balls_out)
            players_name(winner)


        pygame.display.flip()

    pygame.quit()

main()