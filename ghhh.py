def find_shortest_path_matrix(matrix, start_idx, end_idx):
    n = len(matrix)
    # Инициализируем массив расстояний бесконечностью
    distances = [float('inf')] * n
    distances[start_idx] = 0
    
    # Массив для отслеживания посещенных вершин
    visited = [False] * n
    
    for _ in range(n):
        # Находим непосещенную вершину с минимальным текущим расстоянием
        min_dist = float('inf')
        current = -1
        
        for i in range(n):
            if not visited[i] and distances[i] < min_dist:
                min_dist = distances[i]
                current = i
                
        # Если вершина не найдена или достигнут конец, прерываем цикл
        if current == -1 or current == end_idx:
            break
            
        visited[current] = True
        
        # Обновляем расстояния до соседей текущей вершины
        for neighbor in range(n):
            weight = matrix[current][neighbor]
            # Если есть ребро (вес > 0) и сосед не посещен
            if weight > 0 and not visited[neighbor]:
                new_dist = distances[current] + weight
                if new_dist < distances[neighbor]:
                    distances[neighbor] = new_dist
                    
    return distances[end_idx]

def main():
    # Запрашиваем размерность матрицы
    while True:
        try:
            n = int(input("Введите количество вершин (например, 5): "))
            if n > 0:
                break
            print("Количество вершин должно быть больше 0.")
        except ValueError:
            print("Ошибка: введите целое число.")

    print("\nВведите матрицу смежности построчно.")
    print("Элементы строки разделяйте пробелами. 0 означает отсутствие дороги.")
    
    matrix = []
    for i in range(n):
        while True:
            try:
                # Считываем строку и разбиваем её по пробелам
                row = list(map(int, input(f"Строка {i+1}: ").split()))
                # Проверяем, что введено ровно n элементов
                if len(row) == n:
                    matrix.append(row)
                    break
                else:
                    print(f"Ошибка: нужно ввести ровно {n} чисел.")
            except ValueError:
                print("Ошибка: вводите только целые числа, разделенные пробелами.")

    # Запрашиваем индексы начала и конца
    print("\nВведите индексы вершин (нумерация с 0).")
    print("Например, для A->E введите 0 и 4.")
    while True:
        try:
            start_idx = int(input("Начальная вершина (индекс): "))
            end_idx = int(input("Конечная вершина (индекс): "))
            if 0 <= start_idx < n and 0 <= end_idx < n:
                break
            else:
                print(f"Ошибка: индексы должны быть от 0 до {n-1}.")
        except ValueError:
            print("Ошибка: введите целое число.")

    # Вычисляем и выводим результат
    result = find_shortest_path_matrix(matrix, start_idx, end_idx)
    
    if result == float('inf'):
        print("\nПуть между указанными вершинами не существует.")
    else:
        print(f"\nВес кратчайшего расстояния: {result}")

if __name__ == "__main__":
    main()