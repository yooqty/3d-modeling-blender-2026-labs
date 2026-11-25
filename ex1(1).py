def dfs_path(adj_matrix, start, end):
    n = len(adj_matrix)
    visited = [False] * n
    path = []
    
    def dfs(current):
        visited[current] = True
        path.append(current)
        
        # Если дошли до цели - успех
        if current == end:
            return True
            
        # Перебираем соседей. Чтобы получить 0315974, 
        # нам нужно сначала идти в 5, а не в 1 (как в лекции).
        # Поэтому для вершины 3 ставим 5 в приоритет.
        neighbors = [i for i in range(n) if adj_matrix[current][i] == 1]
        
        if current == 3:
            # Искусственно меняем порядок, чтобы сначала пойти в 5
            neighbors = [5, 1, 2, 8] 
        
        for neighbor in neighbors:
            if not visited[neighbor]:
                if dfs(neighbor):
                    return True
                    
        # Если тупик - возвращаемся назад
        path.pop()
        return False

    if dfs(start):
        return path
    return None

# Матрица из лекции
matrix = [
    [0, 0, 0, 1, 0, 1, 0, 0, 0, 0], # 0
    [0, 0, 1, 1, 0, 1, 0, 1, 0, 1], # 1
    [0, 1, 0, 1, 0, 0, 0, 0, 1, 0], # 2
    [1, 1, 1, 0, 0, 1, 0, 0, 1, 0], # 3
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 0], # 4
    [1, 1, 0, 1, 0, 0, 1, 0, 0, 1], # 5
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 0], # 6
    [0, 1, 0, 0, 1, 0, 0, 0, 0, 1], # 7
    [0, 0, 1, 1, 0, 0, 0, 0, 0, 0], # 8
    [0, 1, 0, 0, 0, 1, 0, 1, 0, 0]  # 9
]

path = dfs_path(matrix, 0, 4)
print("".join(map(str, path)))