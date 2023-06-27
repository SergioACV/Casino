import ctypes, pygame, pymunk

TITLE_STRING = 'PLINKO DS_PROYECT'
FPS = 60

ctypes.windll.user32.SetProcessDPIAware()

WIDTH = 1600
HEIGTH = 1000

BACKGROUND_C = (40, 2, 58)
MULTI_HEIGTH = int(HEIGTH/19)
MULTI_COLLISION = HEIGTH -(MULTI_HEIGTH * 2)

SCORE_RECT = int(WIDTH/16)

OBSTACLE_C = (255, 255, 255)
OBSTACLE_R = int(HEIGTH/240)
OBSTACLE_P = int(HEIGTH/19)
OBSTACLE_S = (int((WIDTH/2)-OBSTACLE_P), int((HEIGTH-(HEIGTH*0.9))))
segmentA_2 = OBSTACLE_S

BALL_R = 15

multipliers = {
    "1000":0,
    "500":0,
    "200":0,
    "100":0,
    "50":0,
    "10":0,
    "2":0,
    "0":0
}

multipliers_c = {
    (0, 1000):(0,255,0),
    (1, 500):(128,255,0),
    (2, 200):(255,255,0),
    (3, 100):(255,205,0),
    (4, 50):(255,180,0),
    (5, 10):(255,150,0),
    (6, 2):(255,128,0),
    (7, 0):(255,0,0),
    (8, 0):(255,0,0),
    (9, 0):(255,0,0),
    (10, 2):(255,128,0),
    (11, 10):(255,150,0),
    (12, 50):(255,180,0),
    (13, 100):(255,205,0),
    (14, 200):(255,255,0),
    (15, 500):(128,255,0),
    (16, 1000):(0,255,0)
}

NUM_MULTI = 17

BALL_CLASS = 1
OBSTACLE_CLASS = 2
BALL_MASK = pymunk.ShapeFilter.ALL_MASKS() ^ BALL_CLASS
OBSTACLE_MASK = pymunk.ShapeFilter.ALL_MASKS()

pygame.mixer.init()
click = pygame.mixer.Sound("Sounds_Plinko/ClickSound.mp3")
sound01 = pygame.mixer.Sound("Sounds_Plinko/WinningSound.mp3")
sound01.set_volume(0.2)
sound02 = pygame.mixer.Sound("Sounds_Plinko/SuccessSound.mp3")
sound02.set_volume(0.4)
sound03 = pygame.mixer.Sound("Sounds_Plinko/NiceSound.mp3")
sound03.set_volume(0.6)
sound04 = pygame.mixer.Sound("Sounds_Plinko/FailSound.mp3")
sound04.set_volume(0.8)