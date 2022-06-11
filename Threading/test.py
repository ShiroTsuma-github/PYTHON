from multiprocessing import Pool
from random import randint


def gen() -> int:
    yield randint(0, 100)


def tablica(size: int) -> list[int]:
    x = gen()
    ans = list()
    for _ in range(size):
        ans = next(x)
    return ans


if __name__ == '__main__':
    with Pool(5, maxtasksperchild=1) as p:
        x = p.map(tablica, [1, 2, 3, 4, 5, 6, 7])
        print(x)
