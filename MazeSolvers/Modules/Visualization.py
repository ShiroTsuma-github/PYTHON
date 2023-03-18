import pygame
from .Colors import Colors
from pathlib import Path
from .FileListConversion import SaveToFile



class Visualize():
    def __init__(self, size, marks, allowMultipleEnds) -> None:
        pygame.init()
        self.size = size
        self.cellSize = (0, 0)
        self.boardState = []
        self.multipleEnds = allowMultipleEnds
        self.board = []
        self.marks = marks
        pygame.display.set_caption('MazeSolverV2 - Tomasz Góralski')
        self.ColorMaster = Colors()
        self.objectcolors = {
            'WALL': self.ColorMaster.GetColor('black'),
            'START': self.ColorMaster.GetColor('green'),
            'END': self.ColorMaster.GetColor('red'),
            'SEEN': self.ColorMaster.GetColor('pink'),
            'WALK': self.ColorMaster.GetColor('orange'),
            'BACKGROUND': self.ColorMaster.GetColor("white"),
            'TEXT': self.ColorMaster.GetColor('black'),
        }
        self.screen = pygame.display.set_mode(self.size)
        self.clock = pygame.time.Clock()
        self._background()

    def Resize(self, size):
        self.size = size
        self.screen = pygame.display.set_mode(self.size)

    def __CalculateCellSize(self, table):
        lenY = len(table)
        lenX = len(table[0])
        self.cellSize = (round(self.size[0] / lenY, 0), round(self.size[1] / lenX, 0))
        # self.Resize((self.cellSize[0] * (lenY - 1), self.cellSize[1] * (lenX - 1)))

    def Setup(self, table):
        self.__CalculateCellSize(table)
        self.board = table
        for y, lineY in enumerate(table):
            self.boardState.append([])
            for x, objX in enumerate(lineY):
                self.boardState[y].append(pygame.Rect(
                    x * self.cellSize[1],   # LEFT
                    y * self.cellSize[0],   # TOP
                    self.cellSize[1],       # WIDH
                    self.cellSize[0]))      # HEIGHT
        self.Resize((self.boardState[y][x].left + self.boardState[y][x].width,
                     self.boardState[y][x].top + self.boardState[y][x].height))
   
    def __DrawBase(self):
        for y, lineY in enumerate(self.board):
            for x, objX in enumerate(lineY):
                color = None
                if self.marks.get(self.board[y][x]) == 'Wall':
                    color = self.objectcolors['WALL']
                elif self.marks.get(self.board[y][x]) == 'Start':
                    color = self.objectcolors['START']
                elif self.marks.get(self.board[y][x]) == 'End':
                    color = self.objectcolors['END']
                if color is None:
                    continue
                pygame.draw.rect(self.screen,
                                 color,
                                 self.boardState[y][x])

    def __drawMovement(self, movement, action):
        if action:
            return pygame.draw.rect(self.screen,
                             self.objectcolors['SEEN'],
                             self.boardState[movement[0]][movement[1]])
        else:
            return pygame.draw.rect(self.screen,
                             self.objectcolors['WALK'],
                             self.boardState[movement[0]][movement[1]])

    def _locateAndSwap(self, target, item):

        def get_keys_from_value(dict, val):
            return [k for k, v in dict.items() if v == val][0]

        for y, line in enumerate(self.board):
            for x, pos in enumerate(line):
                if pos == get_keys_from_value(self.marks, target):
                    self.board[y][x] = get_keys_from_value(self.marks, item)

    def __Recalculate(self, mousePos, button):

        def get_keys_from_value(dict, val):
            return [k for k, v in dict.items() if v == val][0]

        mouseX, mouseY = mousePos
        sqY = int(mouseY // self.cellSize[0])
        sqX = int(mouseX // self.cellSize[1])
        if button == 1:     # LEFT BUTTON
            if self.marks[self.board[sqY][sqX]] == 'Path':
                self.board[sqY][sqX] = get_keys_from_value(self.marks, 'Wall')
            elif self.marks[self.board[sqY][sqX]] == 'Wall':
                self.board[sqY][sqX] = get_keys_from_value(self.marks, 'Path')
        elif button == 2:
            if self.marks[self.board[sqY][sqX]] == 'Path':
                if not self.multipleEnds:
                    self._locateAndSwap('End', 'Path')
                self.board[sqY][sqX] = get_keys_from_value(self.marks, 'End')
            elif self.marks[self.board[sqY][sqX]] == 'End' and self.multipleEnds:
                self.board[sqY][sqX] = get_keys_from_value(self.marks, 'Path')
        elif button == 3:
            if self.marks[self.board[sqY][sqX]] == 'Path':
                self._locateAndSwap('Start', 'Path')
                self.board[sqY][sqX] = get_keys_from_value(self.marks, 'Start')
        return self.board

    def _background(self):
        self.screen.fill(self.objectcolors['BACKGROUND'])

    def DisplayScore(self):
        text = pygame.font.SysFont('calibri', int(self.size * 22 / 500))
        white, black = self.Score()
        whitetextsurface = text.render(str(white), True, self.objectcolors['TEXT'])
        blacktextsurface = text.render(str(black), True, self.objectcolors['TEXT'])
        self.screen.blit(whitetextsurface, (self.size * 1.035, self.size * 0.85))
        self.screen.blit(blacktextsurface, (self.size * 1.035, self.size * 0.15))

    def DisplayButtons(self):
        pass

    def run(self, actionLog: list, pathLog: list, save='', speed: int = 60):
        self._background()
        self.__DrawBase()
        pygame.display.flip()
        run = True
        currentPos = 1
        if not self.multipleEnds:
            currentPos = 2
        actions = True
        update = False
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if update:
                        continue
                    ans = self.__Recalculate(event.pos, event.button)
                    if save:
                        
                        SaveToFile(f'MazeSolvers/Output/{save}', ans)
                    return (False, ans, False)
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        update = not update
                    elif event.key == pygame.K_RETURN:
                        return (True, self.board, False)
                    elif event.key == pygame.K_BACKSPACE:
                        return (False, self.board, True)
            if not update:
                continue
            current = actionLog[currentPos] if actions else pathLog[currentPos]
            pygame.display.update(self.__drawMovement(current, actions))
            if currentPos < len(actionLog) - 2 and actions:
                currentPos += 1
            elif currentPos < len(pathLog) - 2 and not actions:
                currentPos += 1
            else:
                currentPos = 1
                actions = False
            self.clock.tick(speed)
            pygame.display.flip()

    def getSize(self):
        return self.screen.get_size()


def main():
    a = Visualize((1000, 1000))
    # a.Setup()
    # a.run()


if __name__ == '__main__':
    main()
