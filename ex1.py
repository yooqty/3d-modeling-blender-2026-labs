import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

# ==========================================
# ВИЗУАЛИЗАЦИЯ ГРАФА (Картинка)
# ==========================================
# Создаем граф
G = nx.Graph()

# Добавляем ребра (связи) согласно нашему графу
edges = [(1, 2), (1, 3), (1, 4), (2, 3), (3, 4)]
G.add_edges_from(edges)

# Задаем координаты вершин, чтобы граф выглядел как ромб (как на картинке)
pos = {
    1: (0, 1),    # Верхняя вершина
    2: (-1, 0),   # Левая вершина
    3: (1, 0),    # Правая вершина
    4: (0, -1)    # Нижняя вершина
}

# Настраиваем отрисовку
plt.figure(figsize=(5, 5))
nx.draw(G, pos, 
        with_labels=True, 
        node_color='red',      # Цвет вершин как на картинке
        node_size=800,         # Размер вершин
        font_color='white',    # Цвет текста внутри вершин
        font_weight='bold', 
        edge_color='gray',     # Цвет линий
        width=2)

plt.title("Исходный граф")
plt.axis('off') # Убираем оси координат
plt.show()

# ==========================================
# РАСЧЕТЫ (Осталось без изменений)
# ==========================================

# 1. Ввод графа с помощью матрицы смежности
A = np.array([
    [0, 1, 1, 1],  
    [1, 0, 1, 0],  
    [1, 1, 0, 1],  
    [1, 0, 1, 0]   
])

print("Матрица смежности A:")
print(A)
print("-" * 30)

# 2. Матрица Кирхгофа (L = D - A)
degrees = np.sum(A, axis=1)
D = np.diag(degrees)
L = D - A

print("Матрица Кирхгофа L:")
print(L)
print("-" * 30)

# 3. Уравнение для расчета собственных значений
import sympy as sp
lam = sp.symbols('lambda')
L_sym = sp.Matrix(L)
char_eq = L_sym.charpoly(lam)
print("Уравнение для расчета собственных значений (det(L - lambda*I) = 0):")
print(char_eq.as_expr(), "= 0")
print("-" * 30)

# 4. Собственные значения и вектор Фидлера
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