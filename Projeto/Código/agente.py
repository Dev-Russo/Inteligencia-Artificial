from collections import deque
import heapq

class Agente:
    def __init__(self, labirinto, start, goal):
        self.labirinto = labirinto
        self.start = start
        self.goal = goal

    def busca_em_largura(self):
        fila = deque([(self.start, [])])
        visitados = set()
        visitados_ordenados = []

        while fila:
            (x, y), caminho = fila.popleft()
            visitados_ordenados.append((x, y))
            if (x, y) == self.goal:
                return caminho + [(x, y)], visitados_ordenados
            if (x, y) in visitados:
                continue
            visitados.add((x, y))

            for dx, dy in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
                nx, ny = x + dx, y + dy
                if self.labirinto.is_valid_move(nx, ny):
                    fila.append(((nx, ny), caminho + [(x, y)]))
        return [], visitados_ordenados

    def busca_em_profundidade(self):
        pilha = [(self.start, [])]
        visitados = set()
        visitados_ordenados = []

        while pilha:
            (x, y), caminho = pilha.pop()
            visitados_ordenados.append((x, y))
            if (x, y) == self.goal:
                return caminho + [(x, y)], visitados_ordenados
            if (x, y) in visitados:
                continue
            visitados.add((x, y))

            for dx, dy in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
                nx, ny = x + dx, y + dy
                if self.labirinto.is_valid_move(nx, ny):
                    pilha.append(((nx, ny), caminho + [(x, y)]))
        return [], visitados_ordenados

    def distancia_dinamica(self, start, goal):
        fila = deque([(start, 0)])
        visitados = set()

        while fila:
            (x, y), distancia = fila.popleft()
            if (x, y) == goal:
                return distancia
            if (x, y) in visitados:
                continue
            visitados.add((x, y))

            for dx, dy in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
                nx, ny = x + dx, y + dy
                if self.labirinto.is_valid_move(nx, ny):
                    fila.append(((nx, ny), distancia + 1))

        return float('inf')

    ##Busca Dinamica
    def busca_heuristica(self):
        fila_prioridade = []
        heapq.heappush(fila_prioridade, (0, self.start, []))
        visitados = set()
        visitados_ordenados = []

        while fila_prioridade:
            _, (x, y), caminho = heapq.heappop(fila_prioridade)
            visitados_ordenados.append((x, y))
            if (x, y) == self.goal:
                return caminho + [(x, y)], visitados_ordenados
            if (x, y) in visitados:
                continue
            visitados.add((x, y))

            for dx, dy in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
                nx, ny = x + dx, y + dy
                if self.labirinto.is_valid_move(nx, ny):
                    custo = len(caminho) + 1
                    heuristica = self.distancia_dinamica((nx, ny), self.goal)
                    heapq.heappush(fila_prioridade, (custo + heuristica, (nx, ny), caminho + [(x, y)]))
        return [], visitados_ordenados
