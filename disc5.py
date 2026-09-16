import numpy as np
from collections import deque

def main():
    # ============================================================
    # Пункт 2. Матрица смежности (вводим вручную для графа с картинки)
    # ============================================================
    # Порядок вершин: A, B, C, D (индексы 0,1,2,3)
    # Рёбра графа: A-B, A-D, B-C, B-D, C-D
    vertices = ['A', 'B', 'C', 'D']
    n = len(vertices)

    adj_matrix = np.array([
        [0, 1, 0, 1],  # A: связана с B и D
        [1, 0, 1, 1],  # B: связана с A, C, D
        [0, 1, 0, 1],  # C: связана с B и D
        [1, 1, 1, 0]   # D: связана с A, B, C
    ])

    print("=== Пункт 2. Матрица смежности ===")
    print("    " + "  ".join(vertices))
    for i, row in enumerate(adj_matrix):
        print(f"{vertices[i]}: {row}")

    # ============================================================
    # Пункт 3. Матрица инцидентности
    # ============================================================
    print("\n=== Пункт 3. Матрица инцидентности ===")

    # Находим все рёбра (верхний треугольник)
    edges = []
    for i in range(n):
        for j in range(i + 1, n):
            if adj_matrix[i][j] == 1:
                edges.append((i, j))

    # Обозначаем рёбра буквами e1, e2, ...
    edge_names = [f"e{k+1}" for k in range(len(edges))]
    print("Обозначение рёбер:")
    for name, (u, v) in zip(edge_names, edges):
        print(f"  {name} = ({vertices[u]}, {vertices[v]})")

    # Строим матрицу инцидентности (вершины × рёбра)
    inc_matrix = np.zeros((n, len(edges)), dtype=int)
    for e_idx, (u, v) in enumerate(edges):
        inc_matrix[u][e_idx] = 1
        inc_matrix[v][e_idx] = 1

    print("\nМатрица инцидентности:")
    print("     " + "  ".join(edge_names))
    for i, row in enumerate(inc_matrix):
        print(f"{vertices[i]}:  {row}")

    # ============================================================
    # Пункт 4. Матрица Кирхгофа
    # ============================================================
    print("\n=== Пункт 4. Матрица Кирхгофа ===")

    degree_matrix = np.diag(np.sum(adj_matrix, axis=1))
    kirchhoff = degree_matrix - adj_matrix

    print("Матрица Кирхгофа (L = D - A):")
    print("    " + "  ".join(vertices))
    for i, row in enumerate(kirchhoff):
        print(f"{vertices[i]}: {row}")

    # ============================================================
    # Пункт 5. Эксцентриситеты и радиус графа
    # ============================================================
    print("\n=== Пункт 5. Эксцентриситеты и радиус графа ===")

    # BFS для поиска кратчайших расстояний от каждой вершины
    def bfs(start):
        dist = [-1] * n
        dist[start] = 0
        queue = deque([start])
        while queue:
            u = queue.popleft()
            for v in range(n):
                if adj_matrix[u][v] == 1 and dist[v] == -1:
                    dist[v] = dist[u] + 1
                    queue.append(v)
        return dist

    dist_matrix = np.array([bfs(i) for i in range(n)])

    print("Матрица кратчайших расстояний:")
    print("    " + "  ".join(vertices))
    for i, row in enumerate(dist_matrix):
        print(f"{vertices[i]}: {row}")

    # Эксцентриситет — максимальное расстояние от вершины
    eccentricities = {}
    for i in range(n):
        ecc = int(np.max(dist_matrix[i]))
        eccentricities[vertices[i]] = ecc
        print(f"Эксцентриситет вершины {vertices[i]}: {ecc}")

    radius = min(eccentricities.values())
    diameter = max(eccentricities.values())

    print(f"\nРадиус графа: {radius}")
    print(f"Диаметр графа: {diameter}")

    # ============================================================
    # Пункт 6. Кратчайший путь между A и E (E нет на графе → ищем A и C)
    # ============================================================
    print("\n=== Пункт 6. Кратчайшее расстояние (в задании опечатка) ===")
    print("Вершины E на графе нет. Найдём расстояние между крайними вершинами A и C.")

    idx_A = vertices.index('A')
    idx_C = vertices.index('C')
    print(f"Кратчайшее расстояние между A и C: {dist_matrix[idx_A][idx_C]}")

    # Дополнительно: восстановим сам путь A → C
    def shortest_path(start, end):
        dist = [-1] * n
        parent = [-1] * n
        dist[start] = 0
        queue = deque([start])
        while queue:
            u = queue.popleft()
            if u == end:
                break
            for v in range(n):
                if adj_matrix[u][v] == 1 and dist[v] == -1:
                    dist[v] = dist[u] + 1
                    parent[v] = u
                    queue.append(v)
        # Восстанавливаем путь
        path = []
        cur = end
        while cur != -1:
            path.append(vertices[cur])
            cur = parent[cur]
        return path[::-1]

    path = shortest_path(idx_A, idx_C)
    print(f"Сам путь: {' → '.join(path)}")


if __name__ == "__main__":
    main()