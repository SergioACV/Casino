import random
from Card import Card
from Player import Player, PlayerBlackjack
from Deck import Deck
from Blackjack import Blackjack

# Creación de objetos PlayerBlackjack
player1 = PlayerBlackjack("Player 1", 100)
player2 = PlayerBlackjack("Player 2", 150)

# Creación de objeto Blackjack y pasando los jugadores como una lista
game = Blackjack([player1, player2])

# Iniciar el juego
#game.play_game()



