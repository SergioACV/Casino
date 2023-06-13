import random
from Card import Card
from Player import Player, PlayerBlackjack
from Deck import Deck

class Blackjack:
    def __init__(self, players):
        self.players = players
        self.croupier = PlayerBlackjack("Croupier", 0)  # Croupier como instancia de PlayerBlackjack
        self.deck = Deck()
        self.pBusted = []
        self.winners= []
        self.dBsusted =False
        self.deadDeck = Deck()
        self.deck.shuffle()
        

    def deal_initial_cards(self):
        for _ in range(2):
            for player in self.players:
                card = self.deck.draw_card()
                player.receive_card(card)

            card = self.deck.draw_card()
            self.croupier.receive_card(card)

    def stand(self):
        
        print("\nCroupier's Turn:")
        self.croupier.display_hand()
        i=0
        while self.croupier.get_hand_value() < 17:
            i+=1
            card = self.deck.draw_card()
            self.croupier.receive_card(card)
            self.croupier.display_hand()

            if self.croupier.get_hand_value() > 21:
                print("Croupier Busted!")
        print("AFTER")
        return i
        self.croupier.display_hand()

    def determine_winner(self):
        croupier_value = self.croupier.get_hand_value()
        self.winners = []
        print("\n-- Game Results --")
        for player in self.players:
            player_value = player.get_hand_value()

            if player_value > 21:
                print(f"{player.name}: Busted!")
                self.winners.append(False)
            elif croupier_value > 21:
                print(f"{player.name} wins with a hand value of {player_value}!")
                self.winners.append(True)
            elif player_value > croupier_value:
                print(f"{player.name} wins with a hand value of {player_value}!")
                self.winners.append(True)
            elif player_value < croupier_value:
                print(f"{player.name} loses with a hand value of {player_value}!")
                self.winners.append(False)
            else:
                print(f"{player.name}: It's a tie!")
                self.winners.append(2)
            
        return self.winners
  

    def play_game(self):
        print("-- Blackjack Game --")
        self.deal_initial_cards()

        for player in self.players:
            print(f"\n{player.name}'s Turn:")
            player.display_hand()

        self.play_round()
        self.determine_winner()
    
    def hit(self):
        
        # if the deck is empty, shuffle in the dead deck
        if len(self.deck.cards) == 0:
            self.returnFromDead()
            
        else:
            for player in self.players:
                card = self.deck.draw_card()
                self.deadDeck.cards.append(card)
                player.receive_card(card)
                player.display_hand()
        
        self.Busted()

    #cartas usadas nuevamente en la baraja
    def returnFromDead(self):
        """ Appends the cards from the deadDeck to the deck that is in play. This is called when the main deck
        has been emptied. """
        print("RETURNING FROM DEAD")
        for card in self.deadDeck.cards:
            self.deck.cards.append(card)
        
        self.deadDeck.cards = []
        
        self.deck = self.deck.shuffle()
    
    def Busted(self):
        self.pBusted = []
        for player in self.players:
            
            hv= player.get_hand_value()
            if(hv>21):
                self.pBusted.append(True)
            else:
                self.pBusted.append(False)
        
        hv =self.croupier.get_hand_value()
        if(hv>21):
            dBusted = True
        else:
            dBusted = False
        
            
                

        
