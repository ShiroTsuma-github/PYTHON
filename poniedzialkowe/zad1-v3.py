import math
from funcy import print_durations


@print_durations()
def cholesky_decomposition(A):
    n = len(A)
    l: list[list[float]] = [[0.0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(i + 1):
            if i == j:
                sum_sq = 0
                for k in range(i):
                    sum_sq += math.pow(l[i][k], 2) 

                l[i][i] = math.sqrt(a[i][i] - sum_sq)

            else:
                sum = 0
                for k in range(j):
                    sum = l[i][k] * l[j][k]

                l[i][j] = (a[i][j] - sum) / l[j][j]
    return l


a = [
    [4.0, 12.0, -16.0],
    [12.0, 37.0, -43.0],
    [-16.0, -43.0, 98.0]]

L: list[list[float]] = cholesky_decomposition(a)
print(L)