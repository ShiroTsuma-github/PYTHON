from typing import  Union
from math import sqrt
from random import shuffle, choice

src = """
.#####
......
.##.##
.##@##
.#..##
.#.###
!..###
"""
src2 = """
#################################################################################
#.#...#....!....#...................#.............#.......#.............#.......#
#.#.#.#.###.###.#########.#########.#.#####.#####.#####.#.#.#######.###.#.#####.#
#...#.....#...#.#.........#.#.....#.#...#...#...#.......#.#.#.......#.#.#.#...#.#
#############.#.#.#########.#.###.#.###.#.###.#.#.#######.###.#######.#.#.#.#.#.#
#...........#.#...#.#.....#...#...#.....#.#.#.#...#...#.......#.......#.#.#.#.#.#
#.#########.#.#####.#.#.#.#.###.#####.#.#.#.#.#####.#.#########.###.###.###.#.#.#
#.#.........#...#...#.#.#.#...#.....#.#.#.#...#.#...#.......#.....#.#...#...#...#
#.#########.#.#.###.#.#.#####.###.#.#.#.#.#.###.#.#########.#####.#.#.###.#####.#
#.#.......#.#.#...#...#.#.....#.#.#.#...#.#.....#.#.....#.#...#...#.......#...#.#
#.#.#####.#.#.###.#####.#.#####.#.#.###.#.#######.###.#.#.###.#.###########.#.#.#
#...#...#.#.#...#.....#.#.......#.#.#...#.....#...#...#.....#.#.#...#...#...#...#
#####.#.#.#.#########.#.#######.#.###.#######.#.###.#########.###.#.#.#.#.#######
#.....#...#.#.........#.......#.#...#.#.#.....#.#.....#.......#...#.#.#.#.#.....#
#.#########.#.#########.###.###.###.#.#.#.###.#.#.###.#.#######.###.#.###.#.###.#
#...#.#.....#...#.....#.#.#...#.#.#.....#...#.#.#...#.#...#...#...#.#.#...#...#.#
###.#.#.#####.#.#.#.###.#.###.#.#.#####.###.###.#####.###.#.#.#.###.#.#.#####.#.#
#...#...#.....#.#.#.#...#...#.....#...#.#...#...........#.#.#...#...#.......#.#.#
#.###.#########.#.#.#.###.#.#####.#.#.###.###.###########.#.###.#.#########.###.#
#.#.............#.#.......#.#...#.#.#...#.#...#.#.......#.......#.#...#.....#...#
#.#.#############.#########.#.#.###.###.#.#.###.#.#####.#.#######.#.#.#.#####.#.#
#.#.#...........#.#.#.#.....#.#.....#...#.#.....#...#.#.#.#.#...#.#.#.#.#.....#.#
#.###.#########.#.#.#.#######.#######.###.#####.###.#.#.#.#.###.#.#.#.#.#####.#.#
#.....#...#.....#...#.........#.....#...#.....#...#...#.#.....#.#...#.#.#.....#.#
#.#####.#.#.#######.###########.#######.#.#######.###.#.###.###.#####.#.#.#####.#
#.....#.#.#...#...#.#.......#.........#.#...#.......#.#.#...#...#.....#.#.#...#.#
#######.#.###.#.###.#.#####.#.#####.###.#.#.#.#######.#.#####.###.#####.#.###.#.#
#.......#.#...#.....#.#...#.#...#.#.....#.#.#.#.#.....#...#...#...#.....#...#.#.#
#.#######.#.#.#####.#.###.#.###.#.#######.#.#.#.#.#######.#.###.#.###.#####.#.#.#
#.#.#.....#.#.#...#.#...#.#...#...#.#...#.#...#.#.....#.#...#...#...#.......#...#
#.#.#.#####.#.#.#.#####.#.###.###.#.#.#.#.#####.#####.#.#####.#####.#######.#.###
#.#...#.....#.#.#.#...#...#.#.#...#...#.#.#...#.....#...#.#...#...#.....#...#.#.#
#.###.###.#.###.#.#.#.###.#.#.#.#######.#.#.#.#####.###.#.#.###.#.#####.###.#.#.#
#...#...#.#.#...#.#.#...#.#.#.#.#.......#...#.........#.#...#...#.#...#...#.#...#
#.#.###.#.#.#.###.#.###.#.#.#.#.###.###.###########.###.#.###.###.###.###.#.###.#
#.#...#.#.#.#...#...#...#.#.#.#.....#...#...#.....#.#...#.....#.....#.#...#...#.#
#.###.#.#.#####.#####.#.#.#.#.#######.###.#.#####.#.#.#############.#.#.###.#.#.#
#...#.#...#...#.....#.#.#.#.#.#...#...#.#.#.......#.#.#.......#...#...#.#.#.#...#
###.#.#####.#.#####.#.###.#.#.#.#.#.###.#.#########.#.#.#.#.#.#.#.#####.#.#.#####
#...#.......#.......#.......#...#..........#........#...#...#...#..............@#
#################################################################################
"""
src3 = """
##########
........#@
...###....
........#.
......####
...#####!#
..........
##########

"""


class MazeSolver:

    class Node:
        def __init__(self, mark: str, position: 'tuple[int, int]', start=False, end=False) -> None:
            self.mark = mark
            self.start = start
            self.end = end
            self.position = position
            self.parent = None
            self.neighbours = None
            self.distance = 0

        def GetNeighbours(self, state) -> None:
            if self.mark != 'Path':
                return
            else:
                moves = [
                    (-1, 0),    # TOP
                    (0, -1),    # LEFT
                    (1, 0),     # DOWN
                    (0, 1)]     # RIGHT
                lenY = len(state)
                lenX = len(state[0])
                neighbours = []
                for y, x in moves:
                    node_y, node_x = self.position
                    if node_y + y < 0 or node_y + y == lenY:
                        continue
                    if node_x + x < 0 or node_x + x == lenX:
                        continue
                    AdjNode = state[node_y + y][node_x + x]
                    if AdjNode.mark == 'Path':
                        neighbours.append(AdjNode)
                shuffle(neighbours)
                self.neighbours = neighbours if neighbours else False

        def __str__(self) -> str:
            return f"""
Mark: {self.mark}   {"|Start: True" if self.start else ""}{"|End: True" if self.end else ""}
Parent: {self.parent}
Position: {self.position}
Distance: {self.distance}
Neighbours: {self.neighbours}
            """

    def __init__(self, table) -> None:
        self.startPos = None    # (y, x)
        self.endPos = None      # (y, x)
        self.shortestPathLen = 0
        self.walkable = 0
        self.actionLog = []
        self.endNode = None
        self.table = table
        self.state = self.__CreateState(table)
        self.__UpdateState()
        self.visited = []
        self.next = []
        self.mode = None

    marking =\
    {
        '.': 'Path',
        '#': 'Wall',
        '!': 'Start',
        '@': 'End',
    }
    traversed =\
    {
        'Seen': '`',
        'Correct': '*'
    }

    def __CreateState(self, table):
        lenLine = len(table[0])
        for i, line in enumerate(table):
            if len(line) != lenLine:
                raise ValueError(f"Line {i + 1} is of different length: {len(line)} (Expected {lenLine})")
        if not table:
            raise ValueError('Empty table')
        result = []
        for i, line in enumerate(table):
            resultline = []
            for j, obj in enumerate(line):
                if obj not in MazeSolver.marking.keys():
                    raise ValueError(f'Argument outside of expected marks ({obj})')
                temp = MazeSolver.marking.get(obj)
                if temp in ('Start', 'End', 'Path'):
                    self.walkable += 1
                if temp == 'Start':
                    self.startPos = (i, j)
                    resultline.append(self.Node('Path', (i, j), start=True))
                elif temp == 'End':
                    self.endPos = (i, j)
                    resultline.append(self.Node('Path', (i, j), end=True))
                else:
                    resultline.append(self.Node(temp, (i, j)))
            result.append(resultline)
        return result

    def __UpdateState(self):
        for obj in self.__GetObjects():
            obj.GetNeighbours(self.state)

    def __SolverDoubleSided(self, distanceFunc, chooseFunc):

        def ParentSwap(main, other):
            ogParent = main                     # Backup of actual node
            actualNode = other                  # Swapping positions to do reversal
            while True:                         # Since we go from start we go to end
                temp = actualNode.parent        # Keeping parent 1 further in graph
                actualNode.parent = ogParent    # Changing directions of parent in actual position
                ogParent = actualNode           # After direction change we store this as backup
                actualNode = temp               # We swap with parent 1 further to do another swap
                if actualNode.start or actualNode.end:
                    break
            self.endNode = actualNode           # When we finish save this as endNode
            self.endNode.parent = ogParent      # Give parent to last node
            return

        def Filter(nextX, actualNodeX):
            self.visited.append(actualNodeX)
            self.actionLog.append(actualNodeX.position)
            nextX.pop(nextX.index(actualNodeX))
            for pos in actualNodeX.neighbours:
                if pos in self.visited or pos in nextX:
                    continue
                else:
                    if pos.parent is not None:
                        ParentSwap(actualNodeX, pos)
                        return (-1, -1)
                    else:
                        pos.parent = actualNodeX
                        pos.distance = distanceFunc(
                            actualNodeX,
                            pos,
                            startPos.position if actualNodeX == actualNodeE else endPos.position)
                        nextX.append(pos)
            return (nextX, chooseFunc(nextX))

        self.mode = 'DoubleSided'
        steps = 0
        nextS = []
        nextE = []
        startPos = self.state[self.startPos[0]][self.startPos[1]]
        actualNodeS = startPos
        endPos = self.state[self.endPos[0]][self.endPos[1]]
        actualNodeE = endPos
        actualNodeS.distance = distanceFunc(startPos, None, endPos.position)
        actualNodeE.distance = distanceFunc(endPos, None, startPos.position)
        nextS.append(actualNodeS)
        nextE.append(actualNodeE)
        while nextS or nextS:
            nextS, actualNodeS = Filter(nextS, actualNodeS)
            if nextS == -1:
                return
            nextE, actualNodeE = Filter(nextE, actualNodeE)
            if nextE == -1:
                return
            steps += 1

    def SolveDoubleSidedFIFO(self):

        def distFunc(actualNode, pos, *args):
            if pos is None:
                return 0
            return actualNode.distance + 1

        def chooseFunc(nextX):
            return nextX[0]

        self.__SolverDoubleSided(distFunc, chooseFunc)
        self.mode += 'FIFO'

    def SolveDoubleSidedLIFO(self):

        def distFunc(actualNode, pos, *args):
            if pos is None:
                return 0
            return actualNode.distance + 1

        def chooseFunc(nextX):
            return nextX[len(nextX) - 1]

        self.__SolverDoubleSided(distFunc, chooseFunc)
        self.mode += 'LIFO'

    def SolveDoubleSidedClosest(self):

        def distFunc(actualNode, pos, *args):
            if pos is None:
                return 0
            return actualNode.distance + 1

        def chooseFunc(nextX):
            minPos = nextX[0]
            table = nextX
            for pos in table:
                if pos.distance <= minPos.distance:
                    minPos = pos
            return minPos

        self.__SolverDoubleSided(distFunc, chooseFunc)
        self.mode += 'Closest'

    def SolveDoubleSidedLeastDistance(self):

        def distFunc(actualNode, pos, endPos=None):
            end_y, end_x = endPos
            if pos is None:
                y, x = actualNode.position
            else:
                y, x = pos.position
            return sqrt( (end_x - x)**2 + (end_y - y)**2 )

        def chooseFunc(nextX):
            minPos = nextX[0]
            table = nextX
            for pos in table:
                if pos.distance <= minPos.distance:
                    minPos = pos
            return minPos

        self.__SolverDoubleSided(distFunc, chooseFunc)
        self.mode += 'minDistance'

    def SolveDoubleSidedRandom(self):

        def distFunc(actualNode, pos, *args):
            if pos is None:
                return 0
            return actualNode.distance + 1

        def chooseFunc(nextX):
            return choice(nextX)

        self.__SolverDoubleSided(distFunc, chooseFunc)
        self.mode += 'Random'

    def __Solver(self, distanceFunc, chooseFunc):
        steps = 0
        actualNode = self.state[self.startPos[0]][self.startPos[1]]
        actualNode.distance = distanceFunc(actualNode, None)
        self.next.append(actualNode)
        while self.next:
            self.actionLog.append(actualNode.position)
            self.next.pop(self.next.index(actualNode))
            self.visited.append(actualNode)
            if actualNode.end:
                self.endNode = actualNode
                return
            for pos in actualNode.neighbours:
                if pos in self.visited or pos in self.next:
                    continue
                else:
                    pos.parent = actualNode
                    pos.distance = distanceFunc(actualNode, pos)
                    self.next.append(pos)
            actualNode = chooseFunc()
            steps += 1

    def SolveFIFO(self):
        self.mode = 'FIFO'

        def distFunc(actualNode, pos):
            if pos is None:
                return 0
            return actualNode.distance + 1

        def chooseFunc():
            return self.next[0]

        self.__Solver(distFunc, chooseFunc)

    def SolveLIFO(self):
        self.mode = 'LIFO'

        def distFunc(actualNode, pos):
            if pos is None:
                return 0
            return actualNode.distance + 1

        def chooseFunc():
            return self.next[len(self.next) - 1]

        self.__Solver(distFunc, chooseFunc)

    def SolveClosest(self):
        self.mode = 'Closest'

        def distFunc(actualNode, pos):
            if pos is None:
                return 0
            return actualNode.distance + 1

        def chooseFunc():
            minPos = self.next[0]
            table = self.next
            for pos in table:
                if pos.distance <= minPos.distance:
                    minPos = pos
            return minPos

        self.__Solver(distFunc, chooseFunc)

    def SolveLeastDistance(self):
        self.mode = 'minDistance'

        def distFunc(actualNode, pos):
            end_y, end_x = self.endPos
            if pos is None:
                y, x = actualNode.position
            else:
                y, x = pos.position
            return sqrt( (end_x - x)**2 + (end_y - y)**2 )

        def chooseFunc():
            minPos = self.next[0]
            table = self.next
            for pos in table:
                if pos.distance <= minPos.distance:
                    minPos = pos
            return minPos

        self.__Solver(distFunc, chooseFunc)

    def SolveRandom(self):
        self.mode = 'Random'

        def distFunc(actualNode, pos):
            return actualNode.distance + 1

        def chooseFunc():
            return choice(self.next)

        self.__Solver(distFunc, chooseFunc)

    def DisplayMaze(self):
        for pos in self.visited:
            if pos.start or pos.end:
                continue
            y, x = pos.position
            self.table[y][x] = MazeSolver.traversed['Seen']
        actualNode = self.endNode
        target = actualNode.start if self.endNode.end else actualNode.end
        while not target:
            target = actualNode.start if self.endNode.end else actualNode.end
            if actualNode.end or actualNode.start:
                actualNode = actualNode.parent
                continue
            y, x = actualNode.position
            self.table[y][x] = MazeSolver.traversed['Correct']
            actualNode = actualNode.parent
        print(MazeSolver.ConvertTableToString(self.table))

    def Verify(self):
        if self.endNode is None:
            raise ValueError("DisplayStats invoked before solving labirynth")
        if self.shortestPathLen == 0:
            actualNode = self.endNode
            target = actualNode.start if self.endNode.end else actualNode.end
            while not target:
                target = actualNode.start if self.endNode.end else actualNode.end
                self.shortestPathLen += 1
                actualNode = actualNode.parent
        t = set(self.actionLog)
        for pos in t:
            if self.actionLog.count(pos) > 1:
                raise RuntimeError(f"Somehow went to same place more than 1 time ({pos}: {self.actionLog.count(pos)})")
        if self.shortestPathLen > len(self.visited):
            raise RuntimeError(f"Somehow shortest path is smaller than places seen ({self.shortestPathLen}: {len(self.visited)})")
        if len(self.actionLog) != len(self.visited):
            raise RuntimeError(f"Somehow took different amount of actions, than seen places ({len(self.actionLog)}: {len(self.visited)})")
        if len(self.actionLog) > self.walkable or len(self.visited) > self.walkable:
            raise RuntimeError(f"Somehow took | visited more things than possible ({len(self.actionLog)}. Possible {self.walkable})")

    def DisplayStats(self):
        self.Verify()
        print("=" * 30)
        print(f"Mode run: {self.mode}")
        print(f"Places Seen vs Possible: {len(self.visited)} | {self.walkable}")
        print(f"Seen | Possible Ratio: {round(self.walkable / len(self.visited) - 1,5)}")
        print(f"Shortest Path Found: {self.shortestPathLen}")
        print(f"Efficiency: {round(self.shortestPathLen / len(self.visited) * 100,2)}%")

    def GetState(self):
        for obj in self.__GetObjects():
            yield str(obj)

    def __GetObjects(self):
        for line in self.state:
            for obj in line:
                yield obj

    @staticmethod
    def ConvertStringToTable(src):
        table = []
        for line in src.split('\n'):
            if line:
                table.append(list(line))
        return table

    @staticmethod
    def ConvertTableToString(table):
        result = ''
        for line in table:
            result += ''.join(line)
            result += '\n'
        return result


def main():

    # table = MazeSolver.ConvertStringToTable(src2)
    # a = MazeSolver(table)
    # a.SolveFIFO()
    # a.DisplayStats()
    ## a.DisplayMaze()

    # table = MazeSolver.ConvertStringToTable(src2)
    # b = MazeSolver(table)
    # b.SolveLIFO()
    # b.DisplayStats()
    ## b.DisplayMaze()

    # table = MazeSolver.ConvertStringToTable(src2)
    # c = MazeSolver(table)
    # c.SolveClosest()
    # c.DisplayStats()
    ## c.DisplayMaze()

    # table = MazeSolver.ConvertStringToTable(src2)
    # d = MazeSolver(table)
    # d.SolveLeastDistance()
    # d.DisplayStats()
    ## d.DisplayMaze()

    table = MazeSolver.ConvertStringToTable(src2)
    e = MazeSolver(table)
    e.SolveRandom()
    e.DisplayStats()
    ## e.DisplayMaze()
    
    # table = MazeSolver.ConvertStringToTable(src2)
    # f = MazeSolver(table)
    # f.SolveDoubleSidedFIFO()
    # f.DisplayStats()
    ## f.DisplayMaze()

    # table = MazeSolver.ConvertStringToTable(src2)
    # g = MazeSolver(table)
    # g.SolveDoubleSidedLIFO()
    # g.DisplayStats()
    ## g.DisplayMaze()

    # table = MazeSolver.ConvertStringToTable(src2)
    # h = MazeSolver(table)
    # h.SolveDoubleSidedClosest()
    # h.DisplayStats()
    ## h.DisplayMaze()

    # table = MazeSolver.ConvertStringToTable(src2)
    # i = MazeSolver(table)
    # i.SolveDoubleSidedLeastDistance()
    # i.DisplayStats()
    ## i.DisplayMaze()

    table = MazeSolver.ConvertStringToTable(src2)
    j = MazeSolver(table)
    j.SolveDoubleSidedRandom()
    j.DisplayStats()
    j.DisplayMaze()

if __name__ == '__main__':
    main()
