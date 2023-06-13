import random
from Card import Card
import pygame

class Deck():
    
    
    def __init__(self):
        
        self.cards = []
        

    def build(self):
        
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        values = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
        self.cards = [Card(value, suit, (0,0)) for suit in suits for value in values]

    def shuffle(self):
        random.shuffle(self.cards)

    def draw_card(self):
        if(len(self.cards)!=0):
            return self.cards.pop()
        

    def cards_remaining(self):
        return len(self.cards)
