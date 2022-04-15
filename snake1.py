import pygame
from random import randrange

res = 700
size = 50
line = (50,50,50)

x, y = randrange(0,res,size), randrange(0,res, size)
apple = randrange(0,res, size), randrange(0, res, size)

dirs = {'W': True,'S': True,'A': True,'D': True}

lenght = 1
snake = [(x,y)]
score = 0
dx,dy = 0,0
fps = 5

pygame.init()
sc = pygame.display.set_mode([res,res])
clock = pygame.time.Clock()
font_score = pygame.font.SysFont('Arial',26, bold = True)
font_end = pygame.font.SysFont('Arial',66, bold = True)

while True:
    sc.fill(pygame.Color('black'))
    [(pygame.draw.rect(sc,pygame.Color('green'),( i , j , size -2 , size- 2))) for i ,j in snake]
    pygame.draw.rect(sc,pygame.Color('red'),(*apple,size,size))

    render_score = font_score.render(f'SCORE: {score}',1, pygame.Color('blue'))
    sc.blit(render_score,(5,5))

    x+= dx * size
    y+= dy * size
    snake.append((x,y))
    snake = snake[-lenght:]

    if snake[-1] == apple:
        apple = randrange(0,res,size),randrange(0,res,size)
        lenght += 1
        score+=1
        if lenght % 5 == 0:
            fps+= 1   
    if x < 0 or x > res - size or y < 0 or y > res - size:
        while True:
            render_end = font_end.render('GAME OVER',1,pygame.Color('blue'))
            sc.blit(render_end,(res // 2 -200, res//3))
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()

    if len(snake) != len(set(snake)):
        break

    pygame.display.flip()
    clock.tick(fps)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()


    key = pygame.key.get_pressed()
    if key[pygame.K_w] and dirs['W']:
        dx,dy = 0,-1
        dirs = {'W': True,'S': False,'A': True,'D': True}
    if key[pygame.K_s] and dirs['S']:
        dx,dy = 0,1
        dirs = {'W': False,'S': True,'A': True,'D': True}
    if key[pygame.K_a] and dirs['A']:
        dx,dy = -1, 0
        dirs = {'W': True,'S': True,'A': True,'D': False}
    if key[pygame.K_d] and dirs['D']:
        dx,dy = 1,0
        dirs = {'W': True,'S': True,'A': False,'D': True}
    
    

def drawGrid():
    for x in range(0, res, size):
        for y in range(0, res, size):
            rect = pygame.Rect(x, y, size, size)
            pygame.draw.rect(sc,line, rect, 1)