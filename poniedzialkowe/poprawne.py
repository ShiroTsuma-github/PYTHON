import math
from funcy import print_durations
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import networkx as nx
from matplotlib.widgets import Slider, Button


SIZE = 4
DISPLAY_PARTIAL_TABLES = True
DISPLAY_FULL_TABLE = False
FLOW = True
FLOW_CHART_SHELL = True
FLOW_CHART_TREE = True
PLOT = True


def generate_pos_def_matrix(n):
    A = np.random.randint(1, 10, size=(n, n))
    A = 0.5 * (A + A.T)
    while not np.all(np.linalg.eigvals(A) > 0):
        A = A + n * np.eye(n, dtype=int)
    return A


@print_durations()
def Cholesky_Decomposition(a) -> list[list[float]]:
    N = len(a)
    L: list[list[float]] = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        a[i][i] = math.sqrt(a[i][i])
        for j in range(i + 1, N):
            a[j][i] = a[j][i] / a[i][i]
        for j in range(i + 1, N):
            for k in range(i + 1, j + 1):
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
    pd.s_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)

# Wydrukuj DataFrame
print(df)

dependencies_df = pd.DataFrame(columns=['From', 'To'])
last_occurrence = {}
unique_paris = set()
for index, row in df.iterrows():
    operands = [row['i, i'], row['j, i'], row['j, k'], row['k, i']]
    for order, operand in enumerate(operands):
        if operand:
            from_values = tuple(last_occurrence.get(operand, {'i': row["i"], 'j': row["j"], 'k': row["k"]}).values())
            to_values = tuple({'i': row['i'], 'j': row['j'], 'k': row['k']}.values())
            if str(from_values) + str(to_values) not in unique_paris:
                dependencies_df = pd.concat([dependencies_df, pd.DataFrame({
                    'From': [from_values],
                    'To': [to_values],
                    'Type': ['Move data' if from_values != to_values else 'Calculate']
                })], ignore_index=True)
                last_occurrence[operand] = {'i': row['i'], 'j': row['j'], 'k': row['k']}
                unique_paris.add(str(from_values) + str(to_values))
dependencies_df = dependencies_df.sort_values(by=['To', 'From'])
dependencies_df = dependencies_df.reset_index(drop=True)
dependencies_df = pd.concat([dependencies_df, pd.DataFrame({
    'From': [(SIZE, SIZE, SIZE)],
    'To': [(SIZE, SIZE, SIZE)],
    'Type': ['Calculate']
})], ignore_index=True)
print(dependencies_df)

if FLOW:
    G = nx.DiGraph()
    for _, row in dependencies_df.iterrows():
        if row['Type'] == 'Move data':
            G.add_edge(row['From'], row['To'], weight=row['Type'])

    # Perform topological sorting for "Move data" dependencies
    try:
        topological_order = list(nx.topological_sort(G))
    except nx.NetworkXUnfeasible:
        print("Cycle detected in 'Move data' dependencies")

    # Display the topological order
    print("\n\nTopological Order for 'Move data' dependencies:")
    [print(f'{i + 1}: {topological_order[i]}') for i in range(len(topological_order))]

    # Visualize the graph (optional)
    if FLOW_CHART_SHELL:
        plt.figure()
        plt.title('Cholesky Decomposition Flow Chart (Shell Layout))')
        pos = nx.shell_layout(G)
        nx.draw(G, pos, with_labels=True, font_weight='bold', node_size=700, node_color='lightblue')
    if FLOW_CHART_TREE:
        plt.figure()
        plt.title('Cholesky Decomposition Flow Chart (Tree Layout))')
        tree = nx.bfs_tree(G, source=topological_order[0])
        pos = nx.spring_layout(tree)
        nx.draw(tree, pos, with_labels=True, font_weight='bold', node_size=700, node_color='lightblue')
        


def draw_x_arrows(z_val=None):
    arrows_x = []
    if z_val is None:
        for i in range(len(df) - 1):
            num_arrows = len(df) - i
            if df['j'].iloc[i] != df['j'].max():  # Avoid drawing arrows when x=size
                arrows_x.append(ax.quiver(df['j'].iloc[i] * np.ones(num_arrows),
                                df['k'].iloc[i] * np.ones(num_arrows),
                                df['i'].iloc[i] * np.ones(num_arrows),
                                np.ones(num_arrows), np.zeros(num_arrows), np.zeros(num_arrows),
                                color='red', arrow_length_ratio=0.1))
    else:
        for i in range(len(df) - 1):
            num_arrows = len(df) - i
            if df['i'].iloc[i] == z_val:
                if df['j'].iloc[i] != df['j'].max():  # Avoid drawing arrows when x=size
                    arrows_x.append(ax.quiver(df['j'].iloc[i] * np.ones(num_arrows),
                                    df['k'].iloc[i] * np.ones(num_arrows),
                                    df['i'].iloc[i] * np.ones(num_arrows),
                                    np.ones(num_arrows), np.zeros(num_arrows), np.zeros(num_arrows),
                                    color='red', arrow_length_ratio=0.1))
    return arrows_x


def draw_y_arrows(z_val=None):
    arrows_y = []
    if z_val is None:
        for i in range(len(df) - 1, 0, -1):
            num_arrows = len(df) - i
            if df['k'].iloc[i] < df['j'].iloc[i]:
                arrows_y.append(ax.quiver(df['j'].iloc[i] * np.ones(num_arrows),
                                df['k'].iloc[i] * np.ones(num_arrows),
                                df['i'].iloc[i] * np.ones(num_arrows),
                                np.zeros(num_arrows), np.ones(num_arrows), np.zeros(num_arrows),
                                color='red', arrow_length_ratio=0.1))
    else:
        for i in range(len(df) - 1, 0, -1):
            num_arrows = len(df) - i
            if df['i'].iloc[i] == z_val and df['k'].iloc[i] < df['j'].iloc[i]:
                arrows_y.append(ax.quiver(df['j'].iloc[i] * np.ones(num_arrows),
                                df['k'].iloc[i] * np.ones(num_arrows),
                                df['i'].iloc[i] * np.ones(num_arrows),
                                np.zeros(num_arrows), np.ones(num_arrows), np.zeros(num_arrows),
                                color='red', arrow_length_ratio=0.1))
    return arrows_y


def draws_z_arrows(z_val=None):
    arrows_min_mul = []
    arrows_other = []
    if z_val is None:
        for i in range(0, len(df)):
            if df['op'].iloc[i] == 'min mul':
                color = 'red'
                arrow_length_ratio = 0.1
                arrows_min_mul.append(ax.quiver(df['j'].iloc[i], df['k'].iloc[i], df['i'].iloc[i],
                                      0, 0, 1, color=color, arrow_length_ratio=arrow_length_ratio))
            else:
                color = 'green'
                arrow_length_ratio = 0.05  # Adjust the length for green arrows
                arrows_other.append(ax.quiver(df['j'].iloc[i], df['k'].iloc[i], df['i'].iloc[i],
                                    0, 0, 1, color=color, arrow_length_ratio=arrow_length_ratio))
    else:
        for i in range(len(df)):
            if df['op'].iloc[i] == 'min mul' and df['i'].iloc[i] == z_val:
                color = 'red'
                arrow_length_ratio = 0.1
                arrows_min_mul.append(ax.quiver(df['j'].iloc[i], df['k'].iloc[i], df['i'].iloc[i],
                                      0, 0, 1, color=color, arrow_length_ratio=arrow_length_ratio))
            elif df['i'].iloc[i] == z_val:
                color = 'green'
                arrow_length_ratio = 0.05  # Adjust the length for green arrows
                arrows_other.append(ax.quiver(df['j'].iloc[i], df['k'].iloc[i], df['i'].iloc[i],
                                    0, 0, 1, color=color, arrow_length_ratio=arrow_length_ratio))
    return arrows_min_mul, arrows_other


def update(val):
    z_val = round(z_slider.val)
    global arrows_x
    global arrows_y
    global arrows_min_mul
    global arrows_other
    global scatter
    for arrow in arrows_min_mul:
        arrow.remove()
    for arrow in arrows_other:
        arrow.remove()
    for arrow in arrows_x:
        arrow.remove()
    for arrow in arrows_y:
        arrow.remove()

    arrows_min_mul.clear()
    arrows_other.clear()
    arrows_x.clear()
    arrows_y.clear()
    arrows_min_mul, arrows_other = draws_z_arrows(z_val)
    arrows_x = draw_x_arrows(z_val)
    arrows_y = draw_y_arrows(z_val)
    mask = (z == z_val)
    scatter.remove()
    scatter = ax.scatter(x[mask], y[mask], z[mask], c=op_colors[mask], marker='o', s=100)
    ax.set_zlim([z_val - 0.5, z_val + 0.5])
    ax.set_xticks(np.arange(1, SIZE + 1, 1))
    ax.set_yticks(np.arange(1, SIZE + 1, 1))
    ax.set_zticks(np.arange(1, SIZE + 1, 1))
    plt.draw()


def reset(event):
    global arrows_x
    global arrows_y
    global arrows_min_mul
    global arrows_other
    global scatter

    z_slider.reset()
    z_slider.set_val(0)

    scatter.remove()
    scatter = ax.scatter(initial_state['x'], initial_state['y'], initial_state['z'],
                        c=initial_state['op_colors'], marker='o', s=100)
    ax.set_zlim([z.min() - 0.5, z.max() + 0.5])
    ax.set_xticks(np.arange(1, SIZE + 1, 1))
    ax.set_yticks(np.arange(1, SIZE + 1, 1))
    ax.set_zticks(np.arange(1, SIZE + 1, 1))

    arrows_x = draw_x_arrows()
    arrows_y = draw_y_arrows()
    arrows_min_mul, arrows_other = draws_z_arrows()
    plt.draw()


if PLOT:
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    x = df['j']
    y = df['k']
    z = df['i']

    colors = {'sqrt': 'red', 'div': 'blue', 'min mul': 'purple'}
    op_colors = df['op'].map(colors)

    c = df['op'].map(colors)

    scatter = ax.scatter(x, y, z, c=op_colors, marker='o', s=100)

    #  Set labels and ticks
    ax.set_xlabel('j')
    ax.set_ylabel('k')
    ax.set_zlabel('i')

    ax.set_xticks(np.arange(1, SIZE + 1, 1))
    ax.set_yticks(np.arange(1, SIZE + 1, 1))
    ax.set_zticks(np.arange(1, SIZE + 1, 1))

    plt.title('Cholesky Decomposition')

    arrows_x = draw_x_arrows()
    arrows_y = draw_y_arrows()
    arrows_min_mul, arrows_other = draws_z_arrows()

    ax_z_slider = plt.axes([0.1, 0.02, 0.65, 0.03], facecolor='lightgoldenrodyellow')
    z_slider = Slider(ax_z_slider, 'Z Value', df['i'].min(), df['i'].max(), valstep=1)
    z_slider.set_val(0)

    ax_reset_button = plt.axes([0.85, 0.02, 0.1, 0.03])
    reset_button = Button(ax_reset_button, 'Reset', color='lightgoldenrodyellow', hovercolor='0.975')
    initial_state = {
        'x': x,
        'y': y,
        'z': z,
        'op_colors': op_colors
    }

    z_slider.on_changed(update)
    reset_button.on_clicked(reset)

if PLOT or FLOW_CHART_SHELL or FLOW_CHART_TREE:
    plt.show()
