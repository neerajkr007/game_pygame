import pygame

pygame.init()

# screen parameters

screenWidth = 500
screenheight = 500
win = pygame.display.set_mode((screenheight, screenWidth))
pygame.display.set_caption('First Game', 'test')

# font

font = pygame.font.SysFont(None, 20)


class Ship(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.velocity_ship = 3

    def draw_ship(self, win):
        shipImg = pygame.image.load("ship.png")
        pygame.draw.rect(win, (0, 191, 255), (self.x, self.y, self.width, self.height), -2)
        rect = shipImg.get_rect()
        rect.center = (50, 30)
        win.blit(shipImg, [playerShip.x - 11, playerShip.y - 3])


class Bullet(object):
    def __init__(self, x, y, radius, color):
        self.x = playerShip.x + 22
        self.y = playerShip.y
        self.radius = radius
        self.color = color
        self.vel = 3

    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)


bullets = []

clock = pygame.time.Clock()

# background image is loaded
backGround = pygame.image.load("bg.jpg").convert()


def screendraw(win):
    win.blit(backGround, [0, 0])
    Fps(win)
    playerShip.draw_ship(win)
    for bullet in bullets:
        bullet.draw(win)
    pygame.display.update()


def Fps(win):
    showFps = font.render('FPS ' + str(fps), True, (255, 0, 0))
    win.blit(showFps, [0, 0])

firetime = 0
run = True
playerShip = Ship(250, 440, 40, 50)

# main loop

while run:
    pygame.time.delay(16)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    for bullet in bullets:
        if (bullet.y <= playerShip.y) and (bullet.y > 0):
            bullet.y -= bullet.vel
        else:
            bullets.pop(bullets.index(bullet))

    clock.tick(60)
    if firetime > 0:
        firetime += 1
    if firetime >= 15:
        firetime = 0
    fps = int(clock.get_fps())
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a] and playerShip.x > playerShip.velocity_ship - 5:
        playerShip.x -= playerShip.velocity_ship
    if keys[pygame.K_d] and playerShip.x < screenWidth - playerShip.width:
        playerShip.x += playerShip.velocity_ship
    if keys[pygame.K_w] and playerShip.y > playerShip.velocity_ship - 5:
        playerShip.y -= playerShip.velocity_ship
    if keys[pygame.K_s] and playerShip.y < screenheight - playerShip.height:
        playerShip.y += playerShip.velocity_ship
    v = playerShip.y
    if keys[pygame.K_SPACE] and firetime == 0:
        if len(bullets) < 6:
            bullets.append(Bullet(round(playerShip.x + playerShip.width //2), round(playerShip.y), 6, (255, 0, 0)))
        firetime = 1

    screendraw(win)
    # win.fill((0, 0, 0))
pygame.quit()
