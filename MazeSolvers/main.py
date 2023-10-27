from Modules.Visualization import Visualize
from Modules.MazeSolverV2 import MazeSolver
from Modules.FileListConversion import GetTable


def main(speed, mode, size, save, cfile):
    table = GetTable(f'MazeSolvers/Output/{cfile}')
    allowMultipleEnds = False
    previous = []
    nextMode = False
    fileChange = False
    modes = ['LeastDistance',
            'FIFO',
            'LIFO',
            'A*',
            'Random',
            'DoubleLeast',
            'DoubleFIFO',
            'DoubleLIFO',
            'DoubleClosest',
            'DoubleRandom']
    files = ['labirynth.txt',
             'labirynth2.txt',
             'labirynth3.txt',
             'CustomLabirynth.txt']
    while True:
        if fileChange:
            cfile = files[files.index(cfile) + 1] if files.index(cfile) + 1 < len(files) else files[0]
            table = GetTable(f'MazeSolvers/Output/{cfile}')
            fileChange = False
        a = MazeSolver(table)
        if nextMode:
            mode = modes[modes.index(mode) + 1] if modes.index(mode) + 1 < len(modes) else modes[0]
            nextMode = False
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
            elif mode == 'A*':
                allowMultipleEnds = True
                a.SolveAStar()
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
            nextMode, table, fileChange = list(b.run(a.actionLog, a.GetShortestPath(), save, speed))
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
    # A*
    # Random
    # DoubleLeast
    # DoubleFIFO
    # DoubleLIFO
    # DoubleClosest
    # DoubleRandom

    # SPACE - PAUSE / RESUME
    # ALL MODIFICATIONS CAN BE DONE ONLY WHEN PAUSED
    # ENTER - CHANGE MODE (FROM INITIAL TO NEXT ONE IN LIST)
    # LMB - PLACE WALL
    # MMB - PLACE END (IF SINGLE SEARCH MODE YOU CAN PLACE MORE THAN 1)
    # RMB - PLACE START (CHANGES LOCATION OF START)
    main(30, 'LIFO', (1000, 1000), save='CustomLabirynth.txt', cfile = 'labirynth.txt')
