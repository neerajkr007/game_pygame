import pygame
import random

pygame.init()

screenWidth = 500
screenheight = 500
win = pygame.display.set_mode((screenheight, screenWidth))

pygame.display.set_caption('First Game', 'test')

velocity = 5
width = 40
height = 60
x = random.randrange(0, screenWidth - width - 10, 10)
y = random.randrange(0, screenheight - height - 10, 10)
isJump = False
jumpCount = 10

run = True
while run:
    pygame.time.delay(50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

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
            print(jumpCount)
            jumpCount -= 1
        else:
            isJump = False
            jumpCount = 10

    win.fill((0, 0, 0))

    pygame.draw.rect(win, (0, 191, 255), (x, y, width, height))
    pygame.display.update()

pygame.quit()
