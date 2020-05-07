import pygame
from colors import color_convert as kolor
class Cell:
    pass

class Board:
    def __init__(self,width,height):
        self.width=width
        self.height=height
        self.screen=pygame.display.set_mode((width,height))
    def get_BlockSize(self,grid):
        return self.width//grid
    
    def drawGrid(self,grid):
        blockSize = self.get_BlockSize(10)
        for x in range(width):
            for y in range(height):
                rect = pygame.Rect(x*blockSize, y*blockSize,
                                blockSize, blockSize)
                pygame.draw.rect(screen, kolor.convert('black'), rect, 1)
                if x*blockSize >=width or y*blockSize >=height:
                    break
