import pygame
from labirinto import Labirinto
from agente import Agente

# Configurações do jogo
TAMANHO_CELULA = 40
LARGURA_JANELA = 12 * TAMANHO_CELULA
ALTURA_JANELA = 12 * TAMANHO_CELULA
FPS = 10

CORES = {
    "parede": (31, 31, 32),
    "caminho": (255, 255, 255),
    "inicio": (220, 224, 230),
    "fim": (220, 224, 230),
    "visitado": (86, 126, 187),
    "solucao": (43, 76, 126),
}

# Função para desenhar o labirinto
def desenhar_labirinto(screen, grid, visitados, solucao, start, goal):
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            cor = CORES["parede"] if grid[x][y] == 0 else CORES["caminho"]
            if (x, y) in visitados:
                cor = CORES["visitado"]
            if (x, y) in solucao:
                cor = CORES["solucao"]
            if (x, y) == start:
                cor = CORES["inicio"]
            if (x, y) == goal:
                cor = CORES["fim"]
            pygame.draw.rect(screen, cor, (y * TAMANHO_CELULA, x * TAMANHO_CELULA, TAMANHO_CELULA, TAMANHO_CELULA))

# Inicialização do Pygame
pygame.init()
screen = pygame.display.set_mode((LARGURA_JANELA, ALTURA_JANELA))
pygame.display.set_caption("Busca no Labirinto")
clock = pygame.time.Clock()

# Grid do labirinto
grid = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0],
    [0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0],
    [0, 1, 1, 1, 1, 0, 0, 0, 1, 0, 1, 1],
    [0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0],
    [0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
    [0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0],
    [1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]

labirinto = Labirinto(grid)
agente = Agente(labirinto, start=(4, 11), goal=(10, 0))

# Obter soluções e passos visitados
solucao_bfs, visitados_bfs = agente.busca_em_largura()
solucao_dfs, visitados_dfs = agente.busca_em_profundidade()
solucao_aestrela, visitados_aestrela = agente.busca_heuristica()

# Ciclo do jogo
rodando = True
modo = "bfs"
solucao = []
visitados = []

while rodando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                modo = "bfs"
            elif event.key == pygame.K_2:
                modo = "dfs"
            elif event.key == pygame.K_3:
                modo = "aestrela"

    # Atualizar solução com base no modo selecionado
    if modo == "bfs":
        solucao, visitados = agente.busca_em_largura()
    elif modo == "dfs":
        solucao, visitados = agente.busca_em_profundidade()
    elif modo == "aestrela":
        solucao, visitados = agente.busca_heuristica()

    screen.fill((0, 0, 0))
    desenhar_labirinto(screen, grid, visitados, solucao, (4, 11), (10, 0))

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()