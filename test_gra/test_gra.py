import pygame
import subprocess
import colors.py
pygame.init()
width=1920//2
height=1080//2
run=True
screen=pygame.display.set_mode((width,height))
     

def text(text,size,color):
    result=pygame.font.SysFont("Arial", size)
    render=result.render(text, 1, color_convert(color))
    x=(width-render.get_rect().width)//2
    y=(height-render.get_rect().height)//2
    
    screen.blit(render,(x,y))

while run:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            run =False

    text("What do you see here?",32,"gray")
    pygame.display.update()
pygame.quit()