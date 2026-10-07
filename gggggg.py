import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

# --- 1. Ввод графа с помощью матрицы смежности ---
# Вершины: A, B, C, D. Пронумеруем их для удобства: 0:A, 1:B, 2:C, 3:D
# Связи (ребра) из картинки:
# A-B, A-D, B-C, B-D, C-D
# (Ребра: AB, AD, BC, BD, CD - всего 5 ребер)

nodes = ['A', 'B', 'C', 'D']
n = len(nodes)

# Инициализация матрицы смежности нулями
adj_matrix = np.zeros((n, n), dtype=int)

# Заполнение матрицы смежности (1 = есть ребро, 0 = нет)
edges = [
    (0, 1), # A-B
    (0, 3), # A-D
    (1, 2), # B-C
    (1, 3), # B-D
    (2, 3)  # C-D
]

for u, v in edges:
    adj_matrix[u][v] = 1
    adj_matrix[v][u] = 1

print("--- 1. Матрица смежности ---")
print(adj_matrix)
print(f"Обозначение ребер: {[(nodes[u], nodes[v]) for u, v in edges]}\n")


# --- 2. Матрица инцидентности ---
# Строки = Вершины, Столбцы = Ребра
# 1, если вершина является началом ребра; -1, если конец (для ориентированного), 
# но для неориентированного графа обычно ставят 1 для обоих концов.
# Здесь используем стандарт: 1 - инцидентна, 0 - нет.

inc_matrix = np.zeros((n, len(edges)), dtype=int)

for j, (u, v) in enumerate(edges):
    inc_matrix[u][j] = 1
    inc_matrix[v][j] = 1

print("--- 2. Матрица инцидентности ---")
print(inc_matrix)
print()


# --- 3. Матрица Кирхгофа и матрица Лапласа ---
# Для неориентированного графа они совпадают.
# L = D - A, где D - матрица степеней (диагональная), A - матрица смежности.

# Матрица степеней (Degree Matrix)
degree_matrix = np.diag(np.sum(adj_matrix, axis=1))

# Матрица Лапласа (L = D - A)
laplacian_matrix = degree_matrix - adj_matrix

print("--- 3. Матрица Кирхгофа (Лапласа) ---")
print(laplacian_matrix)
print()


# --- 4. Спектр графа ---
# Собственные значения матрицы Лапласа
eigenvalues = np.linalg.eigvals(laplacian_matrix)

# Сортировка для красоты
eigenvalues = np.sort(eigenvalues)

print("--- 4. Спектр графа (Собственные значения) ---")
print(np.round(eigenvalues, 4))

# Вывод уравнения на 2-м шаге (Характеристическое уравнение)
# Для матрицы 4x4 уравнение имеет вид: λ^4 - c1*λ^3 + c2*λ^2 - c3*λ + c4 = 0
# Коэффициенты можно найти через np.poly

coeffs = np.poly(laplacian_matrix) # Возвращает коэффициенты полинома
print("\nХарактеристическое уравнение (коэффициенты при λ^n):")
print(f"{coeffs[0]:.0f}*λ^4 + {coeffs[1]:.0f}*λ^3 + {coeffs[2]:.0f}*λ^2 + {coeffs[3]:.0f}*λ + {coeffs[4]:.0f} = 0")

print("\n(Примечание: для матрицы Лапласа сумма всех собственных значений равна сумме степеней вершин (2*кол-во ребер = 10), а одно из значений всегда равно 0)")

# --- Визуализация (бонус) ---
G = nx.Graph()
G.add_edges_from([(nodes[u], nodes[v]) for u, v in edges])
pos = {'A': (1, 0), 'B': (0, 1), 'C': (-1, 0), 'D': (0, -1)} # Примерные координаты как на картинке
nx.draw(G, pos, with_labels=True, node_color='red', node_size=500, font_color='white', font_weight='bold')
plt.title("Визуализация графа")
plt.show()