import heapq

# Definindo a classe para o nó
class Node:
    def __init__(self, name, g=0, h=0):
        self.name = name  # Nome do nó
        self.g = g        # Custo do caminho desde a origem
        self.h = h        # Heurística
        self.f = g + h    # Custo total

    def __lt__(self, other):
        return self.f < other.f

# Implementação do algoritmo A*
def a_star(graph, start, goal, heuristic):
    open_set = []
    closed_set = set()
    start_node = Node(start, 0, heuristic(start, goal))
    
    heapq.heappush(open_set, start_node)

    came_from = {}  # Para reconstruir o caminho

    while open_set:
        current_node = heapq.heappop(open_set)

        # Se chegamos ao objetivo, reconstruímos o caminho
        if current_node.name == goal:
            return reconstruct_path(came_from, current_node.name), current_node.g

        closed_set.add(current_node.name)

        for neighbor, cost in graph[current_node.name].items():
            if neighbor in closed_set:
                continue
            
            g_cost = current_node.g + cost
            h_cost = heuristic(neighbor, goal)
            neighbor_node = Node(neighbor, g_cost, h_cost)

            # Verifica se o nó já está na lista aberta
            if any(neighbor_node.name == n.name and neighbor_node.g >= n.g for n in open_set):
                continue
            
            # Armazena de onde o nó veio para reconstruir o caminho
            came_from[neighbor] = current_node.name
            
            heapq.heappush(open_set, neighbor_node)

    return [], float('inf')  # Se não há caminho para o objetivo

# Função para reconstruir o caminho
def reconstruct_path(came_from, current):
    total_path = [current]
    while current in came_from:
        current = came_from[current]
        total_path.append(current)
    total_path.reverse()
    return total_path

# Função para calcular a heurística (distância de Manhattan)
def manhattan_distance(node1, node2):
    positions = {
        'A': (0, 0),
        'B': (1, 0),
        'C': (0, 1),
        'D': (1, 1),
        'E': (0, 2),
        'F': (1, 2)
    }
    x1, y1 = positions[node1]
    x2, y2 = positions[node2]
    return abs(x1 - x2) + abs(y1 - y2)

# Definição do grafo com os custos das arestas
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'D': 2},
    'C': {'D': 1, 'E': 5},
    'D': {'F': 3},
    'E': {'F': 2},
    'F': {}
}

# Execução do algoritmo
start_node = 'A'
goal_node = 'F'
path, total_cost = a_star(graph, start_node, goal_node, manhattan_distance)

# Impressão do resultado
print(f'O caminho mais curto de {start_node} até {goal_node} é: {path}')
print(f'O custo total do caminho é: {total_cost}')
