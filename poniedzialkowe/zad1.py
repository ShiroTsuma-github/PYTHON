from funcy import print_durations
import pprint


@print_durations()
def cholesky_decomposition(A) -> list[list[float]]:
    N: int = len(A)
    L: list[list[float]] = [[0.0] * N for _ in range(N)]

    for i in range(N):
        for j in range(i + 1):
            if i == j:
                sum_sq = sum(L[i][k] ** 2 for k in range(i))
                L[i][i] = (A[i][i] - sum_sq) ** 0.5
            else:
                sum_product = sum(L[i][k] * L[j][k] for k in range(j))
                L[i][j] = (A[i][j] - sum_product) / L[j][j]

    return L


A: list[list[int]] = [
    [4, 12, -16],
    [12, 37, -43],
    [-16, -43, 98]]

L: list[list[float]] = cholesky_decomposition(A)
print("Macierz L (dolna trójkątna):")
pprint.pprint(L)
