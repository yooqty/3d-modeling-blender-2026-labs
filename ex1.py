import numpy as np

# 1. Ввод графа с помощью матрицы смежности
# Узлы: 1, 2, 3, 4 (индексы 0, 1, 2, 3)
# Связи: 1-2, 1-3, 1-4, 2-3, 3-4
A = np.array([
    [0, 1, 1, 1],  # связи узла 1 (с 2, 3, 4)
    [1, 0, 1, 0],  # связи узла 2 (с 1, 3)
    [1, 1, 0, 1],  # связи узла 3 (с 1, 2, 4)
    [1, 0, 1, 0]   # связи узла 4 (с 1, 3)
])

print("Матрица смежности A:")
print(A)
print("-" * 30)

# 2. Матрица Кирхгофа (L = D - A)
# D - диагональная матрица степеней вершин
degrees = np.sum(A, axis=1)
D = np.diag(degrees)
L = D - A

print("Матрица Кирхгофа L:")
print(L)
print("-" * 30)

# 3. Уравнение для расчета собственных значений
# Характеристическое уравнение: det(L - lambda * E) = 0
# Выведем его символьное представление (для понимания)
import sympy as sp
lam = sp.symbols('lambda')
L_sym = sp.Matrix(L)
char_eq = L_sym.charpoly(lam)
print("Уравнение для расчета собственных значений (det(L - lambda*I) = 0):")
print(char_eq.as_expr(), "= 0")
print("-" * 30)

# 4. Собственные значения и вектор Фидлера
# Используем numpy.linalg.eigh, так как матрица Кирхгофа симметричная
eigenvalues, eigenvectors = np.linalg.eigh(L)

# Сортируем (eigh уже сортирует по возрастанию, но для надежности)
idx = np.argsort(eigenvalues)
eigenvalues = eigenvalues[idx]
eigenvectors = eigenvectors[:, idx]

print("Собственные значения (отсортированы):")
print(np.round(eigenvalues, 4))
print("-" * 30)

# Вектор Фидлера - это собственный вектор, соответствующий второму по величине 
# (или первому ненулевому) собственному значению.
# Индекс 1, так как индекс 0 - это 0 (для связного графа).
fiedler_vector = eigenvectors[:, 1]
print("Вектор Фидлера (соответствует второму собственному значению):")
print(np.round(fiedler_vector, 4))