from pathlib import Path
import pygame
from time import sleep
from Cmodules.colors import color_convert
class MotherBoard:
    
    def __init__(self,width=1280,height=720):
        self.width=width
        self.color=color_convert()
        self.height=height
        self.screen=pygame.display.set_mode((width,height))
        self.screen.fill(self.color.convert('white'))
    def changeBackground(self,_input):
        self.screen.fill(self.color.convert(_input))
        
    def text(self,text,_color):
        result=pygame.font.SysFont("Arial", int(self.XblockSize//1.5))
        if isinstance(_color,str):
            render=result.render(text, 1, self.color.convert(_color))
        if isinstance(_color, list):
            render=result.render(text, 1, self.color.convert(_color))
        x=(self.width-render.get_rect().width)//2
        y=(self.height-render.get_rect().height)//2  
        self.screen.blit(render,(x,y))
                
class Board(MotherBoard):
    def __init__(self,gridX=10,gridY=10,*args,**kwargs):
        self.gridX=gridX
        self.gridY=gridY
        super().__init__(*args, **kwargs)
        self.XblockSize=self.width//gridX
        self.YblockSize=self.height//gridY
        self.cell_positions=self.__get_coordinates()
    def __get_coordinates(self):
        cells=[]
        counter=0
        for x in range(0,self.width,self.XblockSize):
            cells.append([])
            for y in range(0,self.height,self.YblockSize):
                cells[counter].append([x,y])
            counter+=1
        return cells       
    def UpdateCell(self,_color='white',position=None):
        if position == None:
            return("Nie podana została pozycja do aktualizacji")
        else:
            c_kolor=self.color.convert(_color)
            position=self.cell_positions[position[1]][position[0]]
            rect = pygame.Rect(position[0], position[1],
                                self.XblockSize, self.YblockSize)
            return pygame.draw.rect(self.screen, c_kolor , rect, 0)
        
    def drawGrid(self,_color='black'):
        XblockSize = self.XblockSize
        YblockSize = self.YblockSize
        c_kolor=self.color.convert(_color)
        for y in range(0,self.gridY*YblockSize,YblockSize):
            for x in range(0,self.gridX*XblockSize,XblockSize):
                rect = pygame.Rect(x, y,
                                XblockSize, YblockSize)
                pygame.draw.rect(self.screen, c_kolor , rect, 1)
                if x >=self.width or y >=self.height:
                    break



  