from pathlib import Path
import pygame
from time import sleep



pygame.init()
run=True

class MotherBoard:
    from colors import color_convert
    def __init__(self,width=1280,height=720):
        self.width=width
        self.color=self.color_convert()
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
        for x in range(0,self.gridX,XblockSize):
            for y in range(0,self.gridY,YblockSize):
                rect = pygame.Rect(x*XblockSize, y*YblockSize,
                                XblockSize, YblockSize)
                pygame.draw.rect(self.screen, c_kolor , rect, 1)
                if x*XblockSize >=self.width or y*YblockSize >=self.height:
                    break
class Labirynth():
    def __init__(self,wall='=',path=' ',start='A',end='B',read_path='A_star//labirynth.txt'):
        self.wall=wall
        self.path=path
        self.start=start
        self.end=end
        self.read_path=Path(path)
        self.__fields=self.__read_from_file(read_path)
    def full_return_fields(self):
        return self.__fields
    def lengthX(self):
        return len(self.__fields[0])
    def lengthY(self):
        return len(self.__fields)
    def yield_fields(self):
        for i,y in enumerate(self.__fields):
            for j,x in enumerate(y):
                yield [x,i,j]
    def __read_from_file(self,r_path):
        file_path=r_path
        fields=[]
        
        with open(file_path,'r') as File:
            for i,line in enumerate(File):
                if len(line)<3:
                    pass
                else:
                    fields.append([])
                for char in line:
                    if char != "\n":
                        fields[i].append(char)
        MFlen=len(fields[0])
        for i in fields:
            if len(i)>MFlen:
                MFlen=len(i)
        for i,line in enumerate(fields):
            if MFlen == len(line):
                pass
            else:
                for add in range(0,MFlen-len(line)):
                    fields[i].append(self.wall)
        return fields
    def prettify(self):
        fields=self.__fields
        Xlen=len(fields[0])+2
        Ylen=len(fields)+2
        for y in range(Ylen):
            for x in range(Xlen):
                if y ==0:
                    if x==0 or x==Xlen-1:
                        print(" ",end='')
                    else:
                        print("_",end='')
                elif y==Ylen-1:
                    if x==0 or x==Xlen-1:
                        print(" ",end='')
                    else:
                        print("‾",end='')
                else:
                    if x==0:
                        print(u"\u23B9",end='')
                    elif x==Xlen-1:
                        print(u"\u23B8",end='')
                    else:
                        if fields[y-1][x-1] ==self.wall :
                            print("█",end='')
                        elif fields[y-1][x-1] == self.start:
                            print("⚐",end='')
                        elif fields[y-1][x-1] == self.end:
                            print("⚑",end='')
                        elif fields[y-1][x-1] == self.path:
                            print("·",end='')
                        else:
                            print(fields[y-1][x-1],end='')
            print("")
    def Solve(self): 
        for i in self.yield_fields():
            if i[0] == self.start:
                init_s=i[1:]
            elif i[0] == self.end:
                init_e=i[1:]
        Solve=self.__Solve(start=init_s,end=init_e,wall=self.wall,path=self.path,maze=self.full_return_fields())
        for i in Solve.Solving_steps():
            yield i
        
    class __Solve():
        class Node():
            def __init__(self,parent=None,position=None,value=None):
                self.parent=parent
                self.position=position
                self.g=0
                self.h=0
                self.f=0
                self.value=value
            def __eq__(self, other):
                return self.position == other.position
            def __lt__(self, other):
                return self.f < other.f
            def __repr__(self):
                return (f'Position Y: {self.position[0]},Position X: {self.position[1]}, f={self.f}, g={self.g}, h={self.h}, value="{self.value}"')
        def __init__(self,start=None,end=None,wall=None,path=None,maze=None):
            self.oList=[]
            self.cList=[]
            self.wall=wall
            self.path=path
            self.maze=maze
            self.Start_node=self.Node(position=start,value=self.maze[start[0]][start[1]])
            self.End_node=self.Node(position=end,value=self.maze[end[0]][end[1]])
            self.Current_node=self.Node()
            self.oList.append(self.Start_node)
        def __add_oList(self,neighbor):
            for node in self.oList:
                if neighbor.position == node.position and neighbor.f>=node.f:
                    return False
            return True
        def Solving_steps(self):
            while len(self.oList)>0:
                """
                for i in range(len(self.oList)):
                    for j in range(len(self.oList)-1):
                        if self.oList[j].f>self.oList[j+1].f:
                            self.oList[j],self.oList[j+1]=self.oList[j+1],self.oList[j]
                """
                self.oList.sort()
                self.Current_node=self.oList.pop(0)
                self.cList.append(self.Current_node)      
                # print(f'adding to closed list {self.Current_node}')
                if self.Current_node == self.End_node:
                    path=[]
                    while self.Current_node != self.Start_node:
                        path.append(self.Current_node.position)
                        self.Current_node=self.Current_node.parent
                    for coords in reversed((path)):
                        yield coords
                    # yield path[::-1]
                y,x=self.Current_node.position
                surr=[]
                if y==0:
                    surr.append([y+1,x])
                elif y>0 and y<len(self.maze)-1:
                    surr.append([y-1,x])
                    surr.append([y+1,x])
                else:
                    surr.append([y-1,x])
                if x==0:
                    surr.append([y,x+1])
                elif x>0 and x<len(self.maze[0])-1:
                    surr.append([y,x-1])
                    surr.append([y,x+1])
                else:
                    surr.append([y,x-1])
                for side_node in surr:
                    map_value=self.maze[side_node[0]][side_node[1]]
                    if map_value==self.wall:
                        continue
                    cont=False
                    for item in self.cList:
                        if side_node == item.position:
                            cont=True
                            break
                    if cont:
                        continue
                    neighbor = self.Node(position=side_node,parent=self.Current_node,value=map_value)
                    neighbor.g = abs(neighbor.position[0] - self.Start_node.position[0]) + abs(neighbor.position[1] - self.Start_node.position[1])
                    neighbor.h = abs(neighbor.position[0] -self.End_node.position[0]) + abs(neighbor.position[1] - self.End_node.position[1])
                    neighbor.f = neighbor.g + neighbor.h
                    if self.__add_oList(neighbor=neighbor):
                        self.oList.append(neighbor)

                    
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
    color='yellow'
    pos=i[1],i[2]
    if i[0] == Labirynth.wall:
        color='black'
    elif i[0] == Labirynth.start or i[0] == Labirynth.end:
        color='red'
    elif i[0] == Labirynth.path:
        color='white'
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
        except IndexError:
            pass
        finally:
            counter+=1
    if counter>Solved_sum:
        rep=1
            


  
# klasa 1/metoda 1
# klasa 2/metoda 2

#sciezka w kontruktorze labiryntu
# bo niestety mam problem,ze jak cos zaczynam robic,to podchodze na poczatku jak perfekcjonista,wiec poczatek chce zawsze wszystko najbardziej potymalnie,jak wiem,ze da lepiej,a ilosc opcji przy klasach mnie przytlacza,wiec czesto sie poddawalem na poczatku

