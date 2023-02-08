import pygame

pygame.init()
win = pygame.display.set_mode((911, 512))
pygame.display.set_caption("Движения Марио")
walk_Right = [pygame.image.load('marioImages/mRight_Move.png'),
              pygame.image.load('marioImages/mRight_Move1.png'),
              pygame.image.load('marioImages/mRight_Move2.png')]
walk_Left = [pygame.image.load('marioImages/mLeft_Move.png'),
              pygame.image.load('marioImages/mLeft_Move1.png'),
              pygame.image.load('marioImages/mLeft_Move2.png')]
char = pygame.image.load('marioImages/mRight.png')

bg = pygame.image.load('marioImages/fon_bg_mario.png')
clock = pygame.time.Clock()


class player (object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.isJump = False
        self.left = False
        self.right = False
        self.walkCount = 0
        self.jumpCount = 10
        self.standing = True

    def draw(self, win):
        if self.walkCount + 1 >= 30:
            self.walkCount = 0

        if not(self.standing):
            if self.left:
                win.blit(walk_Left[self.walkCount//10], (self.x, self.y))
                self.walkCount += 1
            elif self.right:
                win.blit(walk_Right[self.walkCount//10], (self.x, self.y))
                self.walkCount += 1
        else:
            if self.right:
                win.blit(walk_Right[0], (self.x, self.y))
            else:
                win.blit(walk_Left[0], (self.x, self.y))


class projectile(object):
    def __init__(self, x, y, radius, color, facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 8 * facing

    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)


class enemy(object):
    walkRight = [pygame.image.load('Game/R1E.png'), pygame.image.load('Game/R2E.png'), pygame.image.load('Game/R3E.png'),
                 pygame.image.load('Game/R4E.png'), pygame.image.load('Game/R5E.png'), pygame.image.load('Game/R6E.png'),
                 pygame.image.load('Game/R7E.png'), pygame.image.load('Game/R8E.png'), pygame.image.load('Game/R9E.png'),
                 pygame.image.load('Game/R10E.png'), pygame.image.load('Game/R11E.png')]
    walkLeft = [pygame.image.load('Game/L1E.png'), pygame.image.load('Game/L2E.png'), pygame.image.load('Game/L3E.png'),
                pygame.image.load('Game/L4E.png'), pygame.image.load('Game/L5E.png'), pygame.image.load('Game/L6E.png'),
                pygame.image.load('Game/L7E.png'), pygame.image.load('Game/L8E.png'), pygame.image.load('Game/L9E.png'),
                pygame.image.load('Game/L10E.png'), pygame.image.load('Game/L11E.png')]


def redrawGameWindow():
    win.blit(bg, (0, 0))
    man.draw(win)
    for bullet in bullets:
        bullet.draw(win)
    pygame.display.update()

    """Main loop"""
man = player(40, 385, 43, 79)
bullets = []
run = True
while run:
    clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    for bullet in bullets:
        if bullet.x < 911 and bullet.x > 0 :
            bullet.x += bullet.vel
        else:
            bullets.pop(bullets.index(bullet))
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        if man.left:
            facing = -1
        else:
            facing = 1
        if len(bullets) < 10:
            bullets.append(projectile(round(man.x + man.width//2),
                                      round(man.y + man.height//2), 6, (0, 0, 0), facing))
    if keys[pygame.K_LEFT] and man.x > 3:
        man.x -= man.vel
        man.left = True
        man.right = False
        man.standing = False
    elif keys[pygame.K_RIGHT] and man.x < 911 - man.width:
        man.x += man.vel
        man.left = False
        man.right = True
        man.standing = False
    else:
        man.standing = True
        man.walkCount = 0
    if not man.isJump:
        if keys[pygame.K_DOWN] and man.y < 512 - man.height:
            man.y += man.vel
        if keys[pygame.K_UP] and man.y > 3:
            man.y -= man.vel
        if keys[pygame.K_RCTRL]:
            man.isJump = True
    else:
        if man.jumpCount >= -10:
            if man.jumpCount < 0:
                man.y += (man.jumpCount ** 2) / 2
            else:
                man.y -= (man.jumpCount**2) / 2
            man.jumpCount -= 1
        else:
            man.isJump = False
            man.jumpCount = 10
    redrawGameWindow()
