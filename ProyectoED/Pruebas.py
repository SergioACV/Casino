import random
from Card import Card
from Player import Player, PlayerBlackjack
from Deck import Deck
from Blackjack import Blackjack
from Roulette import roulette
from CasinoChip import CasinoChip
from Player import Player,PlayerRoulette

player = PlayerRoulette("Sergio",500)
player.add_chips(5, 10)
player.add_chips(10, 5)
player.add_chips(25, 3)
player.display_chips()





