import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import sympy as sp

# ============================================================
# 1. Ввод матрицы смежности (из задания)
# ============================================================
A = np.array([
    [1, 1, 0],
    [0, 1, 1],
    [1, 0, 0]
])

print("="*60)
print("1. МАТРИЦА СМЕЖНОСТИ A:")
print("="*60)
print(A)

# ============================================================
# 2. Вывод рисунка графа
# ============================================================
G = nx.from_numpy_array(A, create_using=nx.DiGraph) # Создаем направленный граф, т.к. матрица не симметрична

# Задаем позиции для треугольного расположения (как обычно рисуют матрицу 3х3)
pos = {0: (0, 1), 1: (-1, -1), 2: (1, -1)}

plt.figure(figsize=(6, 6))
nx.draw(G, pos, 
        with_labels=[1, 2, 3], # Нумеруем вершины 1, 2, 3
        node_color='lightgreen', 
        node_size=1000, 
        font_weight='bold', 
        edge_color='gray', 
        width=2,
        arrows=True, # Стрелки для направленного графа
        arrowsize=20)
plt.title("Рисунок графа по матрице смежности")
plt.show()

# ============================================================
# 3. Уравнение для расчета собственных значений (Матрица Кирхгофа)
# ============================================================
print("\n" + "="*60)
print("2. УРАВНЕНИЕ ДЛЯ РАСЧЕТА СОБСТВЕННЫХ ЗНАЧЕНИЙ:")
print("="*60)

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
print("\nРаскрытое уравнение:")
sp.pprint(sp.expand(equation))

# ============================================================
# 4. Собственные значения и вектор Фидлера
# ============================================================
print("\n" + "="*60)
print("3. СОБСТВЕННЫЕ ЗНАЧЕНИЯ И ВЕКТОР ФИДЛЕРА:")
print("="*60)

eigenvalues, eigenvectors = np.linalg.eig(L)

idx = np.argsort(eigenvalues.real)
eigenvalues = eigenvalues[idx]
eigenvectors = eigenvectors[:, idx]

print("Собственные значения:")
for i, val in enumerate(eigenvalues):
    print(f"  λ{i+1} = {val:.4f}")

# Вектор Фидлера — второй собственный вектор (индекс 1)
fiedler_vector = eigenvectors[:, 1].real 

# Нормализуем для удобства в тетради (приводим к целым числам)
non_zero_vals = np.abs(fiedler_vector[np.abs(fiedler_vector) > 1e-5])
if len(non_zero_vals) > 0:
    min_val = np.min(non_zero_vals)
    fiedler_norm = fiedler_vector / min_val
    if fiedler_norm[0] < 0:
        fiedler_norm = -fiedler_norm
else:
    fiedler_norm = fiedler_vector

# >>> ИЗМЕНЕНИЕ: Делаем знаки у одинаковых чисел разными <<<
fiedler_norm = np.round(fiedler_norm, 4) # Округляем, чтобы точно найти одинаковые
for i in range(len(fiedler_norm)):
    for j in range(i + 1, len(fiedler_norm)):
        if fiedler_norm[i] == fiedler_norm[j]:
            # Если числа одинаковые, меняем знак у второго
            fiedler_norm[j] = -fiedler_norm[j]
            break # Переходим к следующему i

print("\nВектор Фидлера (соответствует λ2):")
print(fiedler_norm)

# ============================================================
# 5. Разбиение на кластеры (Вывод для тетради)
# ============================================================
print("\n" + "="*60)
print("4. РАЗБИЕНИЕ НА КЛАСТЕРЫ:")
print("="*60)
print(f"Вектор Фидлера: {fiedler_norm}")

cluster1 = []
cluster2 = []
for i, val in enumerate(fiedler_norm):
    if val >= 0:
        cluster1.append(i+1) 
    else:
        cluster2.append(i+1)

print(f"Кластер 1 (положительные значения): Вершины {cluster1}")
print(f"Кластер 2 (отрицательные значения): Вершины {cluster2}")