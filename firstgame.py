import pygame
import random

pygame.init()

screenWidth = 500
screenheight = 500
win = pygame.display.set_mode((screenheight, screenWidth))

pygame.display.set_caption('First Game', 'test')

font = pygame.font.SysFont(None, 20)

velocity = 3
width = 40
height = 60
x = 250
y = 440
isJump = False
jumpCount = 10
backGround = pygame.image.load("bg.jpg").convert()
shipImg = pygame.image.load("shipImg.png").convert()

clock = pygame.time.Clock()

run = True
while run:
    pygame.time.delay(16)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    clock.tick(60)
    fps = int(clock.get_fps())
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a] and x > velocity - 5:
        x -= velocity
    if keys[pygame.K_d] and x < screenWidth - width:
        x += velocity
    if not isJump:
        if keys[pygame.K_w] and y > velocity - 5:
            y -= velocity
        if keys[pygame.K_s] and y < screenheight - height:
            y += velocity
        if keys[pygame.K_SPACE]:
            isJump = True
    else:
        if jumpCount >= -10:
            neg = 1
            if jumpCount < 0:
                neg = -1
            y -= ((jumpCount ** 2) / 2) * neg
            jumpCount -= 1
        else:
            isJump = False
            jumpCount = 10

    win.fill((0, 0, 0))
    win.blit(backGround, [0, 0])
    pygame.draw.rect(win, (0, 191, 255), (x, y, width, height))
    rect = shipImg.get_rect()
    rect.center = (200, 300)
    showFps = font.render('FPS ' + str(fps), True, (255, 0, 0))
    win.blit(showFps, [0, 0])
    win.blit(shipImg, [x, y])
    pygame.display.update()

pygame.quit()






