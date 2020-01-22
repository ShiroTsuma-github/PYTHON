import pygame
import subprocess
pygame.init()
width=1920//2
height=1080//2
run=True
screen=pygame.display.set_mode((width,height))

def color_convert(color):
    basic_colors={"red":[255,0,0],
                  "blue":[0,0,255],
                  "black":[0,0,0],
                  "white":[255,255,255],
                  "green":[0,255,0],
                  "violet":[238,130,238],
                  "deep pink":[255,20,147],
                  "gray":[128,128,128],
                  "yellow":[255,255,0]
                  }
    color_to_use=basic_colors.get(color)
    return color_to_use
        

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