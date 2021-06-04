import pygame,sys
from time import time
from ctypes import windll
import keyboard

from pygame.locals import *
pygame.init()
x1= time()
FPS =30
fpsClock = pygame.time.Clock()
count=0
words=0
SAMPLE=4 # sampling time
GREEN=(255,0,0)
BLUE=(0,0,255)
BLACK=(0,0,0)
DISPLAYSURF=pygame.display.set_mode((200,40))
SetWindowPos = windll.user32.SetWindowPos
SetWindowPos(pygame.display.get_wm_info()['window'], -1, 100, 100, 0, 0, 0x0001)
fontObj= pygame.font.Font('freesansbold.ttf',20)

def inc(data):
    global count
    count=count+1
    #print(count)


def draw(speed):
    s=str(speed)
    if speed ==0:
        s='0'

    textSurfaceObj=fontObj.render(s,True, GREEN , BLACK)
    textRectObj = textSurfaceObj.get_rect()
    textRectObj.center = (100,20)

    DISPLAYSURF.blit(textSurfaceObj,textRectObj)

dx=0



while True:
    x2 = time()
    #print(keyboard.on_press)
    dx=x2-x1   
    for event in pygame.event.get():
       
       if event.type == QUIT:
            pygame.quit()
            sys.exit()
         
    keyboard.on_release(inc,suppress=True)
    if count >=5:
        #print("dec")
        count =0
        words = words +1
        #print(words)
    if dx >= SAMPLE :
        DISPLAYSURF.fill(BLACK)
        speed=(words/SAMPLE)*60
        words=0
        x1=x2
        #print(speed)
        draw(speed)       


        
    pygame.display.update()
    fpsClock.tick(FPS)






