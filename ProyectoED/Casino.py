import pygame
import pygame_gui
import sys
from Button import Button, hitButton, dealButton,standButton, betButton, RouletteButtonBets,SelectChipButton
import random
from Card import Card
from Player import Player, PlayerBlackjack,PlayerRoulette
from Deck import Deck
from Blackjack import Blackjack
from Roulette import Roulette
import os

#Tragamonedas

from maquina import Maquina
from settings import *
import ctypes, pygame, sys
from ctypes import windll, wintypes
from Tragamonedas import Tragamonedas

#loteria

from bingo import Bingo

import pygame
from moviepy.editor import *
from pygame.locals import *
from create_players import create_tables, add_tables
from class_queue import Queue
from config import *
from sets import *

#PLinko
from Settings_Plinko import *
from Board_Plinko import *
from Multis_Plinko import *
from Balls_Plinko import Ball
from External_Plinko import *
from main_Plinko import Plinko
import ctypes, pygame, pymunk, sys, random


# Inicializar Pygame
pygame.init()
ctypes.windll.user32.SetProcessDPIAware()
# Configuración de la ventana

window_width = 1280
window_height = 720
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Casino Game")

# Fuentes
font = pygame.font.SysFont(None, 24)
big_font = pygame.font.SysFont(None, 80)

# Cargar imagen de fondo
background_image = pygame.image.load("Graphics/VerdeBG.jpg")


# Ajustar tamaño de la imagen de fondo
background_image = pygame.transform.scale(background_image, (window_width, window_height))

# Variables de juego y de la GUI
clock = pygame.time.Clock()

#manager
manager = pygame_gui.UIManager((1280, 720))

# Colores
WHITE = (255, 255, 255)
GREEN = (0, 128, 0)
RED = (255, 0, 0)
BLACK =(0,0,0)


def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("Font/font.ttf", size)



def soundLoad(name):
    """ Same idea as the imageLoad function. """
    
    fullName = os.path.join('sounds', name)
    try: sound = pygame.mixer.Sound(fullName)
    except pygame.error.message:
        print ('Cannot load sound:', name)
        raise SystemExit.message
    return sound

def playClick():
    clickSound = soundLoad("click2.wav")
    clickSound.play()

def main_menu():
    
    is_running = True
    
    while is_running:
        
        MENU_MOUSE_POS = pygame.mouse.get_pos()
        window.fill((0,0,0))
        # Dibujar elementos en la ventana
        MENU_TEXT = get_font(100).render("CASINO", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))
        #botones para inciar los juegos
        
        BLACKJACK_BUTTON = Button(image=pygame.image.load("Graphics/GamesBG.png"), pos=(640, 200), 
                            text_input="BLACKJACK", font=get_font(40), base_color="#d7fcd4", hovering_color="White")
        TRAGAMONEDAS_BUTTON = Button(image=pygame.image.load("Graphics/GamesBG.png"), pos=(640, 300), 
                            text_input="TRAGAMONEDAS", font=get_font(35), base_color="#d7fcd4", hovering_color="White")
        ROULLETTE_BUTTON = Button(image=pygame.image.load("Graphics/GamesBG.png"), pos=(640, 400), 
                            text_input="ROULLETTE", font=get_font(40), base_color="#d7fcd4", hovering_color="White")
        LOTERIA_BUTTON = Button(image=pygame.image.load("Graphics/GamesBG.png"), pos=(640, 500), 
                            text_input="LOTERIA", font=get_font(40), base_color="#d7fcd4", hovering_color="White")
        PLINKO_BUTTON = Button(image=pygame.image.load("Graphics/GamesBG.png"), pos=(640, 600), 
                            text_input="PLINKO", font=get_font(40), base_color="#d7fcd4", hovering_color="White")
        
        
        #display
        window.blit(background_image, (0, 0))
        window.blit(MENU_TEXT,MENU_RECT)
        
        
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if BLACKJACK_BUTTON.checkForInput(MENU_MOUSE_POS):
                    playClick()
                    FullGameBlackjack()
                if TRAGAMONEDAS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    playClick()
                    FullTragamonedas()
                if ROULLETTE_BUTTON.checkForInput(MENU_MOUSE_POS):
                    playClick()
                    FullRoulette()
                if LOTERIA_BUTTON.checkForInput(MENU_MOUSE_POS):
                    playClick()
                    FullLoteria()
                if PLINKO_BUTTON.checkForInput(MENU_MOUSE_POS):
                    playClick()
                    FullPlinko()
                    
                    
                
    
        for button in [BLACKJACK_BUTTON, TRAGAMONEDAS_BUTTON, ROULLETTE_BUTTON,LOTERIA_BUTTON,PLINKO_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(window)

        # Actualizar la ventana
        pygame.display.update()
        # Controlar la velocidad de fotogramas
        clock.tick(60)
        
def FullPlinko():
    Game = Plinko()
    Game.run()
        
def FullLoteria():
    x = Bingo()
    x.main()
    
        
def FullTragamonedas():
    ctypes.windll.user32.SetProcessDPIAware()
    tragamonedas = Tragamonedas()
    Finish = False
    while True:
        Finish = tragamonedas.run()
        if (Finish):
            
            #windll.user32.SetThreadDpiAwarenessContext(wintypes.HANDLE(-1))
            ctypes.windll.shcore.SetProcessDpiAwareness(-1)
            pygame.display.set_mode((window_width, window_height))
            break
    

def FullRoulette():
    
    def PlayRoulette(Player):
        BG = pygame.image.load("Graphics/rouletteBG.jpg").convert_alpha()
        RouletteButtons = RouletteButtonBets()
        Player1 = Player
        Player1.chips = 0
        ruleta = Roulette()
        
        #Variableas a usar
        pressed = (False,False,False,False)
        Apuestas = {}
        spin = False
        
        
        #Buttons
        PLAYAGAIN_BUTTON = Button(image=pygame.image.load("Graphics/TinyBt.png"), pos=(1150, 150), 
                            text_input="PLAY AGAIN", font=get_font(10), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("Graphics/TinyBt.png"), pos=(1150, 200), 
                            text_input="QUIT", font=get_font(10), base_color="#d7fcd4", hovering_color="White")
        
        SPIN_BUTTON = Button(image=pygame.image.load("Graphics/TinyBt.png"), pos=(1150, 500), 
                            text_input="SPIN", font=get_font(20), base_color="#d7fcd4", hovering_color="White")
        
        CHIPS_BUTTON =  SelectChipButton(image1=pygame.image.load("Graphics/TinyBt10.jpg"), pos=(1150, 300), 
                                           image2=pygame.image.load("Graphics/TinyBt25.jpg"), pos2=(1150, 350),
                                           image3=pygame.image.load("Graphics/TinyBt50.jpg"), pos3=(1150, 400),
                                           image4=pygame.image.load("Graphics/TinyBt100.jpg"), pos4=(1150, 450),
                                           image1_1=pygame.image.load("Graphics/TinyBt10Grey.jpg"),
                                           image2_2=pygame.image.load("Graphics/TinyBt25Grey.jpg"),
                                           image3_3=pygame.image.load("Graphics/TinyBt50Grey.jpg"),
                                           image4_4=pygame.image.load("Graphics/TinyBt100Grey.jpg"))
        
        BUY_BUTTON = Button(image=pygame.image.load("Graphics/TinyBt.png"), pos=(1150, 684), 
                                text_input="BUY MORE CHIPS", font=get_font(10), base_color="#d7fcd4", hovering_color="White")
        
        #Sprite Groups
        
        DrawChips = pygame.sprite.Group()

        while True:
            MENU_MOUSE_POS = pygame.mouse.get_pos()
            
            window.fill((0,0,0))
            window.blit(BG, (0, 0))
            
            #Variables a usar
            Apuestas = RouletteButtons.stacks

            
            #Text
            fundsFont = pygame.font.Font.render(get_font(11), "Funds: $%.2f" %(Player1.funds), 1, (255,255,255), (0,0,0))
            window.blit(fundsFont, (1083,235))
            
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    print(MENU_MOUSE_POS)
                    if RouletteButtons.checkForInput(MENU_MOUSE_POS):
                        playClick()
                        if(spin == False):
                            Player1 = RouletteButtons.MakeActions(Player1,pressed,MENU_MOUSE_POS) 
                            
                            for clave, elementos in Apuestas.items():
                                
                                for elemento in elementos:
                                    DrawChips.add(elemento)
                                    
                            if pressed == (False,False,False,False) and len(Apuestas)!=0:
                                Player1,card =RouletteButtons.DeleteChipsInStack(Player1)
                                
                                if card != None:
                                    DrawChips.remove(card)
                            

                    if CHIPS_BUTTON.checkForInput(MENU_MOUSE_POS):
                        pressed = CHIPS_BUTTON.pressed
                        playClick()
                        
                    
                    if SPIN_BUTTON.checkForInput(MENU_MOUSE_POS):
                        playClick()
                        if(spin == False):
                            spin = True
                            number = ruleta.spin_wheel()
                            won = ruleta.resultsRoulette(Player1,Apuestas,number)
                            Player1.funds +=won
                        
                        
                        
                    if PLAYAGAIN_BUTTON.checkForInput(MENU_MOUSE_POS):
                        playClick()
                        print("PLAYING AGAIN: ROULETTE")
                        PlayRoulette(Player1)
                        
                    if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                        playClick()
                        main_menu()
                        
                    if BUY_BUTTON.checkForInput(MENU_MOUSE_POS):
                        playClick()
                        BuyYourChips(Player1)
                   
            
            for button in [PLAYAGAIN_BUTTON,QUIT_BUTTON,CHIPS_BUTTON,SPIN_BUTTON,BUY_BUTTON]:
                
                button.changeColor(MENU_MOUSE_POS)
                button.update(window)
            
            
            if(spin):
                COLOR = ruleta.wheel[number]
                if COLOR == "red":
                    COLOR = RED
                elif COLOR == "black":
                    COLOR = BLACK
                else:
                    COLOR = GREEN
                
                NUMBERWINNER= pygame.font.Font.render(get_font(40), str(number), 1, (255,255,255), COLOR)
                WON_TEXT = get_font(15).render(f"{Player1.name} wins {won}. Congratulations!", True, "#b68f40")
            
                window.blit(NUMBERWINNER,(515,106))
                window.blit(WON_TEXT,(300,231))
                
            #info about your chips
            
            if(len(Player1.Casinochips)!=0):
                y= 0
                for amount1 in Player1.Casinochips.values():
                    
                    fundsFont = pygame.font.Font.render(get_font(9), amount1.display2(), 1, (255,255,255), (0,0,0))
                    window.blit(fundsFont, (1070,550+y))
                    y+=30
                
            #Draw sprite groups
            if(len(Apuestas)!=0):
                DrawChips.update()
                DrawChips.draw(window)

            pygame.display.update()
            # Controlar la velocidad de fotogramas
            clock.tick(60)
    
    
    
    def BuyYourChips(Player):
        
        def BuyChips(Player,denomination,amount):
            if amount>0:
                total = amount*denomination
                if(total<= Player.funds):
                    
                    print("Compra realizada")
                    Player.add_chips(denomination,amount)
                    
                    print("Total Fund",Player.funds)
                    playClick()
                else:
                    print("Saldo insuficiente")
            else:
                
                print("Devolviendo saldo")
                
                Player.remove_chips(denomination,amount*-1)
                    
                
            return Player
                
            
        manager = pygame_gui.UIManager((1280, 720))
        Quantity10 = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((240, 146), (100, 50))
                                                            , manager=manager,object_id='#get_quantity10')
        Quantity25 = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((240, 346), (100, 50))
                                                            , manager=manager,object_id='#get_quantity25')
        Quantity50 = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((240, 546), (100, 50))
                                                            , manager=manager,object_id='#get_quantity50')
        Quantity100 = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((770, 146), (100, 50))
                                                            , manager=manager,object_id='#get_quantity100')
        
        Player1 = Player
        
        BG = pygame.image.load("Graphics/ShopBG.jpg")
        is_running = True
        while is_running:
            MENU_MOUSE_POS = pygame.mouse.get_pos()
            UI_REFRESH_RATE = clock.tick(60)/1000
            window.fill((0,0,0))
            window.blit(BG, (0, 0))
            
            #TEXTOS EN PANTALLA
            TITTLE_TEXT = get_font(20).render("Buy your chips ¡you will be millonaire!", True, "White")
            TITTLE_RECT = TITTLE_TEXT.get_rect(center=(420, 38))
            fundsFont = pygame.font.Font.render(get_font(11), "Funds: $%.2f" %(Player.funds), 1, (255,255,255), (0,0,0))
            
            
            #CARGAR IMAGENES
            
            Chip10 = pygame.image.load("Graphics/BIG10.png").convert_alpha()
            Chip25 = pygame.image.load("Graphics/BIG25.png").convert_alpha()
            Chip50 = pygame.image.load("Graphics/BIG50.png").convert_alpha()
            Chip100 = pygame.image.load("Graphics/BIG100.png").convert_alpha()
            
            #DISPLAY
            window.blit(TITTLE_TEXT,TITTLE_RECT)
            window.blit(Chip10,(76,106))
            window.blit(Chip25,(76,306))
            window.blit(Chip50,(76,506))
            window.blit(Chip100,(606,106))
            window.blit(fundsFont, (1074,205))
            
            #BOTON
            BACK_BUTTON = Button(image=pygame.image.load("Graphics/TinyBt.png"), pos=(1150, 654), 
                                text_input="BACK", font=get_font(10), base_color="#d7fcd4", hovering_color="White")
            
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    print(MENU_MOUSE_POS)
                if (event.type == pygame_gui.UI_TEXT_ENTRY_FINISHED and
                    event.ui_object_id == '#get_quantity10'):
                    quantity = int(event.text)
                    Player1 = BuyChips(Player,10,quantity)
                if (event.type == pygame_gui.UI_TEXT_ENTRY_FINISHED and
                    event.ui_object_id == '#get_quantity25'):
                    quantity = int(event.text)
                    Player1 = BuyChips(Player,25,quantity)
                    
                if (event.type == pygame_gui.UI_TEXT_ENTRY_FINISHED and
                    event.ui_object_id == '#get_quantity50'):
                    quantity = int(event.text)
                    Player1 = BuyChips(Player,50,quantity)
                    
                if (event.type == pygame_gui.UI_TEXT_ENTRY_FINISHED and
                    event.ui_object_id == '#get_quantity100'):
                    quantity = int(event.text)
                    Player1 = BuyChips(Player,100,quantity)
                    
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if BACK_BUTTON.checkForInput(MENU_MOUSE_POS):
                        is_running = False
                
                manager.process_events(event)
            
            manager.update(UI_REFRESH_RATE)
            manager.draw_ui(window)
            
            for button in [BACK_BUTTON]:
                button.changeColor(MENU_MOUSE_POS)
                button.update(window)
                
            #info about your chips
            
            if(len(Player1.Casinochips)!=0):
                
                y= 0
                for amount1 in Player1.Casinochips.values():
                    
                    fundsFont = pygame.font.Font.render(get_font(9), amount1.display2(), 1, (255,255,255), (0,0,0))
                    window.blit(fundsFont, (1070,250+y))
                    y+=30
            
            pygame.display.update()
            
            
        
        
    def GetFirstData():
        
        
        manager = pygame_gui.UIManager((1280, 720))
        PlayerName = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((432, 288), (500, 50))
                                                            , manager=manager,object_id='#get_name')
        
        name = ""
        bet = ""
        
        Player1 = PlayerRoulette("",500)
        
        #Botones
        #BOTON
        BACK_BUTTON = Button(image=pygame.image.load("Graphics/TinyBt.png"), pos=(1150, 30), 
                            text_input="BACK", font=get_font(10), base_color="#d7fcd4", hovering_color="White")
        is_running = True
        while is_running:
            MENU_MOUSE_POS = pygame.mouse.get_pos()
            UI_REFRESH_RATE = clock.tick(60)/1000
            window.fill((0,0,0))
            window.blit(background_image, (0, 0))
            
            #BOTON
            ENTER_BUTTON = Button(image=pygame.image.load("Graphics/TinyBt.png"), pos=(620, 654), 
                                text_input="SEND", font=get_font(10), base_color="#d7fcd4", hovering_color="White")
            
            #BOTON COMPRAR 
            BUY_BUTTON = Button(image=pygame.image.load("Graphics/TinyBt.png"), pos=(620, 450), 
                                text_input="BUY", font=get_font(20), base_color="#d7fcd4", hovering_color="White")
            
        
            
            
            #TEXTOS
            
            CHOOSE_TEXT = get_font(45).render("Make your bets", True, "White")
            CHOOSE_RECT = CHOOSE_TEXT.get_rect(center=(640, 200))
            
            BLACKJACK_TEXT = get_font(45).render("¡Welcome to the roulette!", True, "White")
            BLACKJACK_RECT = BLACKJACK_TEXT.get_rect(center=(640, 100))
            
            PLAYERNAME_TEXT = get_font(15).render("Player name:", True, "White")
            PLAYERNAME_RECT = CHOOSE_TEXT.get_rect(center=(555, 325))
            
            BET_TEXT = get_font(20).render("Buy your Casino chips here!!", True, "White")
            BET_RECT = CHOOSE_TEXT.get_rect(center=(555, 420))
            
            
            # Cargar la imagen
            casinoMan = pygame.image.load("Graphics/CasinoMan.png").convert_alpha()
            casinoMan2 = pygame.image.load("Graphics/CasinoMan2.png").convert_alpha()
            
            window.blit(BET_TEXT,BET_RECT)
            window.blit(BLACKJACK_TEXT, BLACKJACK_RECT)
            window.blit(PLAYERNAME_TEXT,PLAYERNAME_RECT)
            window.blit(CHOOSE_TEXT,CHOOSE_RECT)
            
            
            #variables a usar
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if (event.type == pygame_gui.UI_TEXT_ENTRY_FINISHED and
                    event.ui_object_id == '#get_name'):
                    name = event.text
                    Player1.name= name
                    print(name)
                    
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if ENTER_BUTTON.checkForInput(MENU_MOUSE_POS):
                        if(Player1.name!="" and len(Player1.Casinochips)!=0):
                            Player1.display_chips()
                            PlayRoulette(Player1)
                            
                    if BUY_BUTTON.checkForInput(MENU_MOUSE_POS):
                        playClick()
                        BuyYourChips(Player1)
                        
                    if BACK_BUTTON.checkForInput(MENU_MOUSE_POS):
                        is_running = False
                
            
                manager.process_events(event)
            manager.update(UI_REFRESH_RATE)
            manager.draw_ui(window)
            
            
            for button in [ENTER_BUTTON,BUY_BUTTON,BACK_BUTTON]:
                button.changeColor(MENU_MOUSE_POS)
                button.update(window)
                
            
                
                
                        
            # Dibujar la imagen en la pantalla
            window.blit(casinoMan, (10, 210))
            window.blit(casinoMan2, (1050, 210))
            pygame.display.update()
 
    GetFirstData()
        

def FullGameBlackjack():
    
    #Dibuja la pantalla del blackjack
    def GameBlackjack(name, bet, FirstTime):
        
        window.fill((0,0,0))
        print("playing blackjack")
        window.fill((0,0,0))
        BG = pygame.image.load("Graphics/BJBG.jpg").convert_alpha()
            
        window.blit(BG, (0, 0))
        ####Inicializacion de variables y dibujar sobre la pantalla
        Player1 = PlayerBlackjack(name,bet)
        game = Blackjack([Player1])
        game.deck.build()
        game.deck.shuffle()
        Busted = False
        chips = int(Player1.chips)
        
        if (FirstTime == True):
            funds = 200
            totalMoney = funds-chips
        else:
            funds = bet
            chips = 0
            totalMoney =funds-chips
            

        # This is a counter that counts the number of rounds played in a given session
        handsPlayed = 0
        playerCards = pygame.sprite.Group()
        croupierCards = pygame.sprite.Group()
        
        ###coordenadas sobre pantalla
        dCardPos, pCardPos = (),()
        mX, mY = 0, 0
        click = 0
        
        # When the cards have been dealt, roundEnd is zero.
        #In between rounds, it is equal to one
        roundEnd = 1
        # firstTime is a variable that is only used once, to display the initial
        # message at the bottom, then it is set to zero for the duration of the program.
        
        finish = False
        
  
        ###### INITILIZATION ENDS ########
        while True:
 
            MENU_MOUSE_POS = pygame.mouse.get_pos()
            HIT_BUTTON = hitButton(image=pygame.image.load("Graphics/TinyBt.png"), pos=(1150, 350), 
                            text_input="HIT", font=get_font(20), base_color="#d7fcd4", hovering_color="White")
            STAND_BUTTON = standButton(image=pygame.image.load("Graphics/TinyBt.png"), pos=(1150, 400), 
                            text_input="STAND", font=get_font(20), base_color="#d7fcd4", hovering_color="White")
            DEAL_BUTTON = dealButton(image=pygame.image.load("Graphics/TinyBt.png"), pos=(1150, 450), 
                            text_input="DEAL", font=get_font(20), base_color="#d7fcd4", hovering_color="White")
            PLAYAGAIN_BUTTON = Button(image=pygame.image.load("Graphics/TinyBt.png"), pos=(1150, 100), 
                            text_input="PLAY AGAIN", font=get_font(10), base_color="#d7fcd4", hovering_color="White")
            QUIT_BUTTON = Button(image=pygame.image.load("Graphics/TinyBt.png"), pos=(1150, 150), 
                            text_input="QUIT", font=get_font(10), base_color="#d7fcd4", hovering_color="White")
            
            
            BET_TEXT = get_font(20).render("BET", True, "#b68f40")
            BET_RECT = BET_TEXT.get_rect(center=(1150, 550))
            BET_BUTTON =  betButton(image=pygame.image.load("Graphics/TinyBt.png"), pos=(1150, 600), 
                            text_input="+ 10", font=get_font(20), base_color="#d7fcd4", hovering_color="White",
                            text_input2 = "- 10",pos2=(1150, 650) )
            
            
            window.blit(BET_TEXT,BET_RECT)   
            
            if chips > funds:
                # If you lost money, and your bet is greater than your funds, make the bet equal to the funds
                chips = funds

            # Show the blurb at the bottom of the screen, how much money left, and current bet    
            
            fundsFont = pygame.font.Font.render(get_font(11), "Funds: $%.2f" %(totalMoney), 1, (255,255,255), (0,0,0))
            window.blit(fundsFont, (1063,205))
            betFont = pygame.font.Font.render(get_font(11), "Bet: $%.2f" %(chips), 1, (255,255,255), (0,0,0))
            window.blit(betFont, (1080,285))
            hpFont = pygame.font.Font.render(get_font(11), "Round: %i " %(handsPlayed), 1, (255,255,255), (0,0,0))
            window.blit(hpFont, (1063, 180))
            
            
            totalMoney = funds-chips
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    
                    if HIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                        playClick()
                        if(roundEnd!=1):
                            playerCards,pCardPos,roundEnd=HIT_BUTTON.MakeActions(window,game=game, pCardPos=pCardPos,roundEnd=roundEnd,playerCards=playerCards)
  
                    if STAND_BUTTON.checkForInput(MENU_MOUSE_POS):
                        playClick()
                        if(roundEnd!=1):
                            roundEnd,croupierCards = STAND_BUTTON.MakeActions(window, game=game,roundEnd= roundEnd)
                            game.determine_winner()
                            funds = results(game,funds)
                            chips = 0
                            finish = True
                    if DEAL_BUTTON.checkForInput(MENU_MOUSE_POS):
                        playClick()
                        if(roundEnd==1 and finish ==False):
                            playerCards,croupierCards,pCardPos,dCardPos,roundEnd = DEAL_BUTTON.MakeActions(window,game=game,dCardPos=dCardPos, pCardPos=pCardPos,roundEnd=roundEnd)    
                            backStack = pygame.image.load("Graphics/backStack.png").convert_alpha()
                            window.blit(backStack,(890,180))
   
                    if BET_BUTTON.checkForInput(MENU_MOUSE_POS)[0]:
                        
                        playClick()
                        if(roundEnd==1):
                            chips +=10
                            print("INCREASING BET")
                            Player1.chips = chips
                            
                    if BET_BUTTON.checkForInput(MENU_MOUSE_POS)[1]:
                        playClick()
                        if(roundEnd==1):
                            print("DECREASING BET")
                            if(chips>10):
                                chips-=10
                                Player1.chips = chips
                                
                    if PLAYAGAIN_BUTTON.checkForInput(MENU_MOUSE_POS):
                        playClick()
                        print(funds)
                        GameBlackjack(Player1.name,funds,False)
                    if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                        playClick()
                        main_menu()
                    
                elif event.type == pygame.MOUSEBUTTONUP:
                    mX, mY = 0, 0
                    click = 0
  
            for button in [STAND_BUTTON,DEAL_BUTTON, BET_BUTTON,HIT_BUTTON,PLAYAGAIN_BUTTON,QUIT_BUTTON]:
                button.changeColor(MENU_MOUSE_POS)
                button.update(window)
                
    
            if(len(game.pBusted)!=0):    
                if(game.pBusted[0]):
                    
                    if(roundEnd!=1):
                        roundEnd,croupierCards = STAND_BUTTON.MakeActions(window, game=game,roundEnd= roundEnd)
                    roundEnd=1
                    game.determine_winner()
                    funds = results(game,funds)
                    finish = True
                    
                    
                    
   
            if len(playerCards) != 0:
                
                playerCards.update()
                playerCards.draw(window)
                croupierCards.update()
                croupierCards.draw(window)

            pygame.display.update()
            # Controlar la velocidad de fotogramas
            clock.tick(60)
        
    def results(game,funds):
        
        win = game.winners[0]
        player = game.players[0]
        player_value = player.get_hand_value()
        if (win==True):
            RESULTS_TEXT = get_font(20).render(f"{player.name} wins with a hand value of {player_value}!", True, "#b68f40")
            won = int(player.chips)*1.5
            
            funds = funds + won
            won  = str(won)
            player.chips = 0
        elif(win==False):
            RESULTS_TEXT = get_font(20).render(f"{player.name} loses with a hand value of {player_value}!", True, "#b68f40")
            won = "0"
            funds = funds - int(player.chips)
            if(funds<0):
                funds = 0
            player.chips = 0
        elif(win==2):
            RESULTS_TEXT = get_font(20).render(f"{player.name}: It's a tie!", True, "#b68f40")
            
            won = "0"
            
        RESULTS_RECT = RESULTS_TEXT.get_rect(center=(530, 430))
        WON_TEXT = get_font(20).render("You won:"+won, True, "#b68f40")
        WON_RECT = WON_TEXT.get_rect(center=(530, 470))   
        window.blit(RESULTS_TEXT,RESULTS_RECT)
        window.blit(WON_TEXT,WON_RECT)
        
        return funds
    
    #Pantalla para hacer la apuesta inicial
    
    
    def MakingBets():
        manager = pygame_gui.UIManager((1280, 720))
        PlayerName = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((350, 370), (600, 50))
                                                            , manager=manager,object_id='#get_name')
        PlayerBet = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((350, 560), (600, 50))
                                                            , manager=manager,object_id='#get_bet')
        name = ""
        bet = ""
        
        #BOTON
        BACK_BUTTON = Button(image=pygame.image.load("Graphics/TinyBt.png"), pos=(1150, 30), 
                            text_input="BACK", font=get_font(10), base_color="#d7fcd4", hovering_color="White")
        
        ENTER_BUTTON = Button(image=pygame.image.load("Graphics/TinyBt.png"), pos=(620, 654), 
                            text_input="SEND", font=get_font(10), base_color="#d7fcd4", hovering_color="White")
        is_running = True
        while is_running:
            
            MENU_MOUSE_POS = pygame.mouse.get_pos()
            UI_REFRESH_RATE = clock.tick(60)/1000
            window.fill((0,0,0))
            window.blit(background_image, (0, 0))
            
            CHOOSE_TEXT = get_font(45).render("Make your bets", True, "White")
            CHOOSE_RECT = CHOOSE_TEXT.get_rect(center=(640, 200))
            
            BLACKJACK_TEXT = get_font(45).render("¡Welcome to blackjack!", True, "White")
            BLACKJACK_RECT = BLACKJACK_TEXT.get_rect(center=(640, 100))
            
            PLAYERNAME_TEXT = get_font(20).render("Player name:", True, "White")
            PLAYERNAME_RECT = CHOOSE_TEXT.get_rect(center=(640, 350))
            
            BET_TEXT = get_font(20).render("value of you BET:", True, "White")
            BET_RECT = CHOOSE_TEXT.get_rect(center=(640, 530))
            
            # Cargar la imagen
            casinoMan = pygame.image.load("Graphics/CasinoMan.png").convert_alpha()
            casinoMan2 = pygame.image.load("Graphics/CasinoMan2.png").convert_alpha()
            
            window.blit(BET_TEXT,BET_RECT)
            window.blit(BLACKJACK_TEXT, BLACKJACK_RECT)
            window.blit(PLAYERNAME_TEXT,PLAYERNAME_RECT)
            window.blit(CHOOSE_TEXT,CHOOSE_RECT)
            
            #variables a usar
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if (event.type == pygame_gui.UI_TEXT_ENTRY_FINISHED and
                    event.ui_object_id == '#get_name'):
                    name = event.text
                    print(name)
                if (event.type == pygame_gui.UI_TEXT_ENTRY_FINISHED and
                    event.ui_object_id == '#get_bet'):
                    bet = event.text
                    print(bet)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    
                    if ENTER_BUTTON.checkForInput(MENU_MOUSE_POS):
                        if(name !="" and bet != ""):
                            print("Apuesta inicial realizada")
                            player = (name,bet)
                            GameBlackjack(player[0],player[1], True)
                            playClick()
                            
                            
                    if BACK_BUTTON.checkForInput(MENU_MOUSE_POS):
                        is_running = False
                    
            
                manager.process_events(event)
            manager.update(UI_REFRESH_RATE)
            manager.draw_ui(window)
            
            for button in [BACK_BUTTON,ENTER_BUTTON]:
                button.changeColor(MENU_MOUSE_POS)
                button.update(window)
                        
            # Dibujar la imagen en la pantalla
            window.blit(casinoMan, (10, 210))
            window.blit(casinoMan2, (1050, 210))
            pygame.display.update()
            

    #La logica del juego esta en la clase blackjack

    MakingBets()

#Iniciar la interfaz
main_menu()
# Salir del juego
pygame.quit()
sys.exit()
