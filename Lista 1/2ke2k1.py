# Função para navegar no espaço de estados
def navigate_state_space(target):
    # Converte o estado alvo para binário
    bin_target = bin(target)[2:]  # Remove o prefixo '0b' da representação binária
    
    # Começa no estado inicial (1)
    current_state = 1
    path = [current_state]
    
    # Remove o bit mais significativo
    bin_path = bin_target[1:]  # Caminho a partir do bit mais significativo removido
    
    # Navega no espaço de estados
    for bit in bin_path:
        if bit == '0':
            current_state = current_state * 2  # Esquerda (multiplica por 2)
        elif bit == '1':
            current_state = current_state * 2 + 1  # Direita (multiplica por 2 e soma 1)
        
        path.append(current_state)  # Adiciona o estado atual ao caminho
    
    return path

# Teste da função
def test_navigation():
    target_state = 11  # Exemplo de estado objetivo
    path = navigate_state_space(target_state)
    
    print(f"Caminho do estado 1 até {target_state}: {path}")

# Executar o teste
test_navigation()