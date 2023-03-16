from pathlib import Path
class Labirynth():
    def __init__(self,wall='=',path=' ',start='A',end='B',read_path='Pygame//labirynth.txt'):
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
                for _ in range(0,MFlen-len(line)):
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
