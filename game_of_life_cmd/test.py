import os
from time import sleep
from colored import fg,bg,attr
import pygame

def color(color,text):
    get_color={
    'error':'#FF0000',
    'success':'#00FF00',
    'process':'#FFFF00',
    'info':'#0000FF',
    }
    reset=attr('reset')
    return (fg(get_color[color])+text+reset)

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def create_board(size_x,size_y):
    board=[]
    for i in range(size_y):
        board.append([])
        for j in range(size_x):
            board[i].append('X')
    return board

def place_cells():
    pass



board=create_board(10,10)
while True:
    for j in board:
        data=j
        print(" ".join(data))
    sleep(1)
    cls()