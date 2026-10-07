import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import sympy as sp

# ==========================================
# 1. Ввод графа с помощью матрицы смежности
# ==========================================
nodes = ['A', 'B', 'D']
n = len(nodes)

# Исходная матрица (теперь с петлей у вершины A)
# 1 на диагонали означает петлю
adj_matrix = np.array([
    [1, 1, 1],  # A -> A (петля), A -> B, A -> D
    [1, 0, 1],  # B -> A, B -> D
    [1, 0, 1]   # D -> A, D -> D? (нет, 0)
])

print("--- 1. Исходная матрица смежности (с петлей у A) ---")
print(adj_matrix)
print()

# ==========================================
# 2. Создание ориентированного графа
# ==========================================
# Направление по часовой стрелке: A -> B -> D -> A
# Плюс петля у A: A -> A

edges_dir = [
    ('A', 'A'), # Петля
    ('A', 'B'), 
    ('B', 'D'), 
    ('D', 'A')  
]

DG = nx.DiGraph()
DG.add_nodes_from(nodes)
DG.add_edges_from(edges_dir)

print("--- 2. Ориентированный граф (с петлей) ---")
print("Ребра:")
for u, v in DG.edges():
    if u == v:
        print(f"{u} -> {v} (Петля)")
    else:
        print(f"{u} -> {v}")
print()

# ==========================================
# 3. Матрица смежности ориентированного графа
# ==========================================
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
eigenvalues = np.linalg.eigvals(adj_matrix_dir)

print("--- 4. Спектр графа ---")
for val in eigenvalues:
    print(f"{val:.4f}")
print()

# ==========================================
# 5. Характеристическое уравнение (для тетради)
# ==========================================
lam = sp.Symbol('lambda')
I = sp.eye(n)
char_matrix = adj_matrix_dir - lam * I
char_poly = char_matrix.det()

print("--- 5. Характеристическое уравнение ---")
print(f"det(A - λI) = 0")
print(f"Уравнение: {sp.expand(char_poly)} = 0")
print()

# ==========================================
# 6. Визуализация графа (с петлей)
# ==========================================
plt.figure(figsize=(6, 6))
pos = {'A': (1, 0), 'B': (0, 1), 'D': (-1, -1)} 

# Рисуем граф
nx.draw(DG, pos, with_labels=True, node_color='lightcoral', 
        node_size=1000, font_weight='bold', font_size=14, 
        arrows=True, arrowsize=25, edge_color='gray', width=2,
        connectionstyle='arc3, rad=0.2') # rad=0.2 изгибает петлю

plt.title("Ориентированный граф с петлей у A")
plt.axis('off')
plt.show()