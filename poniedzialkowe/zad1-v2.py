import math
from funcy import print_durations


@print_durations()
def Cholesky_Decomposition(matrix):
    n = len(matrix)
    L = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        # i = 0 -> j = 0
        # i = 1 -> j = 0, 1
        # i = 2 -> j = 0, 1, 2 -> k = 0
        for j in range(i + 1):
            suma = 0

            # dla 3x3
            #   0 x 0 = sqrt([0,0] - 0)
            #   1 x 1 = sqrt([1,1] - [1,0]^2)
            #   2 x 2 = sqrt([2,2] - [2,0]^2 + [2,1]^2)
            if (j == i):
                for k in range(j):
                    suma += L[j][k] ** 2
                L[j][j] = int(math.sqrt(matrix[j][j] - suma))
            else:
                # dla 3x3
                # i = 2, j = 1, k = 0
                for k in range(j):
                    suma += (L[i][k] * L[j][k])
                # i = 1, j = 0      1 x 0 = [1, 0] / [0, 0]
                # i = 2, j = 0, 1   2 x 0 = [2, 0] / [0, 0]
                #                   2 x 1 = [2, 1] / [1, 1] 
                if (L[j][j] > 0):
                    L[i][j] = int(
                        (matrix[i][j] - suma) / L[j][j])
    return L


matrix: list[list[int]] = [
    [4, 12, -16],
    [12, 37, -43],
    [-16, -43, 98]]
L: list[list[int]] = Cholesky_Decomposition(matrix)
print(L)