# Definição dos jogos e equipes
games = {
    "J1": ("A", "B"),
    "J2": ("A", "C"),
    "J3": ("A", "D"),
    "J4": ("B", "C"),
    "J5": ("B", "D"),
    "J6": ("C", "D"),
}

# Função para definir os domínios baseados nas restrições
def define_domains(restrictions):
    domains = {game: {1, 2, 3, 4} for game in games}
    for game, teams in games.items():
        domains[game] &= restrictions[teams[0]] & restrictions[teams[1]]
    return domains

# Função para verificar se a atribuição é consistente
def is_consistent(assignment, game, day):
    """Verifica se a atribuição atual é consistente."""
    teams_in_game = games[game]
    # Restrição: uma equipe não pode jogar mais de uma vez no mesmo dia
    for assigned_game, assigned_day in assignment.items():
        if assigned_day == day:
            if set(games[assigned_game]) & set(teams_in_game):
                return False
    return True

# Função principal de backtracking
def backtracking(assignment, domains):
    """Resolve o problema utilizando backtracking."""
    if len(assignment) == len(games):  # Solução completa
        return assignment

    unassigned = [g for g in games if g not in assignment]
    game = unassigned[0]

    for day in domains[game]:
        if is_consistent(assignment, game, day):
            assignment[game] = day
            result = backtracking(assignment, domains)
            if result:  # Solução encontrada
                return result
            del assignment[game]  # Backtrack

    return None  # Sem solução

# Resolver cada caso
def solve_case(case_name, restrictions, additional_constraints=None):
    print(f"Resolvendo {case_name}...")
    domains = define_domains(restrictions)
    if additional_constraints:
        additional_constraints(domains)  # Aplicar restrições adicionais
    solution = backtracking({}, domains)
    if solution:
        print("Solução encontrada:")
        for game, day in sorted(solution.items()):
            print(f"{game} ocorre no dia {day}")
    else:
        print("Nenhuma solução encontrada.")
    print()

# Definição das restrições para cada caso
# Caso (a)
restrictions_a = {
    "A": {1, 2, 3},
    "B": {1, 2, 3, 4},
    "C": {1, 2, 3, 4},
    "D": {2, 3, 4},
}

# Caso (b)
restrictions_b = {
    "A": {1, 2, 3},
    "B": {1, 2, 3, 4},
    "C": {1, 3, 4},
    "D": {2, 3, 4},
}

# Caso (c)
restrictions_c = {
    "A": {1, 2, 3},
    "B": {1, 2, 3, 4},
    "C": {1, 2, 3, 4},
    "D": {2, 3, 4},
}

def additional_constraints_c(domains):
    # Restrição adicional: J3 (A, D) só pode ocorrer no dia 3
    domains["J3"] = {3}

# Resolver os três casos
solve_case("(a)", restrictions_a)
solve_case("(b)", restrictions_b)
solve_case("(c)", restrictions_c, additional_constraints_c)
