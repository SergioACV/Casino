import pygame
import pygame_gui
import sys
from Button import Button, hitButton, dealButton,standButton, betButton
import random
from Card import Card
from Player import Player, PlayerBlackjack
from Deck import Deck
from Blackjack import Blackjack
import os

# Inicializar Pygame
pygame.init()

# Configuración de la ventana
window_width = 1280
window_height = 720
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Blackjack Game")

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
        
        BLACKJACK_BUTTON = Button(image=pygame.image.load("Graphics/GamesBG.png"), pos=(640, 250), 
                            text_input="BLACKJACK", font=get_font(60), base_color="#d7fcd4", hovering_color="White")
        POKER_BUTTON = Button(image=pygame.image.load("Graphics/GamesBG.png"), pos=(640, 400), 
                            text_input="POKER", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        ROULLETTE_BUTTON = Button(image=pygame.image.load("Graphics/GamesBG.png"), pos=(640, 550), 
                            text_input="ROULLETTE", font=get_font(60), base_color="#d7fcd4", hovering_color="White")
        
        
        #display
        window.blit(background_image, (0, 0))
        window.blit(MENU_TEXT,MENU_RECT)
        
        
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if BLACKJACK_BUTTON.checkForInput(MENU_MOUSE_POS):
                    print("entering blackjack")
                    playClick()
                    FullGameBlackjack()
                if POKER_BUTTON.checkForInput(MENU_MOUSE_POS):
                    playClick()
                    print("entering poker")
                if ROULLETTE_BUTTON.checkForInput(MENU_MOUSE_POS):
                    playClick()
                    print("enterir roullette")
    
        for button in [BLACKJACK_BUTTON, POKER_BUTTON, ROULLETTE_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(window)

        # Actualizar la ventana
        pygame.display.update()
        # Controlar la velocidad de fotogramas
        clock.tick(60)

def FullGameBlackjack():
    #Primera pantalla cuando se incial el juego
    #llama las funciones para pedir los datos del jugador e iniciar la partidad
    def playBlackjack():
        
        makeBet = False
        while True:
            PLAY_MOUSE_POS = pygame.mouse.get_pos()
            
            window.fill((0,0,0))
            window.blit(background_image, (0, 0))

            BLACKJACK_TEXT = get_font(45).render("¡Welcome to blackjack!", True, "White")
            BLACKJACK_RECT = BLACKJACK_TEXT.get_rect(center=(640, 100))
            
            
            window.blit(BLACKJACK_TEXT, BLACKJACK_RECT)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            
            #logica
            
            if not makeBet:
                print("Making the bets")
                player = MakingBets()
                GameBlackjack(player[0],player[1], True)
            
                makeBet= True

            pygame.display.update()

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
        
        while True:
            
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
                
            
                manager.process_events(event)
            manager.update(UI_REFRESH_RATE)
            manager.draw_ui(window)
                        
            # Dibujar la imagen en la pantalla
            window.blit(casinoMan, (10, 210))
            window.blit(casinoMan2, (1050, 210))
            pygame.display.update()
            
            if(name !="" and bet != ""):
                print("Apuesta inicial realizada")
                playClick()
                return name,bet
            
    
    #La logica del juego esta en la clase blackjack

    playBlackjack()

#Iniciar la interfaz
main_menu()
# Salir del juego
pygame.quit()
sys.exit()
