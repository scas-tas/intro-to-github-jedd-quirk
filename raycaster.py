import turtle as t
import random
import math as m
import numpy as n
import keyboard as k
import pygame as pg

t.speed(0)
t.tracer(0,0)
t.pensize(4)
pg.init()
clock = pg.time.Clock()
deltatime=0.05
map = [[1,1,1,1,1,1,1,1],
       [1,0,0,0,0,0,0,1],
       [1,0,0,2,0,0,0,1],
       [1,0,0,0,0,0,0,1],
       [1,0,0,0,0,0,0,1],
       [1,0,0,0,0,2,0,1],
       [1,0,0,0,0,0,0,1],
       [1,1,1,1,1,1,1,1]]

def findCell(X,Y):
    return map[int(X)][int(Y)]
px=4.01
py=4.01
pdx=0.00
pdy=0.00
pa=0.001
xv=0.00
yv=0.00
running = True
while running:
    pdx=(yv*m.sin(pa)+xv*m.cos(pa))*.005*deltatime
    pdy=(yv*m.cos(pa)-xv*m.sin(pa))*.005*deltatime
    xv*=.95
    yv*=.95
    if findCell(px+pdx,py+pdy) <= 0:
        px+=pdx
        py+=pdy
    if k.is_pressed("w"):yv+=500.0*deltatime
    if k.is_pressed("s"):yv-=500.0*deltatime
    if k.is_pressed("a"):xv-=500.0*deltatime
    if k.is_pressed("d"):xv+=500.0*deltatime
    if k.is_pressed("left"):pa-=2.0*deltatime
    if k.is_pressed("right"):pa+=2.0*deltatime
    if k.is_pressed("esc"):
        px=4.01
        py=4.01
        xv=0.00
        yv=0.00
        pdx=0.00
        pdy=0.00
    t.clear()

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
                cell=findCell(rx,ry)
                if cell > 0:
                    l=rl
                    rl=20.00
                    if cell==2:
                        t.pencolor("red")
                    else:
                        t.pencolor("black")
            except:
                l=.001
                rl=20.00
                print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
        t.teleport((i-100)*4,200./max(l*m.cos(ra-pa),0.001))
        t.setpos((i-100)*4,-200./max(l*m.cos(ra-pa),0.001))
    t.update()
    deltatime=clock.tick()/1000.0
t.done()
pg.quit()