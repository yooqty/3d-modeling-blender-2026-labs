```import numpy as np
import sympy as sp
import networkx as nx
import matplotlib.pyplot as plt

# Включаем красивый вывод символов
sp.init_printing(use_unicode=True)

# ==========================================
# 1. ВВОД МАТРИЦЫ СМЕЖНОСТИ
# ==========================================
adj_matrix = np.array([
    [1, 1, 1],
    [1, 1, 1],
    [1, 0, 1]
], dtype=int)

print("1. Матрица смежности:")
print(adj_matrix)
print("-" * 30)

# ==========================================
# 2. РИСУНОК ГРАФА (с петлями)
# ==========================================
G = nx.Graph()

# Добавляем ребра (включая петли, если элемент на диагонали = 1)
rows, cols = adj_matrix.shape
for i in range(rows):
    for j in range(i, cols): # Проходим по верхнему треугольнику + диагональ
        if adj_matrix[i, j] == 1:
            G.add_edge(i+1, j+1)

pos = nx.circular_layout(G)

plt.figure(figsize=(6, 6))
# Рисуем вершины
nx.draw_networkx_nodes(G, pos, node_size=700, node_color='lightgreen', edgecolors='black')
# Рисуем обычные ребра (без петель)
edges_no_loops = [(u, v) for u, v in G.edges() if u != v]
nx.draw_networkx_edges(G, pos, edgelist=edges_no_loops, width=2, edge_color='gray')
# Рисуем петли (рисуем их как маленькие дуги)
loops = [(u, v) for u, v in G.edges() if u == v]
for u, v in loops:
    # Рисуем петлю вручную, так как networkx не всегда делает это красиво
    circle = plt.Circle((pos[u][0], pos[u][1]), 0.1, color='gray', fill=False, linewidth=2)
    plt.gca().add_patch(circle)

nx.draw_networkx_labels(G, pos, font_size=16, font_weight='bold')

plt.title("Граф с петлями (Задание 3)")
plt.axis('off')
plt.show()

# ==========================================
# 3. СПЕКТР МАТРИЦЫ (ТОЧНЫЙ РАСЧЕТ)
# ==========================================
print("2. Спектр матрицы смежности (собственные значения):")

M_sym = sp.Matrix(adj_matrix)
# Получаем собственные значения точно
eigen_dict = M_sym.eigenvals()

# Выводим красиво
unique_eigenvalues = list(eigen_dict.keys())

for i, val in enumerate(unique_eigenvalues):
    # Упрощаем выражение
    simplified_val = sp.simplify(val)
    # Выводим в формате lambda_i = значение
    sp.pprint(sp.Eq(sp.Symbol(f'lambda_{i+1}'), simplified_val))

print("\nИли в виде множества:")
sp.pprint(sp.FiniteSet(*unique_eigenvalues))
print("-" * 30)

# ==========================================
# 4. ОПРЕДЕЛИТЕЛЬ (для проверки)
# ==================================