import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

# ==========================================
# Ввод данных
# ==========================================
nodes = ['A', 'B', 'C', 'D']
n = len(nodes)

# Ребра из предыдущего задания
edges = [
    ('A', 'B'), ('A', 'D'), 
    ('B', 'C'), ('B', 'D'), 
    ('C', 'D')
]

# ==========================================
# 1. Матрица весов неориентированного графа
# ==========================================
# По условию: вес AD = 3, остальные по 5.
# Создаем матрицу, заполненную бесконечностями (нет ребра)
weight_matrix = np.full((n, n), np.inf)

# Заполняем диагональ нулями
for i in range(n):
    weight_matrix[i][i] = 0

# Заполняем веса
for u, v in edges:
    u_idx = nodes.index(u)
    v_idx = nodes.index(v)
    
    if (u == 'A' and v == 'D') or (u == 'D' and v == 'A'):
        weight = 3
    else:
        weight = 5
        
    weight_matrix[u_idx][v_idx] = weight
    weight_matrix[v_idx][u_idx] = weight

print("--- 1. Матрица весов (неориентированный граф) ---")
# Заменяем inf на 0 для красивого вывода (или оставляем inf, если так просят)
print("(inf обозначает отсутствие ребра)")
print(weight_matrix)
print()

# ==========================================
# 2. Эксцентриситет и радиус графа
# ==========================================
# Создаем граф networkx с весами
G = nx.Graph()
for u, v in edges:
    w = 3 if (u == 'A' and v == 'D') or (u == 'D' and v == 'A') else 5
    G.add_edge(u, v, weight=w)

# Эксцентриситет вершины - это максимальное кратчайшее расстояние от этой вершины до любой другой
eccentricities = nx.eccentricity(G, weight='weight')

# Радиус графа - это минимальный эксцентриситет
radius = nx.radius(G, weight='weight')

print("--- 2. Эксцентриситет вершин и радиус графа ---")
for node, ecc in eccentricities.items():
    print(f"Эксцентриситет вершины {node}: {ecc}")
print(f"Радиус графа: {radius}")
print()

# ==========================================
# 3. Кратчайший путь между A и C (неориентированный)
# ==========================================
path_length = nx.shortest_path_length(G, source='A', target='C', weight='weight')
path = nx.shortest_path(G, source='A', target='C', weight='weight')

print("--- 3. Кратчайший путь между A и C (неориентированный) ---")
print(f"Длина кратчайшего пути: {path_length}")
print(f"Сам путь: {' -> '.join(path)}")
print()

# ==========================================
# 4. Ориентированный граф (против часовой стрелки)
# ==========================================
# Против часовой стрелки: A -> B -> C -> D -> A
# Исходя из картинки: A(справа), B(сверху), C(слева), D(снизу)
# A -> B (вверх), B -> C (влево), C -> D (вниз), D -> A (вправо)
# Также есть диагонали: B -> D и A -> D? 
# На картинке линии: A-B, B-C, C-D, D-A (периметр) и B-D, A-D (диагонали/внутренние)
# Против часовой стрелки по периметру: A->B, B->C, C->D, D->A
# Внутренние ребра: B->D и A->D (так как A->D идет справа налево-вниз, это против часовой)

DG = nx.DiGraph()

# Периметр против часовой: A -> B -> C -> D -> A
DG.add_edge('A', 'B', weight=5)
DG.add_edge('B', 'C', weight=5)
DG.add_edge('C', 'D', weight=5)
DG.add_edge('D', 'A', weight=3) # Вес AD = 3

# Внутренние ребра (против часовой):
# B -> D (сверху вниз) - против часовой
DG.add_edge('B', 'D', weight=5)
# A -> D (справа налево-вниз) - против часовой
DG.add_edge('A', 'D', weight=3) # Это ребро уже есть, но проверим

print("--- 4. Ориентированный граф (против часовой стрелки) ---")
print("Ребра ориентированного графа:")
for u, v, data in DG.edges(data=True):
    print(f"{u} -> {v} (вес: {data['weight']})")
print()

# ==========================================
# 5. Кратчайший путь между A и C (ориентированный)
# ==========================================
try:
    path_length_dir = nx.shortest_path_length(DG, source='A', target='C', weight='weight')
    path_dir = nx.shortest_path(DG, source='A', target='C', weight='weight')
    
    print("--- 5. Кратчайший путь между A и C (ориентированный) ---")
    print(f"Длина кратчайшего пути: {path_length_dir}")
    print(f"Сам путь: {' -> '.join(path_dir)}")
except nx.NetworkXNoPath:
    print("--- 5. Кратчайший путь между A и C (ориентированный) ---")
    print("Путь не существует!")
print()

# ==========================================
# 6. Визуализация графа
# ==========================================
plt.figure(figsize=(10, 5))

# Рисуем неориентированный граф
plt.subplot(1, 2, 1)
pos = {'A': (1, 0), 'B': (0, 1), 'C': (-1, 0), 'D': (0, -1)}
nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=800, font_weight='bold', font_size=14)
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, font_size=12)
plt.title("Неориентированный граф (веса)")

# Рисуем ориентированный граф
plt.subplot(1, 2, 2)
nx.draw(DG, pos, with_labels=True, node_color='lightgreen', node_size=800, font_weight='bold', font_size=14, arrows=True, arrowsize=20)
labels_dir = nx.get_edge_attributes(DG, 'weight')
nx.draw_networkx_edge_labels(DG, pos, edge_labels=labels_dir, font_size=12)
plt.title("Ориентированный граф (против часовой)")

plt.tight_layout()
plt.show()