import sys

import pygame

pygame.init()# bắt đầu khởi tạo màn hình

clock= pygame.time.Clock()

speed = [3,15]
white= (255,255,255)
black= (0,225,255)
green=(255,0,222)
size =(w,h)=(320,240)

screen= pygame.display.set_mode(size)

ball = pygame.image.load("ball-1.png")
ball = pygame.transform.scale(ball,(30,30))
ballrect =ball.get_rect()

while True:
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            sys.exit()
    ballrect = ballrect.move(speed)
    if ballrect.left<0 or ballrect.right > ballrect.width:
        speed[0]= -speed[0]
    if ballrect.top <0 or ballrect.bottom> ballrect.height:
        speed[1]= -speed[1]

    screen.fill(white)
    screen.blit(ball,ballrect)
    pygame.display.update()
    clock.tick(60)
