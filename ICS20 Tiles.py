#imports pygame
import pygame
import time
from pygame import mixer
import math
import sys
import os
import random

pygame.init()
#making the screen
screen = pygame.display.set_mode((800, 600))
running = True
score = 0
pygame.display.set_caption("ICS20 Catch")
icon = pygame.image.load('clay.png')
pygame.display.set_icon(icon)
clock = pygame.time.Clock()
start = 75350
#player image
playerImg = pygame.image.load('minus-big-symbol.png')
playerX = 270
playerY = 480
player_Xchange = 0
#box image
boxImg1 = pygame.image.load('clay.png')
boxX1 = 270
boxY1 = 0
box_Ychange1 = 0
box_Xchange1 = 0

boxImg2 = pygame.image.load('clay.png')
boxX2 = 500
boxY2 = -400
box_Ychange2 = 0
box_Xchange2 = 0

boxImg3 = pygame.image.load('clay.png')
boxX3 = 20
boxY3 = -600
box_Ychange3 = 0
box_Xchange3 = 0

boxImg4 = pygame.image.load('clay.png')
boxX4 = 700
boxY4 = -800
box_Ychange4 = 0
box_Xchange4 = 0
score = 0
font = pygame.font.Font('freesansbold.ttf', 32)
fonte = pygame.font.Font('freesansbold.ttf', 32)
textX = 10
textY = 10

textX1 = 200
textY1 = 100

textX2 = 200
textY2 = 200

#this is the score
def show_score(x, y):
    score_show = font.render("SCORE : " + str(score), True, (0, 0, 0))
    screen.blit(score_show, (x, y))

#this is the ending text
def ending_text(x, y):
    over_text = fonte.render("GAME OVER, YOUR SCORE IS:" + str(score), True, (255, 255, 255))
    screen.blit(over_text, (x, y))


#this is the player
def player(x, y):
    screen.blit(playerImg, (x, y))

#box #1
def box(x, y):
    screen.blit(boxImg1, (x, y))

#box #2
def box2(x, y):
    screen.blit(boxImg2, (x, y))

#box #3
def box3(x, y):
    screen.blit(boxImg3, (x, y))

#box #4
def box4(x, y):
    screen.blit(boxImg4, (x, y))

#collisions
def iscollision1(boxX1, boxY1, playerX, playerY):
    distance = math.sqrt((math.pow(boxX1 - playerX, 2)) + (math.pow(boxY1 - playerY, 2)))
    if distance < 27:
        return True
    else:
        return False

#collisons
def iscollision2(boxX2, boxY2, playerX, playerY):
    distance = math.sqrt((math.pow(boxX2 - playerX, 2)) + (math.pow(boxY2 - playerY, 2)))
    if distance < 27:
        return True
    else:
        return False

#collision
def iscollision3(boxX3, boxY3, playerX, playerY):
    distance = math.sqrt((math.pow(boxX3 - playerX, 2)) + (math.pow(boxY3 - playerY, 2)))
    if distance < 27:
        return True
    else:
        return False

#collision
def iscollision4(boxX4, boxY4, playerX, playerY):
    distance = math.sqrt((math.pow(boxX4 - playerX, 2)) + (math.pow(boxY4 - playerY, 2)))
    if distance < 27:
        return True
    else:
        return False

#setting the font
font = pygame.font.SysFont("systemboldms", 32)
title_font = pygame.font.SysFont("symbolboldms", 100)
# menu Button
start_box = pygame.Rect(300, 400, 100, 50)
# menu text
button_text = font.render("START", True, (0, 0, 0))
button_text_width = button_text.get_width()
Title_text = title_font.render("ICS20 Catch", True, (254, 255, 255))
Title_text_width = Title_text.get_width()
Menu = True
#menu loop
while Menu == True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            pygame.quit()
            exit
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos

            if start_box.collidepoint(mouse_pos):
                running = True
                Menu = False
                break

    # filling screen
    screen.fill([0, 0, 0])

    # bliting text and shapes
    screen.blit(Title_text, (400 - (Title_text_width / 2), 100))
    pygame.draw.rect(screen, [255, 255, 254], start_box)
    screen.blit(button_text, (350 - (button_text_width / 2), 400))
    pygame.display.flip()
#music
mixer.music.load('circles.wav.mp3')
mixer.music.play(-1, 1)
#game loop
while running == True:
    screen.fill((255, 255, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_Xchange = -2.5
            if event.key == pygame.K_RIGHT:
                player_Xchange = 2.5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player_Xchange = 0

    playerX += player_Xchange
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736
    if boxX1 <= 0:
        box_Xchange1 = 0
        boxY1 += box_Ychange1
    elif boxX1 == boxX1:
        box_Ychange1 = -0.5
        boxY1 -= box_Ychange1
    if boxX2 <= 0:
        box_Xchange2 = 0
        boxY2 += box_Ychange2
    elif boxX2 == boxX2:
        box_Ychange2 = -0.5
        boxY2 -= box_Ychange2
    if boxX3 <= 0:
        box_Xchange3 = 0
        boxY3 += box_Ychange3
    elif boxX3 == boxX3:
        box_Ychange3 = -0.5
        boxY3 -= box_Ychange3
    if boxX4 <= 0:
        box_Xchange4 = 0
        boxY4 += box_Ychange4
    elif boxX4 == boxX4:
        box_Ychange4 = -0.5
        boxY4 -= box_Ychange4
    collision = iscollision1(boxX1, boxY1, playerX, playerY)
    if collision:
        score += 1
        boxX1 = random.randint(0, 650)
        boxY1 = 0
    collision = iscollision2(boxX2, boxY2, playerX, playerY)
    if collision:
        score += 1
        boxX2 = random.randint(0, 650)
        boxY2 = 0
    collision = iscollision3(boxX3, boxY3, playerX, playerY)
    if collision:
        score += 1
        boxX3 = random.randint(0, 650)
        boxY3 = 0
    collision = iscollision4(boxX4, boxY4, playerX, playerY)
    if collision:
        score += 1
        boxX4 = random.randint(0, 650)
        boxY4 = 0
    if boxY1 >= 600:
        boxY1 = 0
        boxX1 = random.randint(0, 650)
    if boxY2 >= 600:
        boxY2 = 0
        boxX2 = random.randint(0, 650)
    if boxY3 >= 600:
        boxY3 = 0
        boxX3 = random.randint(0, 650)
    if boxY4 >= 600:
        boxY4 = 0
        boxX4 = random.randint(0, 650)
    start -= 1
    #ending part of the game
    if start <= 0:
        screen.fill((0, 0, 0))
        ending_text(textX1, textY1)
        boxY1 = 700
        boxY2 = 700
        boxY3 = 700
        boxY4 = 700
        pygame.mixer.quit()
    player(playerX, playerY)
    show_score(textX, textY)
    box(boxX1, boxY1)
    box2(boxX2, boxY2)
    box3(boxX3, boxY3)
    box4(boxX4, boxY4)
    pygame.display.update()
