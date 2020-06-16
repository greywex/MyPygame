import pygame
import math
import random
from pygame.locals import (K_UP, K_DOWN, K_LEFT, K_RIGHT, KEYDOWN, QUIT, K_ESCAPE)

# DISCLAIMER- pygame was a topic not discussed during the quarter, all uses of-
# pygame imports were learned from third parties (though not ALL copied directly from
# third party sources. All icons (.png files) were obtained through flaticon.com
# robot.png and octopus.png author : Freepik, laser.png author: Those Icons, ufo.png author: Icongeek26

# initializes pygame(enables package)
pygame.init()

# in tializes screen
screen = pygame.display.set_mode((900, 900))
# starts the countdown upon opening timer (idea from stackoverflow.com from user "Sloth"
timer = pygame.time.get_ticks()

# Title of game
pygame.display.set_caption("Grey's Custom Game")

# player code from freeCodeCamp.org
PlayerImage = pygame.image.load('ufo1.png')
playerX = 400
playerY = 750
playerX_change = 0
playerY_change = 0

# enemy somewhat from freeCodeCamp.org (they used a much more clever way to blit several enemies onto one screen)
Enemy1Image = (pygame.image.load('robots.png'))
enemy1X = (random.randint(0, 836))
enemy1Y = (random.randint(0, 100))
enemy1X_change = 0
enemy1Y_change = 0

Enemy2Image = (pygame.image.load('octopus.png'))
enemy2X = (random.randint(0, 836))
enemy2Y = (random.randint(0, 100))
enemy2X_change = 0
enemy2Y_change = 0

# laser
# ready state means you cannot see laser
# fire state means laser is moving
# somewhat from freecodecamp.org
laserImage = pygame.image.load('laser.png')
laserX = 0
laserY = playerY
laser1X_change = 0
laserY_change = 1
laser_state = "ready"


def shoot(x, y):
    global laser_state
    laser_state = "fire"
    screen.blit(laserImage, (x + 16, y + 10))


# idea found online, hit system from function modified for game
def hit(enemy1X, ememy1Y, laserX, laserY):
    distance = math.sqrt((math.pow(enemy1X - laserX, 2)) + (math.pow(enemy1Y - laserY, 2)))
    if distance < 90:
        return True


def hit2(enemy2X, ememy2Y, laserX, laserY):
    distance2 = math.sqrt((math.pow(enemy2X - laserX, 2)) + (math.pow(enemy2Y - laserY, 2)))
    if distance2 < 120:
        return True


# drawing players and enemies (drawn on screen) general idea from pygame.org
def player(x, y):
    screen.blit(PlayerImage, (x, y))


def enemy(x, y):
    screen.blit(Enemy1Image, (x, y))


def enemy2(x, y):
    screen.blit(Enemy2Image, (x, y))


# my complete custom coding, changes color of screen while the game progresses
def colorchange():
    if counter <= 4:
        screen.fill((3, 53, 252))
    if counter >= 5 and counter < 9:
        screen.fill((random.randint(0, 10), random.randint(10, 20), random.randint(20, 30)))
    if counter == 9:
        screen.fill((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))


# score of game
counter = 0

# keeps game running, HEAVY modification of player movement from freecodecamp.org
# custom code for enemy movement
# keybind support found from pygame.org and freecodecamp, with custom modifications to inputs
running = True
while running:
    colorchange()
    for event in pygame.event.get():
        # Escape to quit option
        if event.type == pygame.KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
        elif event.type == pygame.QUIT:
            running = False
        # player movement
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -0.3
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.3
            if event.key == pygame.K_UP:
                playerY_change = -0.3
            if event.key == pygame.K_DOWN:
                playerY_change = 0.3
            # player shoot from freecodecamp
            if event.key == pygame.K_SPACE:
                if laser_state is "ready":
                    laserX = playerX
                    shoot(laserX, laserY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                playerY_change = 0

        # enemy movement
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                enemy1X_change = random.uniform(-0.7, 0.7)
            if event.key == pygame.K_RIGHT:
                enemy1X_change = random.uniform(-0.7, 0.7)
            if event.key == pygame.K_UP:
                enemy1Y_change = random.uniform(-0.7, 0.7)
            if event.key == pygame.K_DOWN:
                enemy1Y_change = random.uniform(-0.7, 0.7)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                enemy2X_change = random.uniform(-0.7, 0.7)
            if event.key == pygame.K_RIGHT:
                enemy2X_change = random.uniform(-0.7, 0.7)
            if event.key == pygame.K_UP:
                enemy2Y_change = random.uniform(-0.7, 0.7)
            if event.key == pygame.K_DOWN:
                enemy2Y_change = random.uniform(-0.7, 0.7)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                playerY_change = 0
        # hit from freecodecamp with modification (counter, printing string)

        kill2 = hit2(enemy2X, enemy2Y, laserY, laserX)
        if kill2:
            laserY = playerY
            laser_state = "ready"
            counter += 1
            if counter == 10:
                running = False
                print("You Win! GAME OVER")
            enemy2X = random.randint(0, 810)
            enemy2Y = random.randint(0, 100)

        kill = hit(enemy1X, enemy1Y, laserX, laserY)
        if kill:
            laserY = playerY
            laser_state = "ready"
            counter += 1
            if counter == 10:
                running = False
                print("You Win! GAME OVER")
            enemy1X = random.randint(0, 810)
            enemy1Y = random.randint(0, 100)
        # timer mentioned and credited above, printing and ending game is custom.
        second = (pygame.time.get_ticks() - timer) / 1000
        if second > 30:
            running = False
            print("TIMES UP! YOU LOSE!")

    # show score, from stackoverflow.com anonymous user along with custom code to use a system font and to draw it on screen

    font = pygame.font.SysFont('Agency FB', 74)
    score = font.render(str(counter), 1, (255, 255, 255))
    screen.blit(score, (10, 10))

    # allows player position to be updated
    playerX += playerX_change
    playerY += playerY_change
    enemy1X += enemy1X_change
    enemy1Y += enemy1Y_change
    enemy2Y += enemy2Y_change
    enemy2X += enemy2X_change
    # keeps player and enemy on screen, modified from stackoverflow.com
    if playerX < 0:
        playerX = 0
    elif playerX >= 836:
        playerX = 836
    if playerY < 0:
        playerY = 0
    if playerY > 836:
        playerY = 836

    if enemy1X < 0:
        enemy1X = 0
    elif enemy1X >= 810:
        enemy1X = 810
    if enemy1Y < 0:
        enemy1Y = 0
    if enemy1Y > 836:
        enemy1Y = 836

    if enemy2Y < 0:
        enemy2Y = 0
    if enemy2Y > 836:
        enemy2Y = 836
    if enemy2X < 0:
        enemy2X = 0
    elif enemy2X >= 810:
        enemy2X = 810

    # laser firing from freecodecamp.com
    if laserY <= 0:
        laserY = playerY
        laser_state = "ready"
    if laser_state is "fire":
        shoot(laserX, laserY)
        laserY -= laserY_change
    # keeps enemy on screen
    player(playerX, playerY)
    enemy(enemy1X, enemy1Y)
    enemy2(enemy2X, enemy2Y)
    pygame.display.update()
