#imports
import turtle as t
import random
import math as m
import keyboard as k
import pygame as pg
#initialise engine
t.speed(0)
t.tracer(0,0)
t.pensize(4)
pg.init()
clock=pg.time.Clock()
deltatime=0.05
#initialise map
map = [[2,0,0,0,0,0,2,0],
       [0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0],
       [0,0,0,1,0,0,0,1]]

def findCell(X,Y):
    cx=int(X)
    cy=int(Y)
    if ((X>0 and X<len(map[0])) and (Y>0 and Y<len(map))):
        return map[cx][cy]
    else:
        return 1
#initialise player
#player x
px=4.01
#player y
py=4.01
#player delta x
pdx=0.00
#player delta y
pdy=0.00
#player angle facing
pa=0.001
#player velocity x
xv=0.00
#player velocity y
yv=0.00
#start loop
running = True
while running:
    pdx=(yv*m.sin(pa)+xv*m.cos(pa))*.005*deltatime
    pdy=(yv*m.cos(pa)-xv*m.sin(pa))*.005*deltatime
    #add friction
    xv*=.95
    yv*=.95
    #collision check
    if findCell(px+pdx,py+pdy) <= 0:
        px+=pdx
        py+=pdy
    #handle controls
    if k.is_pressed("w"):yv+=500.0*deltatime
    if k.is_pressed("s"):yv-=500.0*deltatime
    if k.is_pressed("a"):xv-=500.0*deltatime
    if k.is_pressed("d"):xv+=500.0*deltatime
    if k.is_pressed("left"):pa-=2.0*deltatime
    if k.is_pressed("right"):pa+=2.0*deltatime
    if k.is_pressed("esc"):
        running=False
    #clear the screen
    t.clear()
    #start iterating through the lines on the screen
    for i in range(200):
        rx=px
        ry=py
        ra=pa+(i-100.00)*0.005
        rxd=m.sin(ra)
        ryd=m.cos(ra)

        rl=0.00
        D=0.00
        while rl < 20.00:
            try:
                rxD=(float(rxd>0.00)-m.modf(rx)[0])/rxd
                ryD=(float(ryd>0.00)-m.modf(ry)[0])/ryd
            except:
                rxD,ryD = .1,.1
            D=min(rxD,ryD)+0.0001
            rx+=rxd*D
            ry+=ryd*D
            rl+=D
            try:
                #get the cell at the ray's position
                cell=findCell(rx,ry)
                if cell > 0:
                    l=rl
                    rl=20.00
                    #set the colour of the line
                    if cell==2:
                        t.pencolor("red")
                    elif cell==3:
                        t.pencolor("blue")
                    else:
                        t.pencolor("black")
            #oh no your outside the world!
            except:
                l=.001
                rl=20.00
                print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
        #draw the line
        t.teleport((i-100)*4,200./max(l*m.cos(ra-pa),0.001))
        t.setpos((i-100)*4,-200./max(l*m.cos(ra-pa),0.001))
    #update the screen
    t.update()
    #set delta time and tick the clock
    deltatime=clock.tick()/1000.0
#finish the program
t.done()
pg.quit()