import pygame
import subprocess
from colors import color_convert
kolor=color_convert()
pygame.init()
width=1920//2
height=1080//2
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
    
while run:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            run =False

    text("Klaudiusz Hynek",32,kolor.full_random_color())
    pygame.display.update()
pygame.quit()
kolor.show_colors()
