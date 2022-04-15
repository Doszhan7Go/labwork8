import pygame 
 
pygame.init() 
 
size,width = 1290 , 650 
 
fps = 60 
 
clock = pygame.time.Clock() 
 
black = (0,0,0) 
white = (255,255,255) 
red = (255,0,0) 
green = (0,255,0) 
blue = (0,0,255) 
 
a = False 
 
s = 3 
 
white_picture = pygame.image.load("Белый цвет.jpg") 
blue_picture = pygame.image.load("Синий цвет.jpg") 
green_picture = pygame.image.load("Зеленый цвет.jpg") 
red_picture = pygame.image.load("Красный цвет.jpg") 
eraser = pygame.image.load("Ластик.jpg") 
 
b = True 
 
screen = pygame.display.set_mode((size,width)) 
pygame.display.set_caption("Paint") 
 
pos,cur = None , None 
 
cl = green 
print(eraser.get_width(),eraser.get_height()) 
x = 0 
y = 0 
while b: 
    for i in pygame.event.get(): 
        if i.type == pygame.QUIT: 
            b = False 
        if i.type == pygame.MOUSEBUTTONDOWN: 
            pos = pygame.mouse.get_pos() 
        if i.type == pygame.MOUSEMOTION: 
            cur = pygame.mouse.get_pos() 
        if pos: 
            pygame.draw.line(screen,cl, pos,cur,s) 
            pos = cur 
        if i.type == pygame.MOUSEBUTTONUP: 
            pos = None 
        elif pos: 
            x = pos[0] 
            y = pos[1] 
            if x >=10 and x <= 38 and y >=10 and y <= 37: 
                cl = red 
            elif x >=45 and x <= 78 and y >=10 and y <= 37: 
                cl = green 
            elif x >= 85 and x <= 113 and y >=10 and y <= 39:  
                cl = blue 
            elif x >=120 and x <= 153 and y >= 10 and y <= 38: 
                cl = white 
            elif x >=10 and x <=192 and y >=10 and y <=37: 
                cl = black 
    pressed = pygame.key.get_pressed() 
 
    if pressed[pygame.K_RIGHT]: 
        s = s+1 
    if pressed[pygame.K_LEFT]: 
        s = s-1 
        # if i.type == pygame.KEYDOWN: 
        #     if i.key == pygame.K_r: 
        #         cl = red 
        #     if i.key == pygame.K_b: 
        #         cl = black 
        #     if i.key == pygame.K_w: 
        #         cl = white 
        #     if i.key == pygame.K_l: 
        #         cl = blue         
 
    screen.blit(red_picture,(10,10)) 
    screen.blit(green_picture,(45,10)) 
    screen.blit(blue_picture,(85,10)) 
    screen.blit(white_picture,(120,10)) 
    screen.blit(eraser,(160 ,10)) 
    pygame.display.flip() 
    clock.tick(fps) 
pygame.quit()