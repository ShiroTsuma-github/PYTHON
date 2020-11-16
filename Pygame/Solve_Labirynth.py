from pathlib import Path
import pygame
from time import sleep
from Cmodules.Board import *
from Cmodules.Labirynth import Labirynth

pygame.init()
run=True                  
init=True
update=False
clock = pygame.time.Clock()
Labirynth=Labirynth(wall='#',path='.',start='$',end='@')
# Labirynth.prettify()
Board=Board(gridX=Labirynth.lengthX(),gridY=Labirynth.lengthY(),width=1680,height=1050)
Board.drawGrid()
Labirynth.prettify()
Solved=[]
for i in Labirynth.Solve():
    Solved.append(i)
Solved_sum=len(list(Solved))
for i in Labirynth.yield_fields():
    pos=i[1],i[2]
    if i[0] == Labirynth.wall:
        color='black'
    elif i[0] == Labirynth.start or i[0] == Labirynth.end:
        color='red'
    elif i[0] == Labirynth.path:
        color='pink'
    Board.UpdateCell(position=pos,_color=color)
update=True
init=False
counter=0
rep=0
while run:
    # if init:
    clock.tick(20)
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            print("end")
            run =False
    if update:   
        pygame.display.update()
        update=False
    if rep==0:
        try:
            pygame.display.update(Board.UpdateCell(position=Solved[counter],_color='lime'))
        except:
            pass
        finally:
            counter+=1
    if counter>Solved_sum:
        rep=1
            


  
