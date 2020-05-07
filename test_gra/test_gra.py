import pygame
import subprocess
from time import sleep
from colors import color_convert
from objects import Cell, Board
kolor=color_convert()
pygame.init()
width=1920//2
height=1920//2
run=True
screen=pygame.display.set_mode((width,height))

def text(text,size,color):
    result=pygame.font.SysFont("Arial", size)
    if isinstance(color,str):
        render=result.render(text, 1, kolor.convert(color))
    if isinstance(color, list):
        render=result.render(text, 1, color)
    x=(width-render.get_rect().width)//2
    y=(height-render.get_rect().height)//2  
    screen.blit(render,(x,y))


screen.fill(kolor.convert('white'))


def create_board(size_x,size_y):
    board=[]
    for i in range(size_y):
        board.append([])
        for j in range(size_x):
            board[i].append(' ')
    return board

def create_cell(pos_x,pos_y):
    board[pos_y-1][pos_x-1]='X'
    return board
    
def drawCell(pos_x,pos_y):
    blockSize = Board.get_BlockSize(10)
    for x in range(width//blockSize):
        for y in range(height//blockSize):
            rect = pygame.Rect(x*blockSize, y*blockSize,
                               blockSize, blockSize)
            if x==pos_x-1 and y==pos_y-1:
                pygame.draw.rect(screen, kolor.convert('red'), rect, 0)
            if x*blockSize >=width or y*blockSize >=height:
                break


board=create_board(10,10)
board=create_cell(3,4)
Board=Board(width,height)
screen.fill(kolor.convert('white'))
Board.drawGrid(10)

counter=0
while run:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            run =False
    drawCell(5,5)
    sleep(2)
    drawCell(1,1)

    #text("Klaudiusz Hynek",32,kolor.full_random_color())
    pygame.display.update()
pygame.quit()
