import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import sympy as sp

# ============================================================
# 1. Ввод графа с помощью матрицы смежности
# ============================================================
# Узлы: 1, 2, 3, 4 (индексы 0,1,2,3)
# Связи: 1-2, 1-3, 2-3, 2-4, 3-4
A = np.array([
    [0, 1, 1, 0],  # Узел 1
    [1, 0, 1, 1],  # Узел 2
    [1, 1, 0, 1],  # Узел 3
    [0, 1, 1, 0]   # Узел 4
])

print("="*60)
print("1. МАТРИЦА СМЕЖНОСТИ A:")
print("="*60)
print(A)

# ============================================================
# 2. Построение матрицы Кирхгофа L = D - A
# ============================================================
degrees = np.sum(A, axis=1)
D = np.diag(degrees)
L = D - A

print("\n" + "="*60)
print("2. МАТРИЦА КИРХГОФА L = D - A:")
print("="*60)
print("Матрица степеней D:")
print(D)
print("\nМатрица Кирхгофа L:")
print(L)

# ============================================================
# 3. Уравнение для расчёта собственных значений
#    det(L - λI) = 0
# ============================================================
print("\n" + "="*60)
print("3. УРАВНЕНИЕ ДЛЯ РАСЧЁТА СОБСТВЕННЫХ ЗНАЧЕНИЙ:")
print("="*60)

lam = sp.symbols('lambda')
L_sym = sp.Matrix(L)
I = sp.eye(4)
char_matrix = L_sym - lam * I
equation = char_matrix.det()

print("Характеристическая матрица (L - λI):")
sp.pprint(char_matrix)
print("\nУравнение det(L - λI) = 0:")
sp.pprint(sp.Eq(equation, 0))
print("\nРаскрытое уравнение:")
sp.pprint(sp.expand(equation))

# ============================================================
# 4. Собственные значения и вектор Фидлера
# ============================================================
eigenvalues, eigenvectors = np.linalg.eigh(L)  # eigh — для симметричных матриц

print("\n" + "="*60)
print("4. СОБСТВЕННЫЕ ЗНАЧЕНИЯ И ВЕКТОР ФИДЛЕРА:")
print("="*60)
print("Собственные значения (отсортированы по возрастанию):")
for i, val in enumerate(eigenvalues):
    print(f"  λ{i+1} = {val:.4f}")

# Вектор Фидлера — второй собственный вектор (индекс 1)
fiedler_vector = eigenvectors[:, 1]

# Приводим вектор к удобному для тетради виду (целые числа)
non_zero_vals = np.abs(fiedler_vector[np.abs(fiedler_vector) > 1e-5])
min_val = np.min(non_zero_vals)
fiedler_norm = fiedler_vector / min_val

# Делаем первую компоненту положительной для красоты
if fiedler_norm[0] < 0:
    fiedler_norm = -fiedler_norm

print("\nВектор Фидлера (сырой, из кода):")
print(np.round(fiedler_vector, 4))
print("\nВектор Фидлера (нормализованный для тетради):")
print(np.round(fiedler_norm, 4))

# Проверка: L * v = λ * v
print("\nПроверка L * v2 = λ2 * v2:")
print("L * v2 =", np.round(L @ fiedler_vector, 6))
print("λ2 * v2 =", np.round(eigenvalues[1] * fiedler_vector, 6))

# ============================================================
# 5. Разбиение на кластеры
# ============================================================
print("\n" + "="*60)
print("5. РАЗБИЕНИЕ НА КЛАСТЕРЫ:")
print("="*60)
print("Правило: элементы вектора Фидлера с одинаковым знаком относятся к одному кластеру.")
print(f"Вектор Фидлера: {np.round(fiedler_norm, 4)}")
cluster1 = []
cluster2 = []
for i, val in enumerate(fiedler_norm):
    if val >= 0:
        cluster1.append(i+1) # +1 так как индексы с 0
    else:
        cluster2.append(i+1)

print(f"Кластер 1 (положительные значения): Вершины {cluster1}")
print(f"Кластер 2 (отрицательные значения): Вершины {cluster2}")

# ============================================================
# 6. Визуализация: только исходный граф
# ============================================================
G = nx.from_numpy_array(A)
# Фиксируем позиции как на рисунке в задании (ромб)
pos = {0: (0.5, 1.0), 1: (0.0, 0.5), 2: (1.0, 0.5), 3: (0.5, 0.0)}

plt.figure(figsize=(6, 6))
nx.draw(G, pos, with_labels=[1,2,3,4], node_color='red',
        node_size=700, font_color='white', font_weight='bold', edge_color='gray')
plt.title("Исходный граф")
plt.show()