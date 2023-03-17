from Modules.Visualization import Visualize
from Modules.MazeSolverV2 import MazeSolver
from Modules.FileToList import GetTable


def main(speed, mode, src, size):
    table = src
    allowMultipleEnds = False
    previous = []
    while True:
        a = MazeSolver(table)
        try:
            if mode == 'LeastDistance':
                allowMultipleEnds = True
                a.SolveLeastDistance()
            elif mode == 'FIFO':
                allowMultipleEnds = True
                a.SolveFIFO()
            elif mode == 'LIFO':
                allowMultipleEnds = True
                a.SolveLIFO()
            elif mode == 'Closest':
                allowMultipleEnds = True
                a.SolveClosest()
            elif mode == 'Random':
                allowMultipleEnds = True
                a.SolveRandom()
            elif mode == 'DoubleLeast':
                a.SolveDoubleSidedLeastDistance()
            elif mode == 'DoubleFIFO':
                a.SolveDoubleSidedFIFO()
            elif mode == 'DoubleLIFO':
                a.SolveDoubleSidedLIFO()
            elif mode == 'DoubleClosest':
                a.SolveDoubleSidedClosest()
            elif mode == 'DoubleRandom':
                a.SolveDoubleSidedRandom()
            else:
                return
        except (IndexError, TypeError):
            table = previous.copy()
            continue
        b = Visualize(size, MazeSolver.marking, allowMultipleEnds)
        previous = CopyVals(table)
        b.Setup(table)
        try:
            table = list(b.run(a.actionLog, a.GetShortestPath(), speed=speed))
        except TypeError:
            break


def CopyVals(l1):
    temp = []
    for y, line in enumerate(l1):
        temp.append([])
        for x, pos in enumerate(line):
            temp[y].append(pos)
    return temp


if __name__ == '__main__':
    # MODES:
    # LeastDistance
    # FIFO
    # LIFO
    # Closest
    # Random
    # DoubleLeast
    # DoubleFIFO
    # DoubleLIFO
    # DoubleClosest
    # DoubleRandom
    tab = GetTable('MazeSolvers\labirynth.txt')
    main(150, 'LeastDistance', tab, (1000, 1000))
