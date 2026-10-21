import numpy as np
import sympy as sp
import networkx as nx
import matplotlib.pyplot as plt

# ==========================================
# 0. ВИЗУАЛИЗАЦИЯ ГРАФА (Картинка)
# ==========================================
# Создаем граф и добавляем ребра согласно заданию
G = nx.Graph()
edges = [(1, 2), (1, 3), (1, 4), (2, 3), (3, 4)]
G.add_edges_from(edges)

# Задаем позиции вершин "ромбом" как на картинке
pos = {
    1: (0, 1),    # верх
    2: (-1, 0),   # лево
    3: (1, 0),    # право
    4: (0, -1)    # низ
}

plt.figure(figsize=(5, 5))
nx.draw(G, pos, 
        with_labels=True, 
        node_color='red', 
        node_size=800, 
        font_color='white', 
        font_weight='bold',
        edge_color='gray',
        width=2)
plt.title("Граф из задания")
plt.show() # Показывает картинку

# ==========================================
# 1. Ввод графа с помощью матрицы смежности
# ==========================================
A = np.array([
    [0, 1, 1, 1],  # связи узла 1 (с 2, 3, 4)
    [1, 0, 1, 0],  # связи узла 2 (с 1, 3)
    [1, 1, 0, 1],  # связи узла 3 (с 1, 2, 4)
    [1, 0, 1, 0]   # связи узла 4 (с 1, 3)
])

print("Матрица смежности A:")
print(A)
print("-" * 30)

# ==========================================
# 2. Матрица Кирхгофа (L = D - A)
# ==========================================
degrees = np.sum(A, axis=1)
D = np.diag(degrees)
L = D - A

print("Матрица Кирхгофа L:")
print(L)
print("-" * 30)

# ==========================================
# 3. Уравнение для расчета собственных значений
# ==========================================
lam = sp.symbols('lambda')
L_sym = sp.Matrix(L)
char_eq = L_sym.charpoly(lam)
print("Уравнение для расчета собственных значений (det(L - lambda*I) = 0):")
print(char_eq.as_expr(), "= 0")
print("-" * 30)

# ==========================================
# 4. Собственные значения и вектор Фидлера
# ==========================================
eigenvalues, eigenvectors = np.linalg.eigh(L)

# Сортируем
idx = np.argsort(eigenvalues)
eigenvalues = eigenvalues[idx]
eigenvectors = eigenvectors[:, idx]

print("Собственные значения (отсортированы):")
print(np.round(eigenvalues, 4))
print("-" * 30)

# Вектор Фидлера (второй столбец, индекс 1)
fiedler_vector = eigenvectors[:, 1]
print("Вектор Фидлера:")
print(np.round(fiedler_vector, 4))