import pygame
import os
from Blackjack import Blackjack
from Player import Player, PlayerBlackjack
from Deck import Deck
from Card import Card


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
    
 
    
    
    
        
