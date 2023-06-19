import pygame
import os
from Blackjack import Blackjack
from Player import Player, PlayerBlackjack
from Deck import Deck
from Card import Card
from CasinoChip import CasinoChip


class Button():
    def __init__(self, image, pos, text_input, font, base_color, hovering_color):
        self.image = image
        self.x_pos = pos[0]
        self.y_pos = pos[1]
        self.font = font
        self.base_color, self.hovering_color = base_color, hovering_color
        self.text_input = text_input
        self.text = self.font.render(self.text_input, True, self.base_color)
        if self.image is None:
            self.image = self.text
            
        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
        self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))
    
    def update(self, screen):
        if self.image is not None:
            screen.blit(self.image, self.rect)
        screen.blit(self.text, self.text_rect)
    
    def checkForInput(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            return True
        return False
    
    def changeColor(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            self.text = self.font.render(self.text_input, True, self.hovering_color)
        else:
            self.text = self.font.render(self.text_input, True, self.base_color)
        
        
class hitButton(Button):
    
    def MakeActions(self, screen,game,pCardPos,roundEnd,playerCards):
        super().update(screen)
        
        
        if(roundEnd == 0):
            
            print("HITING A CARD")
            
            
            playerHand = game.players[0].cards
            
            playerCards1 = pygame.sprite.Group()
            playerCards1 = playerCards
        
            game.hit()
            player = game.players[0]
            ValueHand = player.get_hand_value()
            
            print("VALUE OF THE HAND ",ValueHand)
            
            game.players[0].display_hand()
            currentCard = len(game.players[0].cards) - 1
            card = game.players[0].cards[currentCard]
            card.update_position(pCardPos)
            
            playerCards1.add(card)
            pCardPos = (pCardPos[0] - 80, pCardPos[1])
            print(game.pBusted[0])
            
        
            return playerCards1,pCardPos,roundEnd

class standButton(Button):
    def MakeActions(self, screen,game,roundEnd):
        
        if(roundEnd ==0):
            
            print("STAND CARS")

            dealerHand = game.croupier.cards
            
            dealerCards = pygame.sprite.Group()
      
            AddedCards = game.stand()

            #Actualizar posiciones de la cartas del dealers
            dealerHand = game.croupier.cards
            dCardPos = (450, 145)
            
            for card in dealerHand:
                card.update_position(dCardPos)
                dCardPos = (dCardPos[0] + 80, dCardPos[1])
                dealerCards.add(card)  
            roundEnd=1
            return roundEnd,dealerCards

class dealButton(Button):
    
                
    def MakeActions(self, screen,game,pCardPos,dCardPos,roundEnd):
        super().update(screen)
    
    
        pCardPos = (580,570)
        dCardPos = (450, 145)
        playerCardSprite = pygame.sprite.Group()
        dealerCardSprite = pygame.sprite.Group()
        
        
        if(roundEnd == 1): 
            print("MAKE DEAL:STARTING ROUND")
            playerHand = game.players[0].cards
            dealerHand = game.croupier.cards
            
            game.deal_initial_cards()   
            for card in playerHand:
                
                card.update_position(pCardPos)
                pCardPos = (pCardPos[0] - 80, pCardPos [1])
                playerCardSprite.add(card)
                
                
            if(len(dealerHand)!=0):   
                backwardsCard = Card("back","",(0,0))
                backwardsCard.update_position(dCardPos)
                dCardPos = (dCardPos[0] + 80, dCardPos[1])
                dealerHand[0].update_position(dCardPos)
                
                dealerCardSprite.add(backwardsCard)
                dealerCardSprite.add(dealerHand[0])
            
            
            roundEnd = 0
            
            
            game.players[0].display_hand()
        return playerCardSprite,dealerCardSprite,pCardPos,dCardPos,roundEnd
        
        
        
        
        
        

class betButton(Button):
    def __init__(self, image, pos, text_input, font, base_color, hovering_color,text_input2,pos2):
        self.image = image
        self.image2 = image
        
        self.x_pos = pos[0]
        self.y_pos = pos[1]
        
        self.x_pos2 = pos2[0]
        self.y_pos2 = pos2[1]
        
        
        self.font = font
        self.base_color, self.hovering_color = base_color, hovering_color
        self.text_input = text_input
        self.text_input2 = text_input2
        self.text = self.font.render(self.text_input, True, self.base_color)
        self.text2 = self.font.render(self.text_input2, True, self.base_color)
        if self.image is None:
            self.image = self.text
            self.image2 = self.text2
        
        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
        self.rect2 = self.image2.get_rect(center=(self.x_pos2, self.y_pos2))
        self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))
        self.text_rect2 = self.text2.get_rect(center=(self.x_pos2, self.y_pos2))
    
    def update(self, screen):
        if self.image is not None:
            screen.blit(self.image, self.rect)
            screen.blit(self.image2, self.rect2)
        
        screen.blit(self.text, self.text_rect)
        screen.blit(self.text2, self.text_rect2)
    
    def checkForInput(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            return True,False
        if position[0] in range(self.rect2.left, self.rect2.right) and position[1] in range(self.rect2.top, self.rect2.bottom):
            return False,True
        
        return False,False
    
    def changeColor(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            self.text = self.font.render(self.text_input, True, self.hovering_color)
        
        else:
            self.text = self.font.render(self.text_input, True, self.base_color)
        
        if position[0] in range(self.rect2.left, self.rect2.right) and position[1] in range(self.rect2.top, self.rect2.bottom):
            self.text2 = self.font.render(self.text_input2, True, self.hovering_color)
        else:
            self.text2 = self.font.render(self.text_input2, True, self.base_color)
    

class RouletteButtonBets():
    def __init__(self):
        
        
        #Pila para las apuestas hechas
        self.stacks = {}
        
        #Atributos a usar
        self.ActualBet = ""
        
        #numbers
        
        self.numberSquareSize = (65,86)
        self.initialCords = (121,267)
        self.bigSquareX = (121,896)
        self.bigSquareY = (267,533)
        
        #THIRDS
        self.thirdsSquareSize = (257,64)
        self.thirdsInitialCords = (120,537)
        self.thirdsSquareSizeBigX = (122,896)
        self.thirdsSquareSizeBigY = (538,600)
        
        #EVEN, ODD, COLORS
        self.OtherBetsSquareSize = (130,61)
        self.OtherBetsInitialCords = (123,605)
        self.OtherBetsSquareBigX = (123,896)
        self.OtherBetsSquareBigY = (604,667)
        
        #Zero
        self.ZeroSquareX = (48,109)
        self.ZeroSquareY = (373,430)
        
        
        
        
        self.numberMatrix = [[3,6,9,12,15,18,21,24,27,30,33,36],
                            [2,5,8,11,14,17,20,23,26,29,32,35],
                            [1,4,7,10,13,16,19,22,25,28,31,34]]
        
        self.thirds = ["1st12","2nd12","3rd12"]
        self.OtherBets = ["1to18","EVEN","RED","BLACK","ODD","19to36"]
    
    
    def create_stack(self, name):
        if name not in self.stacks:
            self.stacks[name] = []
        
    def remove_stack(self, name):
        if name in self.stacks:
            del self.stacks[name]
            
    def push(self, name, chip):
        if name in self.stacks and isinstance(chip, CasinoChip):
            print("haciendo push")
            self.stacks[name].append(chip)

    def pop(self, name):
        if name in self.stacks:
            if not self.is_empty(name):
                return self.stacks[name].pop()
        return None

    def is_empty(self, name):
        if name in self.stacks:
            return len(self.stacks[name]) == 0
        return True   
        
    
    def checkForInput(self, position):
        
        if position[0] in range(self.bigSquareX[0], self.bigSquareX[1]) and position[1] in range(self.bigSquareY[0], self.bigSquareY[1]):
            columna = (position[0]-self.initialCords[0])//self.numberSquareSize[0]
            fila = (position[1]-self.initialCords[1])//self.numberSquareSize[1]
            print("You push square",self.numberMatrix[fila][columna])
            self.ActualBet = self.numberMatrix[fila][columna]
            
            return True
        elif position[0] in range(self.thirdsSquareSizeBigX[0], self.thirdsSquareSizeBigX[1]) and position[1] in range(self.thirdsSquareSizeBigY[0], self.thirdsSquareSizeBigY[1]):
            columna = (position[0]-self.thirdsInitialCords[0])//self.thirdsSquareSize[0]
            print("You push ",self.thirds[columna])
            self.ActualBet = self.thirds[columna]
            
            return True
        elif position[0] in range(self.OtherBetsSquareBigX[0], self.OtherBetsSquareBigX[1]) and position[1] in range(self.OtherBetsSquareBigY[0], self.OtherBetsSquareBigY[1]):
            columna = (position[0]-self.OtherBetsInitialCords[0])//self.OtherBetsSquareSize[0]
            print("You pushh ",self.OtherBets[columna])
            self.ActualBet = self.OtherBets[columna] 
            
            return True
        elif position[0] in range(self.ZeroSquareX[0], self.ZeroSquareX[1]) and position[1] in range(self.ZeroSquareY[0], self.ZeroSquareY[1]):
            print("You push zero")
            self.ActualBet = "Zero"
            
            return True
    
    def MakeActions(self,Player,pressed,pos):
        
        if pressed[0]:
            if 10 in Player.Casinochips:
                self.create_stack(self.ActualBet)
                Player.remove_chips(10,1)
                GenericChip = CasinoChip(10,pos)
                self.push(self.ActualBet,GenericChip)
                
            return Player
        elif pressed[1]:
            if 25 in Player.Casinochips:
                self.create_stack(self.ActualBet)
                Player.remove_chips(25,1)
                GenericChip = CasinoChip(25,pos)
                self.push(self.ActualBet,GenericChip)
            
        elif pressed[2]:
            if 50 in Player.Casinochips:
                self.create_stack(self.ActualBet)
                Player.remove_chips(50,1)
                GenericChip = CasinoChip(50,pos)
                self.push(self.ActualBet,GenericChip)
                
            return Player
        elif pressed[3]:
            if 100 in Player.Casinochips:
                self.create_stack(self.ActualBet)
                Player.remove_chips(100,1)
                GenericChip = CasinoChip(100,pos)
                self.push(self.ActualBet,GenericChip)
                
            return Player
        return Player
    
    def DeleteChipsInStack(self,Player):
        
        card = self.pop(self.ActualBet)
        if card != None:
            denomination = card.denomination
            Player.add_chips(denomination,1)
            return Player,card
        else:
            return Player, None
        
    
class SelectChipButton(Button):
    def __init__(self, image1, pos,image2,pos2,image3,pos3,image4,pos4,image1_1,image2_2,image3_3,image4_4):
        self.image1 = image1
        self.image1_1 = image1_1
        self.image2 = image2
        self.image2_2 = image2_2
        self.image3 = image3
        self.image3_3 = image3_3
        self.image4 = image4
        self.image4_4 = image4_4
        
        self.x_pos = pos[0]
        self.y_pos = pos[1]
        
        self.x_pos2 = pos2[0]
        self.y_pos2 = pos2[1]
        
        self.x_pos3 = pos3[0]
        self.y_pos3 = pos3[1]
        
        self.x_pos4 = pos4[0]
        self.y_pos4 = pos4[1]
        
        self.rect = self.image1.get_rect(center=(self.x_pos, self.y_pos))
        self.rect1_1 = self.image1_1.get_rect(center=(self.x_pos, self.y_pos))
        self.rect2 = self.image2.get_rect(center=(self.x_pos2, self.y_pos2))
        self.rect2_2 = self.image2_2.get_rect(center=(self.x_pos2, self.y_pos2))
        
        self.rect3 = self.image3.get_rect(center=(self.x_pos3, self.y_pos3))
        self.rect3_3 = self.image3_3.get_rect(center=(self.x_pos3, self.y_pos3))
        
        self.rect4 = self.image4.get_rect(center=(self.x_pos4, self.y_pos4))
        self.rect4_4 = self.image4_4.get_rect(center=(self.x_pos4, self.y_pos4))
        
        self.image1Display = self.image1
        self.image1DisplayRect = self.rect
        
        self.image2Display = self.image2
        self.image2DisplayRect = self.rect2
        
        self.image3Display = self.image3
        self.image3DisplayRect = self.rect3
        
        self.image4Display = self.image4
        self.image4DisplayRect = self.rect4
        
        
        self.pressed = (False,False,False,False)
        
    
    def update(self, screen):
        
        screen.blit(self.image1Display,self.image1DisplayRect)
        screen.blit(self.image2Display,self.image2DisplayRect)
        screen.blit(self.image3Display,self.image3DisplayRect)
        screen.blit(self.image4Display, self.image4DisplayRect)
            
        
        
    
    def checkForInput(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            if(self.pressed[0] == False):
                self.pressed= (True,False,False,False)
            elif(self.pressed[0] == True):
                self.pressed= (False,False,False,False)
            self.UpdateImage()
            return True
        if position[0] in range(self.rect2.left, self.rect2.right) and position[1] in range(self.rect2.top, self.rect2.bottom):
            if(self.pressed[1] == False):
                self.pressed= (False,True,False,False)
            elif(self.pressed[1] == True):
                self.pressed= (False,False,False,False)
            self.UpdateImage()
            return True
        if position[0] in range(self.rect3.left, self.rect3.right) and position[1] in range(self.rect3.top, self.rect3.bottom):
            if(self.pressed[2] == False):
                self.pressed= (False,False,True,False)
            elif(self.pressed[2] == True):
                self.pressed= (False,False,False,False)
            
            self.UpdateImage()
            return True
        if position[0] in range(self.rect4.left, self.rect4.right) and position[1] in range(self.rect4.top, self.rect4.bottom):
            if(self.pressed[3] == False):
                self.pressed= (False,False,False,True)
            elif(self.pressed[3] == True):
                self.pressed= (False,False,False,False)
            self.UpdateImage()
            return True
        
        return False
    
    
    
    def UpdateImage(self):
        
        if(self.pressed[0]):
            self.image1Display = self.image1_1
            self.image1DisplayRect = self.rect1_1
        else:
            self.image1Display = self.image1
            self.image1DisplayRect = self.rect
            
        if self.pressed[1]:
            self.image2Display = self.image2_2
            self.image2DisplayRect = self.rect2_2
        else:
            self.image2Display =self.image2
            self.image2DisplayRect = self.rect2
            
        if self.pressed[2]:
            self.image3Display = self.image3_3
            self.image3DisplayRect = self.rect3_3
        else:
            self.image3Display = self.image3
            self.image3DisplayRect = self.rect3
        
        if self.pressed[3]:
            self.image4Display = self.image4_4
            self.image4DisplayRect = self.rect4_4
        else:
            self.image4Display = self.image4
            self.image4DisplayRect = self.rect4
        
            
    
    def changeColor(self, position):
        pass
        
    
class BuyChips(Button):
    pass
    
        
