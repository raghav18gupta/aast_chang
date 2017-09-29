import pygame
import time
import random
pygame.init()
pygame.font.init()

#colors
black = 0, 0, 0
white = 255,255,255
red   = 200,0,0
green = 0,200,0
blue  = 0,0,200
yellow=200,200,0
bright_red   = 255,0,0
bright_green = 0,255,0
bright_blue  = 0,0,255
bright_yellow= 255,255,0

#screen setup
size  = width, height = 1100, 670
midpoint = 550,335
gameDisplay = pygame.display.set_mode(size)
gameIcon = pygame.image.load('imgs/green.png')
clock = pygame.time.Clock()
lineimg=pygame.image.load("imgs/lines.png")

#gotis :)
r_goti = [pygame.image.load("imgs/red.png")]*4
g_goti = [pygame.image.load("imgs/green.png")]*4
b_goti = [pygame.image.load("imgs/blue.png")]*4
y_goti = [pygame.image.load("imgs/yellow.png")]*4

#seeds
b_seeds = pygame.image.load("imgs/back.png")
f_seeds = pygame.image.load("imgs/front.png")

#game constant stuffs
fillsequence = [(30,30),(60,60),(30,60),(60,30),(0,0),(90,90),(0,90),(90,0),(90,3),(0,60),(90,60),(0,30)]
turnlist=rTurn,yTurn,bTurn,gTurn=list(range(0,4))
roww = [(9,9)  ,(143,9)  ,(277,9)  ,(411,9)  ,(545,9)
       ,(9,143),(143,143),(277,143),(411,143),(545,143)
       ,(9,277),(143,277),(277,277),(411,277),(545,277)
       ,(9,410),(143,410),(277,410),(411,410),(545,410)
       ,(9,542),(143,542),(277,542),(411,542),(545,542)]

#global variables
isclick = False

#paths
rpath=[2,1,0,5,10,15,20,21,22,23,24,19,14,9,4,3,8,13,18,17,16,11,6,7,12]
ypath=[10,15,20,21,22,23,24,19,14,9,4,3,2,1,0,5,6,7,8,13,18,17,16,11,12]
bpath=[22,23,24,19,14,9,4,3,2,1,0,5,10,15,20,21,16,11,6,7,8,13,18,17,12]
gpath=[14,9,4,3,2,1,0,5,10,15,20,21,22,23,24,19,18,17,16,11,6,7,8,13,12]

def putgoti(x,y):
    return (x[0]+y[0],x[1]+y[1])

#button
def button(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac,(x,y,w,h))
        if click[0] == 1 and action != None:
            action()
    else:
        pygame.draw.rect(gameDisplay, ic,(x,y,w,h))
    smallText = pygame.font.Font("Fonts/comic.ttf",30)
    textSurf, textRect = text_objects(msg, smallText,black)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    gameDisplay.blit(textSurf, textRect)

def quitgame():
    pygame.quit()
    quit()

def text_objects(text, font, colors):
    textSurface = font.render(text, True, colors)
    return textSurface, textSurface.get_rect()

def color_utility(numb):
    if numb==0:
        return red, 'Red', red
    elif numb==1:
        return yellow, 'Yellow', yellow
    elif numb==2:
        return blue, 'Blue', blue
    elif numb==3:
        return green, 'Green', green

def main_menu():
    menu = True
    while menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitgame()
        gameDisplay.fill(black)
        largeText = pygame.font.Font("Fonts/chalk.ttf",80)
        TextSurf, TextRect = text_objects("Aast Channg", largeText,white)
        TextRect.center = ((width/2),(height/3))
        gameDisplay.blit(TextSurf, TextRect)
        # def button(msg,x,y,w,h,ic,ac,action=None
        button("Play!",260,450,170,50,green,bright_green,toss)
        button("Quit",690,450,159,50,red,bright_red,quitgame)

        pygame.display.update()
        clock.tick(15)

def begin_game(whowon):
    RPath,YPath,BPath,GPath=0,0,0,0
    r_trace   = [0]*4
    y_trace   = [0]*4
    b_trace   = [0]*4
    g_trace   = [0]*4
    cell_trace= [0]*24
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitgame()
        gameDisplay.fill(black)
        gameDisplay.blit(lineimg,(0,0))
        gameDisplay.blit(b_goti[0],putgoti(roww[bpath[BPath]],fillsequence[cell_trace[bpath[BPath]]]))
        cell_trace[bpath[BPath]]+=1
        gameDisplay.blit(b_goti[1],putgoti(roww[bpath[BPath]],fillsequence[cell_trace[bpath[BPath]]]))
        cell_trace[bpath[BPath]]+=1
        gameDisplay.blit(b_goti[2],putgoti(roww[bpath[BPath]],fillsequence[cell_trace[bpath[BPath]]]))
        cell_trace[bpath[BPath]]+=1
        gameDisplay.blit(b_goti[3],putgoti(roww[bpath[BPath]],fillsequence[cell_trace[bpath[BPath]]]))
        cell_trace[bpath[BPath]]+=1
        gameDisplay.blit(r_goti[0],putgoti(roww[rpath[RPath]],fillsequence[cell_trace[rpath[RPath]]]))
        cell_trace[rpath[RPath]]+=1
        gameDisplay.blit(r_goti[1],putgoti(roww[rpath[RPath]],fillsequence[cell_trace[rpath[RPath]]]))
        cell_trace[rpath[RPath]]+=1
        gameDisplay.blit(r_goti[2],putgoti(roww[rpath[RPath]],fillsequence[cell_trace[rpath[RPath]]]))
        cell_trace[rpath[RPath]]+=1
        gameDisplay.blit(r_goti[3],putgoti(roww[rpath[RPath]],fillsequence[cell_trace[rpath[RPath]]]))
        cell_trace[rpath[RPath]]+=1
        gameDisplay.blit(y_goti[0],putgoti(roww[ypath[YPath]],fillsequence[cell_trace[ypath[YPath]]]))
        cell_trace[ypath[YPath]]+=1
        gameDisplay.blit(y_goti[1],putgoti(roww[ypath[YPath]],fillsequence[cell_trace[ypath[YPath]]]))
        cell_trace[ypath[YPath]]+=1
        gameDisplay.blit(y_goti[2],putgoti(roww[ypath[YPath]],fillsequence[cell_trace[ypath[YPath]]]))
        cell_trace[ypath[YPath]]+=1
        gameDisplay.blit(y_goti[3],putgoti(roww[ypath[YPath]],fillsequence[cell_trace[ypath[YPath]]]))
        cell_trace[ypath[YPath]]+=1
        gameDisplay.blit(g_goti[0],putgoti(roww[gpath[GPath]],fillsequence[cell_trace[gpath[GPath]]]))
        cell_trace[gpath[GPath]]+=1
        gameDisplay.blit(g_goti[1],putgoti(roww[gpath[GPath]],fillsequence[cell_trace[gpath[GPath]]]))
        cell_trace[gpath[GPath]]+=1
        gameDisplay.blit(g_goti[2],putgoti(roww[gpath[GPath]],fillsequence[cell_trace[gpath[GPath]]]))
        cell_trace[gpath[GPath]]+=1
        gameDisplay.blit(g_goti[3],putgoti(roww[gpath[GPath]],fillsequence[cell_trace[gpath[GPath]]]))
        cell_trace[gpath[GPath]]+=1
        pygame.display.update()

        turn_button=color_utility(whowon)
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quitgame()
            # def button(msg,x,y,w,h,ic,ac,action=None
            button(str(turn_button[1])+"'s Turn",700,20,300,50,turn_button[2],turn_button[2],chiye)
            pygame.display.update()
        # time.sleep(4)


def chiye():
    inst_turn = list(map(lambda x: random.choice(x), [[0, 1]]*4))
    for i in range(4):
        if inst_turn[i] is 0:
            gameDisplay.blit(b_seeds,(700 + (40 if i is 1 or 3 else 0), 100 + (50 if i is 2 or 3 else 0)))
        elif inst_turn[i] is 1:
            gameDisplay.blit(f_seeds,(700 + (40 if i is 1 or 3 else 0), 100 + (50 if i is 2 or 3 else 0)))
    return


def whoseturnfirst(whowon):
    fillcolor,tring,hhh=color_utility(whowon)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitgame()
            if event.type == pygame.MOUSEBUTTONDOWN:
                begin_game(whowon)
        gameDisplay.fill(fillcolor)
        tosstext = pygame.font.Font("Fonts/chalk.ttf",140)
        tossSurf, tossRect = text_objects(tring+"'s Turn", tosstext,black)
        tossRect.center = ((width/2),(height/2))
        gameDisplay.blit(tossSurf, tossRect)
        pygame.display.update()
        clock.tick(15)

def toss():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitgame()
            if event.type == pygame.MOUSEBUTTONDOWN:
                whoseturnfirst(random.choice(turnlist))
        gameDisplay.fill(black)
        pygame.draw.polygon(gameDisplay,bright_red,[[0,0],[width,0],midpoint],0)
        pygame.draw.polygon(gameDisplay,bright_yellow,[[0,0],[0,height],midpoint],0)
        pygame.draw.polygon(gameDisplay,bright_green,[[width,0],[width,height],midpoint],0)
        pygame.draw.polygon(gameDisplay,bright_blue,[[0,height],[width,height],midpoint],0)
        tosstext = pygame.font.Font("Fonts/chalk.ttf",180)
        tossSurf, tossRect = text_objects("Let's Toss!!!", tosstext,black)
        tossRect.center = ((width/2),(height/2))
        gameDisplay.blit(tossSurf, tossRect)
        pygame.display.update()
        clock.tick(15)

main_menu()
