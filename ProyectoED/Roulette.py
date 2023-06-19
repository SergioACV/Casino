import random
import pygame
import time
import sys

class Roulette:
    
    
    
    
    def __init__(self):
        self.wheel = {
            0: 'green',
            1: 'red',
            2: 'black',
            3: 'red',
            4: 'black',
            5: 'red',
            6: 'black',
            7: 'red',
            8: 'black',
            9: 'red',
            10: 'black',
            11: 'black',
            12: 'red',
            13: 'black',
            14: 'red',
            15: 'black',
            16: 'red',
            17: 'black',
            18: 'red',
            19: 'red',
            20: 'black',
            21: 'red',
            22: 'black',
            23: 'red',
            24: 'black',
            25: 'red',
            26: 'black',
            27: 'red',
            28: 'black',
            29: 'black',
            30: 'red',
            31: 'black',
            32: 'red',
            33: 'black',
            34: 'red',
            35: 'black',
            36: 'red'
        }
        
        self.red = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
        self.black = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]
        self.odd = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35]
        self.even = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36]
    
    def resultsRoulette(self,Player,Bets,luckyNumber):
        
        #Variables a usar
        funds = Player.funds
        won = 0
        win = False
        #Comprobar que al menos halla ganador
        for bet in Bets:
            print(bet)
            win = False
            
            #contar cuanto aposto
            
            contar = Bets[bet]
            num = 0
            for i in range(0,len(contar)):
                
                num+=(contar[i].denomination)
            
            #Si gana por numero
            
            if (bet == "Zero"):
                print("ud aposto por el cero la cantidad de",num)
                if luckyNumber ==0:
                    num = num*36 
                    print("you win(36x):",num)
                    win = True
                    
            
            if(luckyNumber!=0):
                if bet in range(1,37):
                    print("ud aposto por el", bet," la cantidad de",num)
                    if bet == luckyNumber:
                        num = num*36
                        print("you win(36x):",num)
                        win = True
                        
                
                if(bet == "1st12"):
                    print("ud aposto por el primer tercio la cantidad de ",num) 
                    
                    if luckyNumber >=1 and luckyNumber <=12:
                        num = num*3
                        print("you win(3x):",num)
                        win = True    
                if(bet == "2nd12"):
                    print("ud aposto por el segundo  la cantidad de",num)   
                    if luckyNumber >=13 and luckyNumber <=24:
                        num = num*3 
                        print("you win(3x):",num)
                        win = True
                            
                if (bet == "3rd12"):
                    print("ud aposto por el tercer tercio la cantidad de",num)
                    if luckyNumber >=25 and luckyNumber <=36:
                        num = num*3 
                        print("you win(3x):",num)
                        win = True
                if(bet == "1to18"):
                    print("ud aposto de 1 a 18 la cantidad de",num)
                    if luckyNumber >=1 and luckyNumber <=18:
                        num = num*2 
                        print("you win(2x):",num)
                        win = True
                if(bet == "EVEN"):
                    print("ud aposto por los pares la cantidad de",num)
                    if luckyNumber%2==0:
                        num = num*2
                        print("you win(2x):",num)
                        win = True
                if(bet == "RED"):
                    print("ud aposto por los rojos la cantidad de",num)
                    if luckyNumber in self.red:
                        num = num*2
                        print("you win(2x):",num)
                        win = True
                if(bet == "BLACK"):
                    print("ud aposto por los negros la cantidad de",num)
                    if luckyNumber in self.black:
                        num = num*2 
                        print("you win(2x):",num)
                        win = True
                if (bet == "ODD"):
                    print("ud aposto por los impares la cantidad de",num)
                    if luckyNumber %2!=0:
                        num = num*2 
                        print("you win(2x):",num)
                        win = True
                if (bet == "19to36"):
                    print("ud aposto por los numeros del 19 al 36 la cantidad de",num)
                    if luckyNumber >=19 and luckyNumber <=36:
                        num = num*2 
                        print("you win(2x):",num)
                        win = True
            
            if(win):  
                won+=num
        
        print("YOU FINALLY WON: ",won)
        return won
        
    
    def check_key(self,dictionary, value):
        if value in dictionary:
            return True
        else:
            return False      
        
    def spin_wheel(self):
        
        number = random.randint(0, 36)
        return number
        

    def get_color(self, number):
        return self.wheel[number]


# Usage example

