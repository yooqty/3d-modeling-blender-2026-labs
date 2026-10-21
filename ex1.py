import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import sympy as sp

# --- 1. Ввод графа с помощью матрицы смежности ---
# Узлы: 1, 2, 3, 4 (индексы 0, 1, 2, 3)
A = np.array([
    [0, 1, 1, 1],  # 1
    [1, 0, 1, 0],  # 2
    [1, 1, 0, 1],  # 3
    [1, 0, 1, 0]   # 4
])

print("Матрица смежности A:")
print(A)
print("-" * 30)

# --- Отрисовка графа (картинкой) ---
G = nx.from_numpy_array(A)
# Задаем позиции узлов так, чтобы они образовывали ромб (как на картинке)
pos = {
    0: (0, 1),    # Вершина 1 (верх)
    1: (-1, 0),   # Вершина 2 (лево)
    2: (1, 0),    # Вершина 3 (право)
    3: (0, -1)    # Вершина 4 (низ)
}

plt.figure(figsize=(6, 6))
nx.draw_networkx_nodes(G, pos, node_color='red', node_size=800)
nx.draw_networkx_edges(G, pos, edge_color='gray', width=2)
nx.draw_networkx_labels(G, pos, labels={0: "1", 1: "2", 2: "3", 3: "4"}, 
                        font_color='white', font_weight='bold')
plt.title("Визуализация графа")
plt.axis('off') # Отключаем оси
plt.show() # Показываем картинку
# ------------------------------------

# --- 2. Матрица Кирхгофа (L = D - A) ---
degrees = np.sum(A, axis=1)
D = np.diag(degrees)
L = D - A

print("Матрица Кирхгофа L:")
print(L)
print("-" * 30)

# --- 3. Уравнение для расчета собственных значений ---
lam = sp.symbols('lambda')
L_sym = sp.Matrix(L)
char_eq = L_sym.charpoly(lam)
print("Уравнение для расчета собственных значений (det(L - lambda*I) = 0):")
print(char_eq.as_expr(), "= 0")
print("-" * 30)

# --- 4. Собственные значения и вектор Фидлера ---
eigenvalues, eigenvectors = np.linalg.eigh(L)
idx = np.argsort(eigenvalues)
eigenvalues = eigenvalues[idx]
eigenvectors = eigenvectors[:, idx]

print("Собственные значения (отсортированы):")
print(np.round(eigenvalues, 4))
print("-" * 30)

fiedler_vector = eigenvectors[:, 1]
print("Вектор Фидлера (соответствует второму собственному значению):")
print(np.round(fiedler_vector, 4))