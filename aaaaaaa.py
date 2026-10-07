import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import sympy as sp

# ==========================================
# 1. Ввод графа с помощью матрицы смежности
# ==========================================
# Исходная матрица 3x3. Порядок вершин: A, B, D
nodes = ['A', 'B', 'D']
n = len(nodes)

adj_matrix = np.array([
    [0, 1, 1],
    [1, 0, 1],
    [1, 0, 1]
])

print("--- 1. Исходная матрица смежности (A, B, D) ---")
print(adj_matrix)
print()

# ==========================================
# 2. Создание ориентированного графа
# ==========================================
# Условие: ориентирован по часовой стрелке, направление от B к D.
# Логика: A -> B -> D -> A
# Проверим по матрице: есть ребра A-B, A-D, B-D.

edges_dir = [
    ('A', 'B'), # Направление от A к B
    ('B', 'D'), # Направление от B к D (по условию)
    ('D', 'A')  # Замыкаем цикл по часовой стрелке
]

DG = nx.DiGraph()
DG.add_nodes_from(nodes)
DG.add_edges_from(edges_dir)

print("--- 2. Ориентированный граф (по часовой стрелке) ---")
print("Ребра:")
for u, v in DG.edges():
    print(f"{u} -> {v}")
print()

# ==========================================
# 3. Матрица смежности ориентированного графа
# ==========================================
# Строка - откуда, Столбец - куда
adj_matrix_dir = np.zeros((n, n), dtype=int)

for u, v in DG.edges():
    u_idx = nodes.index(u)
    v_idx = nodes.index(v)
    adj_matrix_dir[u_idx][v_idx] = 1

print("--- 3. Матрица смежности ориентированного графа ---")
print(adj_matrix_dir)
print()

# ==========================================
# 4. Спектр графа (Собственные значения)
# ==========================================
# Для ориентированного графа спектр ищут для матрицы смежности.

eigenvalues = np.linalg.eigvals(adj_matrix_dir)

print("--- 4. Спектр графа (Собственные значения) ---")
for val in eigenvalues:
    print(f"{val:.4f}")
print()

# ==========================================
# 5. Характеристическое уравнение (для тетради)
# ==========================================
# Используем sympy для красивого вывода уравнения
lam = sp.Symbol('lambda')
I = sp.eye(n)
char_matrix = adj_matrix_dir - lam * I
char_poly = char_matrix.det()

print("--- 5. Характеристическое уравнение ---")
print(f"det(A - λI) = 0")
print(f"Уравнение: {sp.expand(char_poly)} = 0")
print()

# ==========================================
# 6. Визуализация графа
# ==========================================
plt.figure(figsize=(6, 6))
pos = {'A': (1, 0), 'B': (0, 1), 'D': (-1, -1)} 

nx.draw(DG, pos, with_labels=True, node_color='lightcoral', 
        node_size=1000, font_weight='bold', font_size=14, 
        arrows=True, arrowsize=25, edge_color='gray', width=2)

plt.title("Ориентированный граф (A -> B -> D -> A)")
plt.axis('off')
plt.show()