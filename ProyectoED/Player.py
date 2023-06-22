from Card import Card
from CasinoChip import CasinoChip

class Player:
    def __init__(self, name, chips):
        self.name = name
        self.chips = chips
        

    def display_info(self):
        print(f"Player: {self.name}")
        print(f"Chips: {self.chips}")


class PlayerBlackjack(Player):
    def __init__(self, name, chips):
        super().__init__(name, chips)
        self.cards = []
        

    def receive_card(self, card):
        self.cards.append(card)

    def get_hand_value(self):
        hand_value = 0
        num_aces = 0

        for card in self.cards:
            if card.value in ['Jack', 'Queen', 'King']:
                hand_value += 10
            elif card.value == 'Ace':
                hand_value += 11
                num_aces += 1
            else:
                hand_value += int(card.value)

        while hand_value > 21 and num_aces > 0:
            hand_value -= 10
            num_aces -= 1

        return hand_value

    def reset_hand(self):
        self.cards = []

    def display_hand(self):
        print(f"{self.name}'s Hand:")
        for card in self.cards:
            card.show()
    
    

class PlayerRoulette(Player):
    def __init__(self, name, chips):
        super().__init__(name, chips)
        self.Casinochips = {}
        self.funds = chips
        
    #ROULETTE FEATURES
    def add_chips(self, denomination, amount):
        
        total = amount*denomination
        self.funds = self.funds - total
        if denomination in self.Casinochips:
            
            self.Casinochips[denomination].add_chips(amount)
            
        else:
            chip = CasinoChip(denomination,(0,0))
            chip.add_chips(amount)
            self.Casinochips[denomination] = chip

    def remove_chips(self, denomination, amount):
        
        if denomination in self.Casinochips:
            
            
            quit = self.Casinochips[denomination].remove_chips(amount)
            if quit:
                total = amount*denomination
                self.funds = self.funds + total
                
                
            if self.Casinochips[denomination].amount == 0:
                del self.Casinochips[denomination]
        else:
            print("No hay fichas de esa denominación.")
            
    def ChipInPlayer(self,denomination):
        
        return denomination in self.Casinochips

    def display_chips(self):
        print("Fichas del jugador:")
        for chip in self.Casinochips.values():
            chip.display()
        

