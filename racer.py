import random
import sys
import time
import pygame

pygame.init()

FPS = 60
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
STEP = 5
ENEMTY_STEP = 10

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

SCORE  = 0

clock = pygame.time.Clock()

score_font = pygame.font.SysFont("Verdana", 20)

SURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Street Racer")

bg = pygame.image.load("AnimatedStreet.png")
global speed1
speed1=3     #скорость машины
global speed2
speed2=5     #скорость монет

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    def update(self):
        self.rect.move_ip(0, speed1)
        if(self.rect.bottom > SCREEN_HEIGHT):
            self.top = 0
            self.rect.center = (random.randint(30, 350), 0)

    def draw(self, surface):
        surface.blit(self.image, self.rect)

class Coin(pygame.sprite.Sprite):
    def __init__ (self):
        super().__init__()
        self.coin= pygame.image.load("coin3.png") #берем пнг монетки
        self.coin=pygame.transform.scale(self.coin,(30,30))    #изменяем размер монетки
        self.rect = self.coin.get_rect() #размеры коина
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)   #местоположение начала монеты
    def draw(self,surface):
        surface.blit(self.coin,self.rect)  #рисуем
    
    def update(self):
        self.rect.move_ip(0,speed2) #движение монетки

        if(self.rect.bottom > SCREEN_HEIGHT):# если он выходит за пределы карты то монетка снова появляется в начале карты
            self.rect.center = (random.randint(30, 350), 0)
    def back(self):
        self.rect.center = (random.randint(30, 350), 0) # при соприкасаний с нашей машиной, переводит его в начало карты ( монетку) 


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)

    def update(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 0:
            if pressed_keys[pygame.K_LEFT]:
                self.rect.move_ip(-STEP, 0)

        if self.rect.right < SCREEN_WIDTH:
            if pressed_keys[pygame.K_RIGHT]:
                self.rect.move_ip(STEP, 0)

    def draw(self, surface):
        surface.blit(self.image, self.rect)
plus=2  # надбавка к скорости машины (enemy)
z=10
c=20
SCORE=0
P1 = Player()
E1 = Enemy()
C1=Coin()
enemies = pygame.sprite.Group()
enemies.add(E1)

point = pygame.sprite.Group()
point.add(C1)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    P1.update()
    E1.update()
    C1.update()

    if pygame.sprite.spritecollideany(P1, enemies): #в случае столкновения нашего и enemy машинок игра прекращается 
        pygame.quit()
        sys.exit()
    if pygame.sprite.spritecollideany(P1, point): #в случае столкновения машины и coin нам начисляется рандомное очко в размере от 1 до 5 
        SCORE+=random.randint(1,5)
        C1.back() #монетка идет в начало карты
    SURF.blit(bg, (0, 0))
    E1.draw(SURF)
    P1.draw(SURF)
    C1.draw(SURF)
    score_img = score_font.render(str(SCORE), True, BLACK)
    SURF.blit(score_img, (10, 10))
    if SCORE in range(z,c): # если score в радиусе (z,c) то добавляется скорость, тоесть каждые 10 очков скорость увеличивается
        z+=10
        c+=10
        speed1+=plus
    pygame.display.update()
    clock.tick(FPS)