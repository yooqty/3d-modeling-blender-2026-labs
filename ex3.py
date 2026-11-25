import heapq
import networkx as nx
import matplotlib.pyplot as plt
import math

# Матрица смежности из задания (все веса = 1, 0 = нет ребра)
WEIGHT_MATRIX = [
    [0, 0, 0, 1, 0, 1, 0, 0, 0, 0], # 0
    [0, 0, 1, 1, 0, 1, 1, 1, 0, 0], # 1
    [0, 1, 0, 1, 0, 0, 0, 0, 1, 0], # 2
    [1, 1, 1, 0, 0, 1, 0, 0, 1, 0], # 3
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 0], # 4
    [1, 1, 0, 1, 0, 0, 1, 0, 0, 1], # 5
    [0, 1, 0, 0, 0, 1, 0, 0, 0, 0], # 6
    [0, 1, 0, 0, 1, 0, 0, 0, 0, 1], # 7
    [0, 0, 1, 1, 0, 0, 0, 0, 0, 0], # 8
    [0, 0, 0, 0, 0, 1, 0, 1, 0, 0]  # 9
]

def print_table(step, visited, distances, parents, queue):
    """Вывод таблицы текущего состояния."""
    print(f"\n--- Шаг {step} ---")
    print(f"Очередь (вершина, расстояние): {queue}")
    print(f"Посещенные вершины: {sorted(list(visited))}")
    
    header = "Вершина | " + " | ".join([str(i).center(4) for i in range(len(distances))])
    print("-" * len(header))
    print(header)
    
    dist_str = "Расст.  | " + " | ".join([(str(d) if d != math.inf else "inf").center(4) for d in distances])
    print(dist_str)
    
    par_str = "Родитель| " + " | ".join([(str(p) if p is not None else "-").center(4) for p in parents])
    print(par_str)
    print("-" * len(header))

def dijkstra_with_tables(matrix, start_node, end_node):
    """Алгоритм Дейкстры с выводом промежуточных таблиц."""
    n = len(matrix)
    
    distances = [math.inf] * n
    distances[start_node] = 0
    parents = [None] * n
    visited = set()
    
    pq = [(0, start_node)]
    
    step = 1
    print(f"Начальная вершина: {start_node}, Конечная: {end_node}")
    
    while pq:
        current_dist, current_node = heapq.heappop(pq)
        
        if current_node in visited:
            continue
            
        visited.add(current_node)
        
        print_table(step, visited, distances, parents, pq)
        step += 1
        
        if current_node == end_node:
            print(f"\nДостигнута конечная вершина {end_node}.")
            break
            
        for neighbor in range(n):
            weight = matrix[current_node][neighbor]
            if weight > 0 and neighbor not in visited:
                new_dist = current_dist + weight
                if new_dist < distances[neighbor]:
                    distances[neighbor] = new_dist
                    parents[neighbor] = current_node
                    heapq.heappush(pq, (new_dist, neighbor))
    
    if distances[end_node] == math.inf:
        return None, math.inf
        
    path = []
    curr = end_node
    while curr is not None:
        path.append(curr)
        curr = parents[curr]
    path.reverse()
    
    return path, distances[end_node]

def draw_weighted_graph(matrix, path, title):
    """Отрисовка взвешенного графа с выделением пути."""
    G = nx.Graph()
    n = len(matrix)
    G.add_nodes_from(range(n))
    
    for i in range(n):
        for j in range(i + 1, n):
            if matrix[i][j] > 0:
                G.add_edge(i, j, weight=matrix[i][j])
    
    pos = nx.spring_layout(G, seed=42)
    
    plt.figure(figsize=(10, 8))
    nx.draw_networkx_nodes(G, pos, node_color='lightblue', node_size=700)
    nx.draw_networkx_edges(G, pos, edge_color='gray', width=2)
    nx.draw_networkx_labels(G, pos, font_size=14, font_weight='bold')
    
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=10)
    
    if path:
        path_edges = list(zip(path, path[1:]))
        nx.draw_networkx_nodes(G, pos, nodelist=path, node_color='red', node_size=700)
        nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='red', width=4)
        
    plt.title(title, fontsize=16)
    plt.axis('off')
    plt.show()

def get_valid_input(prompt, max_val):
    while True:
        try:
            val = int(input(prompt).strip())
            if 0 <= val < max_val:
                return val
            else:
                print(f"Ошибка: вершина должна быть в диапазоне от 0 до {max_val - 1}.")
        except ValueError:
            print("Ошибка: пожалуйста, введите целое число.")

def main():
    n = len(WEIGHT_MATRIX)
    print("--- Задание 3: Алгоритм Дейкстры ---")
    print(f"Граф загружен. Количество вершин: {n}")
    
    start_node = get_valid_input("\nВведите номер начальной вершины: ", n)
    end_node = get_valid_input("Введите номер конечной вершины: ", n)
    
    path, total_weight = dijkstra_with_tables(WEIGHT_MATRIX, start_node, end_node)
    
    print("\n--- РЕЗУЛЬТАТ ---")
    if path:
        path_str = " -> ".join(map(str, path))
        print(f"Кратчайший путь: {path_str}")
        print(f"Суммарный вес: {total_weight}")
        draw_weighted_graph(WEIGHT_MATRIX, path, f"Алгоритм Дейкстры: путь {path_str} (вес {total_weight})")
    else:
        print("Путь не найден.")

if __name__ == "__main__":
    main()