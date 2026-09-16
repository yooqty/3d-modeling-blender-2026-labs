import numpy as np

def main():
    # === Пункт 2: Ввод графа с помощью матрицы смежности ===
    # Вершины: 0=C, 1=B, 2=D, 3=A (для удобства индексации)
    # Но для вывода будем использовать буквы
    vertices = ['C', 'B', 'D', 'A']
    n = len(vertices)
    
    print("=== Пункт 2: Матрица смежности ===")
    print("Введите матрицу смежности 4x4 (строки через пробел).")
    print("Порядок вершин: C, B, D, A")
    print("Пример ввода для данного графа:")
    print("0 1 1 0")
    print("1 0 1 1")
    print("1 1 0 1")
    print("0 1 1 0")
    print("-" * 30)

    adj_matrix = []
    for i in range(n):
        while True:
            try:
                row = list(map(int, input(f"Строка {vertices[i]}: ").split()))
                if len(row) == n:
                    adj_matrix.append(row)
                    break
                else:
                    print(f"Ошибка: нужно ввести ровно {n} чисел.")
            except ValueError:
                print("Ошибка: вводите только целые числа.")
    
    adj_matrix = np.array(adj_matrix)
    print("\nВведенная матрица смежности:")
    print(adj_matrix)

    # === Пункт 3: Матрица инцидентности ===
    print("\n=== Пункт 3: Матрица инцидентности ===")
    # Найдем все ребра (верхний треугольник матрицы)
    edges = []
    for i in range(n):
        for j in range(i + 1, n):
            if adj_matrix[i][j] == 1:
                edges.append((i, j))
    
    num_edges = len(edges)
    print(f"Обозначение ребер: {[(vertices[u], vertices[v]) for u, v in edges]}")
    
    # Создаем матрицу инцидентности (вершины x ребра)
    inc_matrix = np.zeros((n, num_edges), dtype=int)
    for edge_idx, (u, v) in enumerate(edges):
        inc_matrix[u][edge_idx] = 1
        inc_matrix[v][edge_idx] = 1
        
    print("Матрица инцидентности (строки - вершины, столбцы - ребра):")
    print(inc_matrix)

    # === Пункт 4: Матрица Кирхгофа ===
    print("\n=== Пункт 4: Матрица Кирхгофа ===")
    # Матрица Кирхгофа = Матрица степеней - Матрица смежности
    degree_matrix = np.diag(np.sum(adj_matrix, axis=1))
    kirchhoff_matrix = degree_matrix - adj_matrix
    
    print("Матрица Кирхгофа:")
    print(kirchhoff_matrix)

    # === Пункт 5: Эксцентриситет и радиус графа ===
    print("\n=== Пункт 5: Эксцентриситет и радиус графа ===")
    
    # Находим матрицу кратчайших расстояний (алгоритм Флойда-Уоршелла)
    # Инициализация: бесконечность, кроме себя самого (0)
    dist_matrix = np.full((n, n), np.inf)
    np.fill_diagonal(dist_matrix, 0)
    
    # Заполняем прямые связи
    for i in range(n):
        for j in range(n):
            if adj_matrix[i][j] == 1:
                dist_matrix[i][j] = 1
                
    # Алгоритм Флойда-Уоршелла
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist_matrix[i][k] + dist_matrix[k][j] < dist_matrix[i][j]:
                    dist_matrix[i][j] = dist_matrix[i][k] + dist_matrix[k][j]
    
    print("Матрица кратчайших расстояний:")
    print(dist_matrix)
    
    # Эксцентриситет вершины - максимальное расстояние от неё до любой другой вершины
    eccentricities = {}
    for i in range(n):
        ecc = int(np.max(dist_matrix[i]))
        eccentricities[vertices[i]] = ecc
        print(f"Эксцентриситет вершины {vertices[i]}: {ecc}")
        
    # Радиус графа - минимальный эксцентриситет
    radius = min(eccentricities.values())
    print(f"Радиус графа: {radius}")

    # === Пункт 6 (в задании опечатка, ищем путь A-E, но E нет) ===
    # Будем искать путь между A и C (так как это крайние вершины)
    # Или просто выведем расстояния от A до всех остальных
    print("\n=== Пункт 6: Кратчайший путь (по условию A и E, но E нет) ===")
    print("Так как вершины E нет на графе, выведем кратчайшие расстояния от вершины A:")
    
    idx_A = vertices.index('A')
    for i in range(n):
        if i != idx_A:
            print(f"Расстояние от A до {vertices[i]}: {int(dist_matrix[idx_A][i])}")

if __name__ == "__main__":
    main()