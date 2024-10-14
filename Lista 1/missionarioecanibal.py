from collections import deque

# Função para verificar se o estado é válido
def is_valid_state(m, c):
    return (m == 0 or m >= c) and (3 - m == 0 or 3 - m >= 3 - c)

# Função para gerar novos estados
def get_new_states(state):
    m, c, b = state
    new_states = []
    if b == 0:  # Barco no lado inicial
        if m > 0: new_states.append((m-1, c, 1))  # 1 missionário
        if m > 1: new_states.append((m-2, c, 1))  # 2 missionários
        if c > 0: new_states.append((m, c-1, 1))  # 1 canibal
        if c > 1: new_states.append((m, c-2, 1))  # 2 canibais
        if m > 0 and c > 0: new_states.append((m-1, c-1, 1))  # 1 missionário e 1 canibal
    else:  # Barco no lado final
        if m < 3: new_states.append((m+1, c, 0))  # 1 missionário
        if m < 2: new_states.append((m+2, c, 0))  # 2 missionários
        if c < 3: new_states.append((m, c+1, 0))  # 1 canibal
        if c < 2: new_states.append((m, c+2, 0))  # 2 canibais
        if m < 3 and c < 3: new_states.append((m+1, c+1, 0))  # 1 missionário e 1 canibal
    return [(nm, nc, nb) for (nm, nc, nb) in new_states if is_valid_state(nm, nc)]

# Função BFS para resolver o problema
def solve_missionaries_and_cannibals():
    start = (3, 3, 0)  # Estado inicial
    goal = (0, 0, 1)   # Estado objetivo
    queue = deque([(start, [])])  # Fila de estados a explorar, junto com o caminho percorrido
    visited = set([start])  # Conjunto de estados visitados

    while queue:
        (state, path) = queue.popleft()
        if state == goal:
            return path + [state]

        for new_state in get_new_states(state):
            if new_state not in visited:
                visited.add(new_state)
                queue.append((new_state, path + [state]))

    return None  # Se não houver solução

# Teste
solution = solve_missionaries_and_cannibals()
for step in solution:
    print(step)

