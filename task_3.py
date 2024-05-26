import heapq

def dijkstra(graph, start):
    # Ініціалізація
    n = len(graph)  # Кількість вершин у графі
    distances = {vertex: float('infinity') for vertex in graph}  # Відстані до всіх вершин
    distances[start] = 0  # Відстань до початкової вершини 0
    priority_queue = [(0, start)]  # Черга з пріоритетом (відстань, вершина)
    
    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)
        
        # Якщо поточна відстань більша за збережену відстань, продовжуємо
        if current_distance > distances[current_vertex]:
            continue
        
        # Оновлюємо відстані до сусідів
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight
            
            # Якщо нова відстань коротша, оновлюємо її
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
    
    return distances

# Створення графа у вигляді словника суміжності
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

# Вибір початкової вершини
start_vertex = 'A'

# Виконання алгоритму Дейкстри
shortest_paths = dijkstra(graph, start_vertex)

# Виведення результатів
print(f"Найкоротші шляхи від вершини {start_vertex}:")
for vertex, distance in shortest_paths.items():
    print(f"Відстань до вершини {vertex}: {distance}")
