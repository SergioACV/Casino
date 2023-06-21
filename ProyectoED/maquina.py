from jugador import Jugador
from reel import *
from settings import *
from ui import UI
from wins import *
import pygame

class Maquina:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()
        self.balance_maquina = 10000.00
        self.reel_index = 0
        self.reel_list = {}
        self.can_toggle = True
        self.girando = False
        self.puede_animar = False
        self.animacion_ganar_encurso = False

        # Resultados Con diccionarios
        self.resultado_anterior = {0: None, 1: None, 2: None, 3: None, 4: None}
        self.resultado_actual = {0: None, 1: None, 2: None, 3: None, 4: None}

        self.spawn_reels()
        self.jugadoractual = Jugador()
        self.ui = UI(self.jugadoractual)

    def cooldowns(self):
        # Hace un cooldown para tirar
        for reel in self.reel_list:
            if self.reel_list[reel].reel_is_spinning:
                self.can_toggle = False
                self.girando = True

        if not self.can_toggle and [self.reel_list[reel].reel_is_spinning for reel in self.reel_list].count(False) == 5:
            self.can_toggle = True
            self.resultado_actual = self.get_result()

            if self.check_wins(self.resultado_actual):
                self.win_data = self.check_wins(self.resultado_actual)
                self.pay_player(self.win_data, self.jugadoractual)
                self.animacion_ganar_encurso = True
                self.ui.win_text_angle = random.randint(-4, 4)

    def input(self):
        keys = pygame.key.get_pressed()

        # checkea si se puede tirar y si se apreto espacio
        if keys[pygame.K_SPACE] and self.can_toggle and self.jugadoractual.balance >= self.jugadoractual.bet_size:
            self.toggle_spinning()
            self.spin_time = pygame.time.get_ticks()
            self.jugadoractual.place_bet()
            self.balance_maquina += self.jugadoractual.bet_size
            self.jugadoractual.last_payout = None
            
    def draw_reels(self, delta_time):
        for reel in self.reel_list:
            self.reel_list[reel].animate(delta_time)

    def spawn_reels(self):
        if not self.reel_list:
            x_topleft, y_topleft = 10, -300
        while self.reel_index < 5:
            if self.reel_index > 0:
                x_topleft, y_topleft = x_topleft + (300 + X_OFFSET), y_topleft
            
            self.reel_list[self.reel_index] = Reel((x_topleft, y_topleft)) 
            self.reel_index += 1

    def toggle_spinning(self):
        if self.can_toggle:
            self.spin_time = pygame.time.get_ticks()
            self.girando = not self.girando
            self.can_toggle = False

            for reel in self.reel_list:
                self.reel_list[reel].start_spin(int(reel) * 200)
                self.animacion_ganar_encurso = False

    def get_result(self):
        for reel in self.reel_list:
            self.resultado_actual[reel] = self.reel_list[reel].reel_spin_result()
        return self.resultado_actual

    def check_wins(self, result):
        hits = {}
        horizontal = flip_horizontal(result)
        for row in horizontal:
            for sym in row:
                if row.count(sym) > 2: 
                    possible_win = [idx for idx, val in enumerate(row) if sym == val]

                    # Checkea una posible victoria con mas de 2 rows
                    if len(longest_seq(possible_win)) > 2:
                        hits[horizontal.index(row) + 1] = [sym, longest_seq(possible_win)]
        if hits:
            self.puede_animar = True
            return hits

    def pay_player(self, win_data, curr_player):
        multiplier = 0
        spin_payout = 0
        for v in win_data.values():
            multiplier += len(v[1])
        spin_payout = (multiplier * curr_player.bet_size)
        curr_player.balance += spin_payout
        self.balance_maquina -= spin_payout
        curr_player.last_payout = spin_payout
        curr_player.total_won += spin_payout


    def play_win_sound(self, win_data):
        sum = 0
        for item in win_data.values():
            sum += len(item[1])
        if sum == 3: self.win_three.play()
        elif sum == 4: self.win_four.play()
        elif sum > 4: self.win_five.play()

    def win_animation(self):
        if self.animacion_ganar_encurso and self.win_data:
            for k, v in list(self.win_data.items()):
                if k == 1:
                    animationRow = 3
                elif k == 3:
                    animationRow = 1
                else:
                    animationRow = 2
                animationCols = v[1]
                for reel in self.reel_list:
                    if reel in animationCols and self.puede_animar:
                        self.reel_list[reel].symbol_list.sprites()[animationRow].fade_in = True
                    for symbol in self.reel_list[reel].symbol_list:
                        if not symbol.fade_in:
                            symbol.fade_out = True

    def update(self, delta_time):
        self.cooldowns()
        self.input()
        self.draw_reels(delta_time)
        for reel in self.reel_list:
            self.reel_list[reel].symbol_list.draw(self.display_surface)
            self.reel_list[reel].symbol_list.update()
        self.ui.update()
        self.win_animation()
