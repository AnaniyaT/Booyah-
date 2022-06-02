import pygame
import random
pygame.init()

width = 600
height = 600
black = (0,0,0)
white = (245,245,245)
grey = (150,150,150)
blue = (0,0,200)
green = (0,200,0)
fps = 60
vel = 3

midheight = 60
lowheight = 30*random.randint(5,14)
upheight = height-lowheight-midheight
xval = 500

screen = pygame.display.set_mode((width,height))
pygame.display.set_caption ("Booyah!")
background1 = pygame.Rect (0,0, width, height)
upline = pygame.Rect (300,0, 5, upheight)
midline = pygame.Rect (300, upheight, 5,midheight)
lowline = pygame.Rect (300,upheight+midheight ,5, lowheight)
font1 = pygame.font.Font(None, 100)
losetext = font1.render ("You lost! lol", True, black)

def drawscreen(xval,lowheight,upheight, linepixel,linepixels,text,frontpixel,play):
    pygame.draw.rect(screen,white,background1)
    if play:
        upheight = height-lowheight-midheight
        upline = pygame.Rect (xval,0, 5, upheight)
        lowline = pygame.Rect (xval,upheight+midheight ,5, lowheight)
        midline = pygame.Rect (xval,upheight,5,upheight)
        pygame.draw.rect(screen,grey,upline)
        pygame.draw.rect(screen,white,midline)
        pygame.draw.rect(screen,grey,lowline)
        pygame.draw.rect(screen,black,frontpixel)
        for linepixel in linepixels:
            pygame.draw.rect(screen,black,linepixel)
        screen.blit(text, (560,10))
    else:
        screen.blit(losetext,(100,100))
    pygame.display.update()
def handleline (linepixel,linepixels,score,lowheight,upheight,xval,font,play):
    clock = pygame.time.Clock()
    midline = pygame.Rect (xval, upheight, 5,midheight)
    for linepixel in linepixels:
        linepixel.x -= vel
        if linepixel.x <-1:
            linepixels.remove(linepixel)
    if not play:
        clock.tick(2)
        for linepixel in linepixels:
            linepixels.remove(linepixel)
    pygame.display.update()

def main(xval,lowheight,upheight):
    run = True
    v=0.1
    acc = 0.2
    clock = pygame.time.Clock()
    linepixels = []
    linepixely = 300
    fall = True
    play = True
    pause = True
    score = "0"
    font = pygame.font.Font(None, 40)
    
    while run:
        clock.tick(fps)
        
        if xval < -5:
            lowheight = 30*random.randint(4,15)
            upheight = height-lowheight -midheight
            xval = 600
    
        for event in pygame.event.get():
            
            if event.type == 771:
                fall = False
                if pause:
                    pause = False
                if not play:
                    pause = True   
                    play = True
                    xval = 500
                    main(xval,lowheight,upheight)
            if event.type == 769:
                fall = True
            if event.type == pygame.QUIT:
                run = False
                 
        if not pause:
            xval -= vel
            if fall:
                v+=acc
                linepixely += v
            else:
                v-=acc
                linepixely +=v
        if not play:
            linepixely = 300
        frontpixel = pygame.Rect(200, linepixely,2,5)
        midline = pygame.Rect (xval,upheight,1,midheight)
        upline = pygame.Rect (xval,0, 5, upheight)
        lowline = pygame.Rect (xval,upheight+midheight ,5, lowheight)
        if midline.colliderect(frontpixel):
            score = str((int(score)+1))
            print ("yeah", score)
        if upline.colliderect(frontpixel) or lowline.colliderect(frontpixel) or frontpixel.y < -1 or frontpixel.y > 596:
            print ("you lose! ha ha") 
            play = False
        linepixel = pygame.Rect (200,linepixely,5,5)
        linepixels.append(linepixel)
        handleline(linepixel,linepixels,score,lowheight,upheight,xval,font,play)
        text = font.render (score, True, black)
        drawscreen(xval,lowheight,upheight, linepixel,linepixels,text,frontpixel,play)
        
main(xval,lowheight,upheight)