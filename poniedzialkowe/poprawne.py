import math
from funcy import print_durations
import numpy as np
import pandas as pd


DISPLAY_PARTIAL_TABLES = False
DISPLAY_FULL_TABLE = False
SIZE = 10


def generate_pos_def_matrix(n):
    A = np.random.randint(1, 10, size=(n, n))
    A = 0.5 * (A + A.T)
    while not np.all(np.linalg.eigvals(A) > 0):
        A = A + n * np.eye(n, dtype=int)
    return A


@print_durations()
def Cholesky_Decomposition(a) -> list[list[float]]:
    N = len(a)
    z = 0
    L: list[list[float]] = [[0 for _ in range(N)] for _ in range(N)]
    # print(' id   i j k a[j][i] a[i][k] a[j][k]      op')
    for i in range(N):
        z += 1
        # print(f'[{str(z).ljust(2, " ")}]: {i + 1} {i + 1} {i + 1}  {(i + 1, i + 1)}  {(i + 1, i + 1)}  {(i + 1, i + 1)} \tsqrt')
        a[i][i] = math.sqrt(a[i][i])
        for j in range(i + 1, N):
            z += 1
            # print(f'[{str(z).ljust(2, " ")}]: {i + 1} {j + 1} {i + 1}  {(j + 1, i + 1)}  {(i + 1, i + 1)}  {(j + 1, i + 1)} \tdiv')
            a[j][i] = a[j][i] / a[i][i]
        for j in range(i + 1, N):
            for k in range(i + 1, j + 1):
                z += 1
                # print(f'[{str(z).ljust(2, " ")}]: {i + 1} {j + 1} {k + 1}  {(j + 1, i + 1)}  {(i + 1, k + 1)}  {(j + 1, k + 1)} \tmin mul')
                a[j][k] = a[j][k] - a[j][i] * a[k][i]

    # do wyciagania i >= j    
    for i in range(N):
        for j in range(i + 1):
            if i >= j:
                L[i][j] = a[i][j]
    return L


matrix = generate_pos_def_matrix(SIZE)
L: list[list[float]] = Cholesky_Decomposition(matrix.copy())
L_np = np.array(L)
Lt_np = L_np.transpose()

original_matrix = np.dot(L_np, Lt_np)
original_matrix = original_matrix

z = 0
result_dict = {}
a = matrix.copy()
if DISPLAY_PARTIAL_TABLES:
    print(' id   i j k\t i, i \t\t op')
for i in range(SIZE):
    for j in range(i, i + 1):
        for k in range(i, i + 1):
            if DISPLAY_PARTIAL_TABLES:
                print(f'[{str(z).ljust(2, " ")}]: {i + 1} {j + 1} {k + 1}\t{(i+1, i+1)}  \tsqrt')
            result_dict[f'{i+1}{j+1}{k+1}'] = {
                'z': z,
                'i': i + 1,
                'j': j + 1,
                'k': k + 1,
                'op': 'sqrt',
                'operands':
                {
                    'ii': (i + 1, i + 1)
                }
            }
            a[i][i] = math.sqrt(a[i][i])
            z += 1
if DISPLAY_PARTIAL_TABLES:
    print('\n\n')
    print(' id   i j k\t j, i \t i, i \t\t op')
z = 0
for i in range(SIZE):
    for j in range(i + 1, SIZE):
        for k in range(i, i + 1):
            if DISPLAY_PARTIAL_TABLES:
                print(f'[{str(z).ljust(2, " ")}]: {i + 1} {j + 1} {k + 1}\t{(j + 1, k + 1)}\t{(i + 1, i + 1)}  \tdiv')
            result_dict[f'{i+1}{j+1}{k+1}'] = {
                'z': z,
                'i': i + 1,
                'j': j + 1,
                'k': k + 1,
                'op': 'div',
                'operands':
                {
                    'ji': (j + 1, i + 1),
                    'ii': (i + 1, i + 1)
                }
            }
            a[j][i] = a[j][i] / a[i][i]
            z += 1
if DISPLAY_PARTIAL_TABLES:
    print('\n\n')
    print(' id   i j k\t j, k \t j, i \t k, i \t\t  op')
z = 0
for i in range(SIZE):
    for j in range(i + 1, SIZE):
        for k in range(i + 1, j + 1):
            if DISPLAY_PARTIAL_TABLES:
                print(f'[{str(z).ljust(2, " ")}]: {i + 1} {j + 1} {k + 1}\t{(j + 1, k + 1)}\t{(j + 1, i + 1)}\t{(k + 1, i + 1)}  \tmin mul')
            result_dict[f'{i+1}{j+1}{k+1}'] = {
                'z': z,
                'i': i + 1,
                'j': j + 1,
                'k': k + 1,
                'op': 'min mul',
                'operands':
                {
                    'jk': (j + 1, k + 1),
                    'ji': (j + 1, i + 1),
                    'ki': (k + 1, i + 1)
                }
            }
            a[j][k] = a[j][k] - a[j][i] * a[k][i]
            z += 1
print('\n\n')
# pprint.pprint(result_dict)

ids = []
i_values = []
j_values = []
k_values = []
ji_values = []
jk_values = []
ki_values = []
ii_values = []
op_values = []

# Przejdź przez słownik i dodaj dane do list
for key, value in result_dict.items():
    i = value['i']
    j = value['j']
    k = value['k']
    ii = value['operands'].get('ii', '')
    ji = value['operands'].get('ji', '')
    jk = value['operands'].get('jk', '')
    ki = value['operands'].get('ki', '')
    op = value['op']

    ids.append(int(key))
    i_values.append(i)
    j_values.append(j)
    k_values.append(k)
    ii_values.append(ii)
    ji_values.append(ji)
    jk_values.append(jk)
    ki_values.append(ki)
    op_values.append(op)

# Stwórz DataFrame z danymi
df = pd.DataFrame({
    'i': i_values,
    'j': j_values,
    'k': k_values,
    'i, i': ii_values,
    'j, i': ji_values,
    'j, k': jk_values,
    'k, i': ki_values,
    'op': op_values
})
df = df.sort_values(by=['i', 'j', 'k'])

# Zresetuj indeksy DataFrame
df = df.reset_index(drop=True)

if DISPLAY_FULL_TABLE:
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)

# Wydrukuj DataFrame
print(df)
