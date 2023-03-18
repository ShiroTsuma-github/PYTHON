from pathlib import Path


def GetTable(path):
    table = []
    with open(Path(path), 'r', encoding='utf-8') as f:
        for pos, line in enumerate(f.readlines()):
            table.append(list(line.replace('\n', '')))
    return table


def SaveToFile(path, data):
    with open(f'{Path(path)}', 'w+', encoding='utf-8') as f:
        for line in data:
            f.write(''.join(line))
            f.write('\n')


if __name__ == '__main__':
    for line in GetTable('MazeSolvers\labirynth.txt'):
        print(line)
