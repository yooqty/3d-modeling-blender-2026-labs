import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import sympy as sp

# ============================================================
# 1. Ввод графа с помощью матрицы смежности
# ============================================================
A = np.array([
    [1, 1, 1],
    [1, 1, 1],
    [1, 0, 1]
])

print("="*60)
print("1. МАТРИЦА СМЕЖНОСТИ A:")
print("="*60)
print(A)

# ============================================================
# 2. Вывод спектра графа и рисунка (обозначение ребер)
# ============================================================
print("\n" + "="*60)
print("1. СПЕКТР ГРАФА (ребра):")
print("="*60)

G = nx.from_numpy_array(A)
edges = list(G.edges())
print(f"Ребра графа: {edges}")
print("Петли (вершина соединена сама с собой):", list(nx.selfloop_edges(G)))

# Рисуем граф
pos = {0: (0, 1), 1: (-1, -1), 2: (1, -1)}
plt.figure(figsize=(6, 6))
nx.draw(G, pos, 
        with_labels=[1, 2, 3], 
        node_color='lightblue', 
        node_size=1000, 
        font_weight='bold', 
        edge_color='gray', 
        width=2)
plt.title("Спектр графа из Задания 3")
plt.show()

# ============================================================
# 3. Уравнение для расчета собственных значений
# ============================================================
print("\n" + "="*60)
print("2. УРАВНЕНИЕ ДЛЯ РАСЧЕТА СОБСТВЕННЫХ ЗНАЧЕНИЙ:")
print("="*60)

# Для графа с петлями (на диагонали 1), матрица степеней D 
# считается как сумма элементов в строке (петля дает +1 к степени в учебных задачах)
degrees = np.sum(A, axis=1)
D = np.diag(degrees)
L = D - A

print("Матрица степеней D:")
print(D)
print("\nМатрица Кирхгофа L = D - A:")
print(L)

lam = sp.symbols('lambda')
L_sym = sp.Matrix(L)
I = sp.eye(3)
char_matrix = L_sym - lam * I
equation = char_matrix.det()

print("\nХарактеристическая матрица (L - λI):")
sp.pprint(char_matrix)
print("\nУравнение det(L - λI) = 0:")
sp.pprint(sp.Eq(equation, 0))

# ============================================================
# 4. Собственные значения и вектор Фидлера
# ============================================================
print("\n" + "="*60)
print("3. СОБСТВЕННЫЕ ЗНАЧЕНИЯ И ВЕКТОР ФИДЛЕРА:")
print("="*60)

# Используем eigh для симметричных матриц
eigenvalues, eigenvectors = np.linalg.eigh(L)

# Сортируем
idx = np.argsort(eigenvalues)
eigenvalues = eigenvalues[idx]
eigenvectors = eigenvectors[:, idx]

print("Собственные значения (отсортированы):")
print(np.round(eigenvalues, 4))

# Вектор Фидлера — второй собственный вектор (индекс 1)
fiedler_vector = eigenvectors[:, 1]

# Нормализуем для удобства
non_zero_vals = np.abs(fiedler_vector[np.abs(fiedler_vector) > 1e-5])
if len(non_zero_vals) > 0:
    min_val = np.min(non_zero_vals)
    fiedler_norm = fiedler_vector / min_val
    if fiedler_norm[0] < 0:
        fiedler_norm = -fiedler_norm
else:
    fiedler_norm = fiedler_vector

fiedler_norm = np.round(fiedler_norm, 4)

print("\nВектор Фидлера (соответствует λ2):")
print(fiedler_norm)

# ============================================================
# 5. Разбиение на кластеры
# ============================================================
print("\n" + "="*60)
print("4. РАЗБИЕНИЕ НА КЛАСТЕРЫ:")
print("="*60)

cluster1 = []
cluster2 = []
for i, val in enumerate(fiedler_norm):
    if val >= 0:
        cluster1.append(i+1) 
    else:
        cluster2.append(i+1)

print(f"Вектор Фидлера: {fiedler_norm}")
print(f"Кластер 1 (>=0): Вершины {cluster1}")
print(f"Кластер 2 (<0):  Вершины {cluster2}")