import pygame as pg 
import numpy as np 

pg.init()

WINDOW_WIDTH = 1000
WINDOW_HEIGHT  = 600
window=pg.display.set_mode([WINDOW_WIDTH,WINDOW_HEIGHT])

font = pg.font.SysFont("Arial", 24)

#Defining the angle and start speed
teta = 1.75*np.pi/4
v0 = 150

vx = v0*np.cos(teta)
v0y = v0*np.sin(teta)

class Ball:
    def __init__(self, xPos, yPos, vx, v0y, ay):
        self.xPos = xPos
        self.yPos = yPos
        self.vx = vx
        self.v0y = v0y
        self.ay = ay
    
    def drawBall(self):
        pg.draw.circle(window,(255,0,0),(self.xPos,self.yPos),8)

ball = Ball(0,600,vx,v0y,-15)

finished = False
dx = 0.01
t=0
while not finished:
    t+=dx
    for event in pg.event.get():
        if event.type == pg.QUIT:
            finished = True

    window.fill((255,255,255))
    ball.drawBall()
    ball.xPos += dx*ball.vx
    ball.yPos -= dx*(ball.v0y+ball.ay*t)
    pg.time.wait(2)
    pg.display.flip()


    

