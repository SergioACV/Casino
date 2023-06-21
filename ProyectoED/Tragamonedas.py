from maquina import Maquina
from settings import *
import ctypes, pygame, sys
from Button import Button





class Tragamonedas:
    
    
    def __init__(self):

        # General setup
        pygame.init()
        self.pantalla = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('Maquina tragaperras')
        self.clock = pygame.time.Clock()
        self.bg_image = pygame.image.load(BG_IMAGE_PATH).convert_alpha()
        self.grid_image = pygame.image.load(GRID_IMAGE_PATH).convert_alpha()
        self.maquina = Maquina()
        self.delta_time = 0

        # Sound
        self.main_sound = pygame.mixer.Sound('audio/track.mp3')
        self.main_sound.play(loops = -1)

    def run(self):
        
        self.start_time = pygame.time.get_ticks()
        
        is_running = True
        
        #Boton para volver al menu principal
        QUIT_BUTTON = Button(image=pygame.image.load("Graphics/TinyBt.png"), pos=(800, 950), 
                            text_input="QUIT", font=pygame.font.Font("Font/font.ttf", 10), base_color="#d7fcd4", hovering_color="White")
        
        while is_running:
            MENU_MOUSE_POS = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    
                    if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                        self.main_sound.stop()
                        return True
                        
                

            # Variables de tiempo
            self.delta_time = (pygame.time.get_ticks() - self.start_time) / 1000
            self.start_time = pygame.time.get_ticks()
            
            for button in [QUIT_BUTTON]:
                button.changeColor(MENU_MOUSE_POS)
                button.update(self.pantalla)

            pygame.display.update()
            self.pantalla.blit(self.bg_image, (0, 0))
            self.maquina.update(self.delta_time)
            self.pantalla.blit(self.grid_image, (0, 0))
            self.clock.tick(FPS)
    
    def Stop(self):
        
        del self


if __name__ == '__main__':
    game = Tragamonedas()
    game.run()